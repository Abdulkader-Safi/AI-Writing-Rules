#!/usr/bin/env python3
"""Scan a text file for AI writing tells. Prints findings, exits 2 if any."""

import json
import os
import re
import statistics
import sys

TEXT_EXT = {".md", ".mdx", ".markdown", ".txt", ".rst"}
OPT_OUT = "slop-check: off"
MAX_PER_RULE = 4

# (label, compiled regex, hint)
RULES = [
    ("em dash", re.compile(r"[—―‒]"), "use a full stop, comma, colon, or brackets"),
    (
        "curly quote or ellipsis",
        re.compile(r"[‘’“”…]"),
        "use straight quotes and three dots",
    ),
    (
        "negative parallelism",
        re.compile(
            r"\b(?:it|this|that|we|they|you)\s*(?:'s|’s| is| are|n't| isn't|n’t)?\s*(?:is|are|was|were)?n?'?t?\s+not\s+(?:just\s+)?[^.!?\n]{1,60}?[,;]\s*(?:it|this|that|we|they|you)\s*(?:'s|’s| is| are)\b"
        r"|\b(?:isn'?t|aren'?t|wasn'?t|weren'?t|don'?t|doesn'?t)\s+(?:just\s+)?[^.!?\n]{1,50}?[,;]\s*(?:it|this|that)\s*(?:'s|’s| is)\b"
            r"|\bnot\s+just\s+[^.!?\n]{1,50}?,\s*but\b"
            r"|\bnot\s+only\s+[^.!?\n]{1,60}?\s+but\s+also\b",
            re.I,
        ),
        "delete the negation, keep the positive half",
    ),
    (
        "AI vocabulary",
        re.compile(
            r"\b(?:delve[sd]?|delving|tapestry|vibrant|multifaceted|nuanced|intricate|intricacies"
            r"|realm|testament|foster(?:s|ed|ing)?|leverag(?:e|es|ed|ing)|robust|seamless(?:ly)?"
            r"|underscor(?:e|es|ed|ing)|pivotal|crucial|holistic|transformative|elevat(?:e|es|ed|ing)"
            r"|embark(?:s|ed|ing)?|unlock(?:s|ed|ing)?|harness(?:es|ed|ing)?|showcas(?:e|es|ed|ing)"
            r"|resonat(?:e|es|ed|ing)|garner(?:s|ed|ing)?|boasts?|meticulous(?:ly)?|bolster(?:s|ed|ing)?"
            r"|streamlin(?:e|es|ed|ing)|empower(?:s|ed|ing)?|myriad|plethora|paradigm|quintessential"
            r"|interplay|indelible|groundbreaking|cutting-edge|state-of-the-art|world-class"
            r"|best-in-class|enterprise-grade|game-chang(?:er|ing)|revolutioniz(?:e|es|ed|ing))\b",
            re.I,
        ),
        "replace with the plainest word that carries the meaning",
    ),
    (
        "inflated verb",
        re.compile(
            r"\b(?:utiliz(?:e|es|ed|ing)|facilitat(?:e|es|ed|ing)|ascertain(?:s|ed)?"
            r"|endeavou?r(?:s|ed|ing)?|commenc(?:e|es|ed|ing)|terminat(?:e|es|ed|ing)"
            r"|in order to|prior to|subsequent to|with regard(?:s)? to|regarding"
            r"|a number of|the vast majority of|in the event that)\b",
            re.I,
        ),
        "use / help / find out / try / start / end / to / before / about / some",
    ),
    (
        "dodged copula",
        re.compile(
            r"\b(?:serves?|serving|stands?|standing|functions?|operates?)\s+as\b"
            r"|\brepresents\s+a\b|\bmarks\s+(?:a|the)\s+(?:significant|key|important|pivotal)\b",
            re.I,
        ),
        "say is",
    ),
    (
        "puffed significance",
        re.compile(
            r"\b(?:is\s+a\s+testament|plays?\s+a\s+(?:crucial|pivotal|vital|key|central)\s+role"
            r"|underscor\w+\s+the\s+importance|reflect\w*\s+a\s+broader"
            r"|(?:evolving|broader|changing)\s+landscape|setting\s+the\s+stage"
            r"|significant\s+milestone|key\s+turning\s+point|left\s+an\s+indelible)\b",
            re.I,
        ),
        "state what happened, drop why it matters to the universe",
    ),
    (
        "vague attribution",
        re.compile(
            r"\b(?:experts?\s+(?:say|agree|argue|believe|note)|studies\s+have\s+shown"
            r"|research\s+(?:suggests|shows|indicates)|industry\s+reports?"
            r"|(?:many|some)\s+(?:believe|argue|say)|it\s+is\s+widely\s+(?:regarded|known|believed)"
            r"|observers\s+have|several\s+sources)\b",
            re.I,
        ),
        "name the source or drop the claim",
    ),
    (
        "empty opener",
        re.compile(
            r"(?:^|\n)\s*(?:in\s+today'?s?\s+(?:fast-paced|digital|modern)|in\s+the\s+digital\s+age"
            r"|in\s+an?\s+era\s+of|picture\s+this|imagine\s+a\s+world|we\s+live\s+in\s+a\s+time"
            r"|now\s+more\s+than\s+ever|it'?s\s+no\s+secret|let'?s\s+face\s+it"
            r"|as\s+technology\s+continues)",
            re.I,
        ),
        "delete the sentence, start with the fact",
    ),
    (
        "outline ending",
        re.compile(
            r"\b(?:in\s+conclusion|to\s+conclude|as\s+we\s+look\s+ahead|moving\s+forward"
            r"|only\s+time\s+will\s+tell|challenges\s+and\s+(?:future|opportunities)"
            r"|future\s+(?:outlook|prospects)|it'?s\s+important\s+to\s+note)\b",
            re.I,
        ),
        "end at the last real sentence",
    ),
    (
        "hedge stack",
        re.compile(
            r"\b(?:it\s+could\s+be\s+argued|one\s+could\s+argue|may\s+potentially"
            r"|can\s+sometimes\s+be|to\s+some\s+extent|generally\s+speaking"
            r"|in\s+certain\s+contexts|there\s+is\s+no\s+one-size-fits-all)\b",
            re.I,
        ),
        "make the claim or drop it",
    ),
    (
        "pseudo-wisdom",
        re.compile(
            r"\b(?:the\s+key\s+is\s+to\s+find|at\s+the\s+end\s+of\s+the\s+day"
            r"|it\s+(?:all\s+)?(?:depends|comes\s+down\s+to)\s+(?:on\s+)?your\s+(?:specific\s+)?needs"
            r"|true\s+\w+\s+comes\s+from\s+within|the\s+right\s+balance)\b",
            re.I,
        ),
        "delete it or make it specific",
    ),
    (
        "assistant scaffolding",
        re.compile(
            r"(?:certainly!|i\s+hope\s+this\s+helps|as\s+an\s+ai(?:\s+language\s+model)?"
            r"|let\s+me\s+know\s+if\s+you'?d\s+like|feel\s+free\s+to\s+(?:ask|reach)"
            r"|great\s+question|as\s+of\s+my\s+knowledge\s+cutoff"
            r"|in\s+this\s+(?:article|guide|post),?\s+we(?:'ll|\s+will)\s+explore"
            r"|\[(?:insert|your|company\s+name|placeholder|citation\s+needed)\b)",
            re.I,
        ),
        "strip it",
    ),
    (
        "model artifact",
        re.compile(
            r"(?:oaicite|contentReference|turn\d+search\d+|attributableIndex|\[cite:\s*\d"
            r"|grok_card|grok_render_citation|ppl-ai-file-upload|:::writing|utm_source=)"
        ),
        "leaked markup, delete it",
    ),
    (
        "Title Case heading",
        re.compile(r"(?m)^#{1,6}\s+(?:[A-Z][a-z]+\s+){1,}(?:[A-Z][a-z]+)\s*$"),
        "sentence case: capital on the first word only",
    ),
    (
        "inline-header bullet",
        re.compile(r"(?m)^\s*(?:[-*+]\s+)?\*\*[^*\n]{2,40}\*\*\s*:\s*\S"),
        "write it as prose or drop the label",
    ),
    (
        "trailing -ing commentary",
        re.compile(
            r",\s+(?:highlighting|underscoring|emphasizing|emphasising|ensuring|reflecting"
            r"|symbolizing|symbolising|showcasing|fostering|cultivating|paving\s+the\s+way"
            r"|allowing\s+for|contributing\s+to)\b",
            re.I,
        ),
        "cut everything after the comma",
    ),
]

TRICOLON = re.compile(
    r"\b([a-z]{3,14}), ([a-z]{3,14}),? and ([a-z]{3,14})\b(?!\s*[,:])", re.I
)
TRANSITIONS = re.compile(
    r"(?:^|(?<=[.!?])\s)\s*(?:Furthermore|Moreover|Additionally|In addition|Consequently|Nevertheless"
    r"|Nonetheless|Ultimately|Notably|Importantly|That said|Indeed|Thus|Hence)\b",
    re.I,
)


def strip_noise(text):
    """Blank out fenced code and inline code so we only lint prose."""
    text = re.sub(r"(?ms)^```.*?^```", lambda m: "\n" * m.group(0).count("\n"), text)
    return re.sub(r"`[^`\n]+`", " ", text)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    path = (payload.get("tool_input") or {}).get("file_path") or ""
    if not path or os.path.splitext(path)[1].lower() not in TEXT_EXT:
        return 0
    try:
        with open(path, encoding="utf-8") as fh:
            raw = fh.read()
    except Exception:
        return 0
    if OPT_OUT in raw:
        return 0

    prose = strip_noise(raw)
    lines = prose.split("\n")
    findings = []

    for label, rx, hint in RULES:
        hits = []
        for n, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                hits.append((n, m.group(0).strip()[:60]))
                break
        if hits:
            findings.append((label, hint, hits))

    tri = [
        (n, m.group(0))
        for n, line in enumerate(lines, 1)
        for m in [TRICOLON.search(line)]
        if m
    ]
    words = len(prose.split())
    if len(tri) >= 2 or (tri and words < 250):
        findings.append(
            ("rule of three", "break the triplet: use one, two, or four", tri)
        )

    starts = [l for l in lines if l.strip()]
    conn = TRANSITIONS.findall(prose) if False else TRANSITIONS.findall(prose)
    if len(conn) >= 3:
        findings.append(
            (
                "transition stacking",
                f"{len(conn)} sentences open with a formal connector, delete them",
                [],
            )
        )

    sents = [
        s
        for s in re.split(r"(?<=[.!?])\s+", re.sub(r"(?m)^[#>\-*|].*$", "", prose))
        if len(s.split()) > 2
    ]
    if len(sents) >= 10:
        lens = [len(s.split()) for s in sents]
        mean = statistics.mean(lens)
        burst = statistics.pstdev(lens) / mean if mean else 1
        if burst < 0.4:
            findings.append(
                (
                    "uniform sentence length",
                    f"burstiness {burst:.2f}, human prose is 0.6 to 1.2. "
                    "Put a short sentence next to a long one",
                    [],
                )
            )

    if not findings:
        return 0

    out = [
        f"Writing rules: {len(findings)} issue(s) in {os.path.basename(path)}. Fix before moving on.\n"
    ]
    for label, hint, hits in findings:
        shown = hits[:MAX_PER_RULE]
        more = f" (+{len(hits) - len(shown)} more)" if len(hits) > len(shown) else ""
        locs = "; ".join(f"L{n}: {t}" for n, t in shown) if shown else ""
        out.append(f"  {label}{more}: {hint}")
        if locs:
            out.append(f"    {locs}")
    out.append("\nDetail: the anti-ai-writing skill, or research/ in the plugin.")
    sys.stderr.write("\n".join(out) + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())

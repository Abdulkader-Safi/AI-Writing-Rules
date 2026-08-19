---
description: Audit and rewrite text so it stops reading as AI-generated
argument-hint: [file path, or nothing to use the last thing you wrote]
---

Rewrite `$1` so it reads like a sharp, plain-spoken human wrote it.

If no path was given, use the most recent text you produced in this conversation.

Steps:

1. Read the target. If it is a file, run the checker on it first:
   `echo '{"tool_input":{"file_path":"TARGET"}}' | python3 "${CLAUDE_PLUGIN_ROOT}/scripts/slop-check.py"`

2. Read `${CLAUDE_PLUGIN_ROOT}/skills/anti-ai-writing/SKILL.md` if it is not already in context. Open the specific files in `${CLAUDE_PLUGIN_ROOT}/research/` for any pattern the checker flagged that you are unsure how to fix.

3. Beyond what the checker catches by regex, judge these by reading:
   - The deletion test. Remove each sentence in turn. If the paragraph loses nothing, the sentence goes.
   - Sentence rhythm. If every sentence is 18 to 24 words, break it up.
   - Elegant variation. If one thing has three names, pick one.
   - Register. Does a one-line answer arrive as five paragraphs?

4. Rewrite. Preserve every fact, number, name, link, and code block exactly. Change only how it reads. Do not invent facts to replace vague claims: if a claim has nothing behind it, cut the claim.

5. Apply the edit to the file, then re-run the checker to confirm it comes back clean.

6. Report in three lines or fewer: what you cut, what you rewrote, and anything you left because fixing it needed a fact you do not have.

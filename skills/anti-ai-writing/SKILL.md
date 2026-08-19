---
name: anti-ai-writing
description: Use when writing or editing any prose for a human reader - documentation, READMEs, emails, reports, captions, scripts, blog posts, UI copy, commit messages, PR descriptions - or when asked to remove AI tells, de-slop text, make writing sound human, or check writing style. Applies 29 researched patterns that make text read as machine-generated.
---

# Anti-AI writing

Writing that reads like a sharp, plain-spoken human. Never like AI.

## The one-line test

If you can cut a word and keep the meaning, cut it.

## How to use this

Writing something new: read the hard rules below, write, then run the checklist at the end.

Editing existing text: run `/deslop <file>` or work through the checklist against the draft.

Diagnosing why something reads as AI: find the pattern in the table and open its file in `research/`.

## Hard rules

**No em dashes.** Not a density target, a ban. Use a full stop, a comma, a colon, or brackets. A hyphen inside a word like "plain-spoken" is fine. See `research/15-em-dash-density.md`.

**Straight quotes only.** No curly quotes, no apostrophe character, no ellipsis character. Three dots, or better, no ellipsis.

**Sentence case headings.** Capital on the first word only. Never Title Case. Never skip a heading level. Never open a document with a heading that repeats its own title.

**No negative parallelism.** Kill "not just X, it's Y", "it's not X, it's Y", "not only X but also Y". Delete the negation and keep the positive half. If the positive half cannot stand alone, the sentence had no content.

**Break the rule of three.** Count the items in every list. If they are all three, use one, two, or four instead. This applies to bullets, features, steps, and adjective strings.

**Bold sparingly.** At most one thing per screen. No stacked `**Label:** text` bullets.

**No wrap-up ending.** No "in conclusion", no "challenges and future prospects", no "as we look ahead", no closing paragraph that restates the opening. End at the last real sentence.

**Name the source or drop the claim.** No "experts say", no "studies have shown", no "research suggests".

**No assistant scaffolding.** No "Certainly!", no "I hope this helps", no "As an AI", no placeholder brackets, no knowledge-cutoff notes.

## Vocabulary

Avoid: delve, tapestry, vibrant, multifaceted, nuanced, intricate, realm, landscape (figurative), testament, navigate (figurative), foster, leverage, robust, seamless, underscore, pivotal, crucial, comprehensive, holistic, transformative, elevate, embark, unlock, harness, showcase, resonate, garner, boasts, meticulous, bolster, streamline, empower, myriad, plethora, paradigm, interplay, groundbreaking, cutting-edge, world-class, enterprise-grade.

Plain word beats fancy synonym:

| Not this | This |
|---|---|
| utilize | use |
| facilitate | help |
| regarding | about |
| prior to | before |
| in order to | to |
| commence | start |
| terminate | end |
| ascertain | find out |
| a number of | some, or the number |
| serves as, stands as | is |
| boasts, features | has |

## Rhythm

Vary sentence length. A three-word sentence is legitimate. So is a forty-word one that carries a genuinely long thought through several clauses before it lands.

Measured: burstiness (sentence-length standard deviation divided by mean) sits at 0.6 to 1.2 in human prose and 0.2 to 0.4 in AI output. Uniform 18 to 24 word sentences, paragraph after paragraph, is the single biggest tell of 2026.

Do not lean on commas and "and". Use colons, full stops, and brackets.

## Substance

Every sentence carries a fact, a number, a date, a cause, or a concrete example. Delete each sentence in turn: if the paragraph loses nothing, the sentence was filler.

State what happened. Do not explain why it matters to the universe.

Make the claim or drop it. One honest "I do not know" beats four hedges.

Repeat the real word rather than reaching for a synonym. "The app... the platform... the solution" reads as padded. Pick one name per thing.

## Match the audience

Technical readers: deep and concrete.
Non-technical readers: plain English, no assumed knowledge, no jargon left unexplained.

A question with a one-line answer gets a one-line answer, not five paragraphs with headings.

## The 29 patterns

Full detail, thresholds, and rewrites in `research/`.

| # | Pattern | File |
|---|---|---|
| 01 | AI vocabulary | `research/01-ai-vocabulary.md` |
| 02 | Corporate verb inflation | `research/02-corporate-verb-inflation.md` |
| 03 | Dodging "is" and "are" | `research/03-copula-avoidance.md` |
| 04 | Negative parallelism | `research/04-negative-parallelism.md` |
| 05 | Rule of three on autopilot | `research/05-rule-of-three.md` |
| 06 | Puffed-up significance | `research/06-puffed-significance.md` |
| 07 | Trailing "-ing" commentary | `research/07-participle-commentary.md` |
| 08 | Vague attribution | `research/08-vague-attribution.md` |
| 09 | Promotional language | `research/09-promotional-language.md` |
| 10 | Empty-opener cliches | `research/10-empty-openers.md` |
| 11 | Pseudo-wisdom filler | `research/11-pseudo-wisdom-filler.md` |
| 12 | Transition-word stacking | `research/12-transition-stacking.md` |
| 13 | Uniform sentence length | `research/13-low-burstiness.md` |
| 14 | Thin punctuation | `research/14-punctuation-thinness.md` |
| 15 | Em dash overuse | `research/15-em-dash-density.md` |
| 16 | Curly quotes | `research/16-curly-quotes.md` |
| 17 | Heading tells | `research/17-heading-tells.md` |
| 18 | Excessive bold | `research/18-excessive-bold.md` |
| 19 | Forced tables | `research/19-forced-tables.md` |
| 20 | Outline-shaped endings | `research/20-outline-endings.md` |
| 21 | Elegant variation | `research/21-elegant-variation.md` |
| 22 | Hedging everything | `research/22-hedging.md` |
| 23 | Assistant scaffolding | `research/23-assistant-scaffolding.md` |
| 24 | Model artifacts | `research/24-model-artifacts.md` |
| 25 | The deletion test | `research/25-deletion-test.md` |
| 26 | Canned summaries | `research/26-canned-summaries.md` |
| 27 | Narrow vocabulary range | `research/27-narrow-vocabulary.md` |
| 28 | Treating the title as a thing | `research/28-lead-construction.md` |
| 29 | Register mismatch | `research/29-register-mismatch.md` |

## Checklist before sending

1. Any word from the vocabulary list? Replace it.
2. Any "not just X, it's Y"? Rewrite.
3. Any list of exactly three? Change the count.
4. Any em dash or curly quote? Replace.
5. Any sentence that sounds smart and says nothing? Cut it or make it concrete.
6. Read it aloud. Does it sound like a metronome? Break the rhythm.
7. Could a busy human have written this in a hurry and still sounded sharp? If not, simplify.

## Running the checker

The plugin runs `scripts/slop-check.py` automatically after every Write and Edit on `.md`, `.mdx`, `.txt`, and `.rst` files. To run it by hand:

```sh
echo '{"tool_input":{"file_path":"path/to/file.md"}}' | python3 scripts/slop-check.py
```

Add `<!-- slop-check: off -->` to a file that quotes bad examples on purpose.

<!-- slop-check: off (this file quotes bad examples on purpose) -->

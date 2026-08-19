# Research: AI writing patterns

29 patterns, one per file. Each covers what the pattern is, why models produce it, a measurable threshold where one exists, a bad example, a rewrite, and the fix.

## The core finding
No single pattern proves anything. Every one has an innocent explanation on its own. Three or four converging in the same piece is the signal.

Human readers detect AI writing at roughly chance level. Heavy LLM users reach about 90% accuracy with a 10% false positive rate. So these are heuristics for writing better, not a verdict on anyone's authorship.

## Vocabulary
- [01 AI vocabulary](01-ai-vocabulary.md)
- [02 Corporate verb inflation](02-corporate-verb-inflation.md)
- [27 Narrow vocabulary range](27-narrow-vocabulary.md)

## Sentence patterns
- [03 Dodging "is" and "are"](03-copula-avoidance.md)
- [04 Negative parallelism](04-negative-parallelism.md)
- [05 Rule of three on autopilot](05-rule-of-three.md)
- [07 Trailing "-ing" commentary](07-participle-commentary.md)
- [21 Elegant variation](21-elegant-variation.md)
- [22 Hedging everything](22-hedging.md)

## Substance
- [06 Puffed-up significance](06-puffed-significance.md)
- [08 Vague attribution](08-vague-attribution.md)
- [09 Promotional language](09-promotional-language.md)
- [10 Empty-opener cliches](10-empty-openers.md)
- [11 Pseudo-wisdom filler](11-pseudo-wisdom-filler.md)
- [25 The deletion test](25-deletion-test.md)

## Rhythm and punctuation
- [12 Transition-word stacking](12-transition-stacking.md)
- [13 Uniform sentence length](13-low-burstiness.md)
- [14 Thin punctuation](14-punctuation-thinness.md)
- [15 Em dash overuse](15-em-dash-density.md)
- [16 Curly quotes](16-curly-quotes.md)

## Structure and formatting
- [17 Heading tells](17-heading-tells.md)
- [18 Excessive bold](18-excessive-bold.md)
- [19 Forced tables](19-forced-tables.md)
- [20 Outline-shaped endings](20-outline-endings.md)
- [28 Treating the title as a thing](28-lead-construction.md)

## Leftover machinery
- [23 Assistant scaffolding](23-assistant-scaffolding.md)
- [24 Model artifacts](24-model-artifacts.md)
- [26 Canned summaries](26-canned-summaries.md)
- [29 Register mismatch](29-register-mismatch.md)

## Measurable thresholds, collected
| Pattern | Metric | Flag at |
|---|---|---|
| AI vocabulary | flagged words per 500 words | more than 3, clustered |
| Verb inflation | inflated verbs replacing plain ones | more than 1 per 300 words |
| Empty openers | count per piece | 2 or more per 500 words |
| Vague attribution | uncited authority claims | more than 50% |
| Pseudo-wisdom | sentences surviving deletion | more than a third |
| Rule of three | polished triplets | more than 1 per 200 words |
| "Not just X, it's Y" | occurrences per article | 3 or more |
| Burstiness | sentence-length stdev / mean | under 0.4 (human: 0.6 to 1.2) |
| Transition stacking | paragraphs opening with a connector | more than half |
| Em dashes | per 1,000 words | above 20 (human: 3.2 to 10) |
| Deletion test | paragraphs yielding a concrete fact | more than half failing |

## Sources
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [SlopDetector: 12 patterns with reproducible thresholds](https://slopdetector.org/blog/signs-of-ai-writing)
- [SlopDetector: em dash density measured](https://slopdetector.org/blog/em-dash-ai-tell-data)
- [How to spot AI writing in 2026](https://aiadventureclub.substack.com/p/how-to-spot-ai-writing-in-2026)
- [Fast Company on the Economist report](https://www.fastcompany.com/91584243/how-to-identify-ai-generated-writing-viral-report-has-surprising-new-clues-economist)
- [The Last Fingerprint: how markdown training shapes LLM prose](https://arxiv.org/pdf/2603.27006)

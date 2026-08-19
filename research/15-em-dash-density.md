# Pattern 15: Em dash overuse

## What it is
Em dashes standing in for commas, colons, brackets, and full stops.

## The numbers
- Human prose baseline: 3.2 to 10 em dashes per 1,000 words
- GPT-4.1: 10.62 per 1,000 words, about 3.3 times the human baseline
- Scoring threshold in short modern prose: above 20 per 1,000 words

## Why it happens
One analysis traces it to markdown-saturated training data. The em dash is the smallest surviving unit of the structural, bullet-pointed orientation models pick up from that corpus.

## Status in 2026
The best-known tell, and therefore the most scrubbed. Its absence proves nothing. Its presence in quantity still reads as machine-written to most readers.

## Safi's rule
No em dashes at all. Not a density target, a ban. Use a full stop, a comma, a colon, or brackets. A hyphen inside a word like "plain-spoken" is fine.

This covers the em dash and the longer horizontal bar. The en dash in a number range is acceptable but a plain "to" is better.

## Bad
> The migration took three weeks - longer than planned - and cost us a sprint.

## Good
> The migration took three weeks, longer than planned, and cost us a sprint.
> The migration took three weeks. That was a sprint longer than planned.

Source: [SlopDetector](https://slopdetector.org/blog/em-dash-ai-tell-data), [The Last Fingerprint](https://arxiv.org/pdf/2603.27006), [Fast Company](https://www.fastcompany.com/91584243/how-to-identify-ai-generated-writing-viral-report-has-surprising-new-clues-economist)

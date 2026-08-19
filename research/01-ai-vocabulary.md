# Pattern 01: AI vocabulary

## What it is
A cluster of words that appear far more often in LLM output than in human prose. No single word proves anything. Three or four in the same page is the signal.

## The list, by era
Wikipedia tracks which words dominate in which period, which matters because the list drifts as models change.

**2023 to mid-2024:** additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, intricacies, interplay, key, landscape, meticulous, meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant

**Mid-2024 to mid-2025:** align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant

**Mid-2025 onward:** emphasizing, enhance, highlighting, showcasing, plus notability language such as "independent coverage" and "widely recognized"

**Grok-flavoured:** causal, empirical, correlate, and still underscore

## Why it happens
RLHF rewards prose that reads as thorough and impressive. These words score well on that axis while carrying almost no information.

## Threshold
More than roughly 3 flagged style words per 500 words, clustered, is worth a rewrite.

Reference point: "delve" appeared at about 25 times its pre-ChatGPT frequency in academic abstracts after 2022.

## Bad
> This vibrant, multifaceted platform underscores the crucial role of community in the evolving landscape of remote work.

## Good
> The platform has 40,000 users. Most of them work remotely and use it to find local coworking space.

## Fix
Replace the word with the plainest one that carries the same meaning. If no plain word fits, the sentence probably has no meaning to carry.

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [SlopDetector](https://slopdetector.org/blog/signs-of-ai-writing)

# Pattern 13: Uniform sentence length

## What it is
Every sentence lands in the same range, usually 18 to 24 words, paragraph after paragraph. Called low burstiness.

Called the single biggest AI tell of 2026 by more than one analysis, now that em dashes have been widely scrubbed.

## The metric
Burstiness = standard deviation of sentence length divided by mean sentence length.

- Human writing: 0.6 to 1.2
- AI output: 0.2 to 0.4

Under 0.4 in ordinary prose is a flag.

## Why it happens
Token-by-token generation with a consistent register produces consistent rhythm. Humans vary because they get bored, emphatic, or rushed.

## Bad
> The system processes incoming requests through a queue that manages backpressure automatically. Each worker pulls from the queue and handles the request in an isolated context. The results are then written back to the database in a single transaction.

Three sentences, 16 to 18 words each, same shape.

## Good
> Requests go into a queue. Each worker pulls one, handles it in an isolated context so a crash cannot take down its neighbours, and writes the result back. One transaction. Done.

## Fix
Put a short sentence next to a long one. Three words is a legitimate sentence. So is forty. Read the draft aloud and listen for the metronome.

Source: [SlopDetector](https://slopdetector.org/blog/em-dash-ai-tell-data), [How to spot AI writing in 2026](https://aiadventureclub.substack.com/p/how-to-spot-ai-writing-in-2026)

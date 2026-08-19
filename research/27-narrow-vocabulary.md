# Pattern 27: Narrow vocabulary range

## What it is
Fewer unique words across the same length of text. Measured as type-token ratio: unique words divided by total words.

## The metric
TTR is length-sensitive, so it only means anything when comparing texts of the same length. AI output consistently scores lower than human writing at matched length.

Treat it as a supporting signal, never as the headline. A technical document with a small controlled vocabulary is doing the right thing (see pattern 21 on elegant variation), and it will score low.

## Why it happens
Generation favours high-probability tokens. High-probability tokens are common words. Rarer, more exact words lose out even when they fit better.

## The paradox
This sits next to a contradictory tell: models also reach for obscure polysyllabic words where plain ones would do (delve, tapestry, myriad, plethora, paradigm, quintessential). Both are true. The vocabulary is narrow in the ordinary register and showy in the decorative one.

The result is prose that is simultaneously bland and overwritten.

## Fix
Neither "use rarer words" nor "use simpler words". Use the exact word. Exactness sometimes means a common word and sometimes an uncommon one, and the choice is driven by meaning rather than by texture.

Source: [SlopDetector](https://slopdetector.org/blog/signs-of-ai-writing), [How to spot AI writing in 2026](https://aiadventureclub.substack.com/p/how-to-spot-ai-writing-in-2026)

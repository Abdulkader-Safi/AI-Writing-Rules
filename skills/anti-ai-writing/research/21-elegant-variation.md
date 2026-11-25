# Pattern 21: Elegant variation

## What it is

Swapping in synonyms to avoid repeating a word.

> the app... the platform... the solution... the tool... the software

## Why it happens

An old style-guide rule against repetition, learned from training data, applied mechanically. Wikipedia now lists this as a weakening indicator because models have improved on it, but it still shows up, especially in longer pieces.

## Why it is wrong

Repetition reads as clear. Variation reads as padded, and it makes the reader wonder whether "the platform" and "the tool" are the same thing.

The rule holds hardest in technical writing, where a consistent term is a contract with the reader.

## Bad

> The dashboard loads quickly. The interface pulls data from three sources. The panel then renders the results, and the view updates every 30 seconds.

Four names for one thing.

## Good

> The dashboard loads quickly. It pulls data from three sources and re-renders every 30 seconds.

## Fix

Pick one name per thing and use it every time. Use pronouns for the rest.

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

<!-- slop-check: off (this file quotes bad examples on purpose) -->

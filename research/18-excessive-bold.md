# Pattern 18: Excessive bold

## What it is

Bold applied mechanically to phrases that were not chosen for emphasis, sometimes to every instance of a chosen word.

## Why it happens

Inherited from README files and listicles, which are heavily represented in training data. Bold is a cheap way to signal "this part is important" without deciding what actually is.

## Bad

> The **migration** was **complex** but our **dedicated team** managed to **deliver on time** while **maintaining quality** across **all environments**.

## Good

> The migration was messy but it shipped on the date we promised.

## The related tell: inline-header lists

The stacked pattern where each bullet opens with a bolded label and a colon:

> **Speed:** it's fast.
> **Cost:** it's cheap.
> **Support:** it's good.

Repeated down a page, this reads as generated. It is fine once, as a genuine definition list. It is not fine as the default shape of every section.

## Fix

Bold at most one thing per screen, and only when a reader skimming needs to catch it. If everything is emphasised, nothing is.

Write the inline-header list as prose or as plain bullets without the labels.

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

<!-- slop-check: off (this file quotes bad examples on purpose) -->

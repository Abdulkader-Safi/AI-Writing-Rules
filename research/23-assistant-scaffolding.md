# Pattern 23: Assistant scaffolding

## What it is
Chat-interface furniture left inside the finished text.

## The tells
- "Certainly! Here's a draft of..."
- "I hope this helps!"
- "Let me know if you'd like me to adjust anything"
- "As an AI language model..."
- "As of my knowledge cutoff..."
- "Feel free to..."
- "Great question!"
- Collaborative framing in a document nobody is collaborating on: "we will explore", "let's discuss", "as we examine", "in this article, we will"
- Placeholder brackets left in: [Company Name], [insert date], [citation needed]
- Emoji used as section markers

## Why it happens
The model is answering a person, and the answer wrapper does not get stripped before the text is pasted somewhere.

## Fix
Read the first line and the last line of anything before it ships. That is where scaffolding lives. Search for "[" and for "hope this helps".

Related: the didactic disclaimer opener, "It's important to note that...". Mostly gone from current models but still worth a search.

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

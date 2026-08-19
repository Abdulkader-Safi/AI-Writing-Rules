# Pattern 16: Curly quotes and smart punctuation

## What it is
Typographic quotes and apostrophes where straight ones are standard.

Curly: the paired left and right double quotes, and the curled apostrophe.
Straight: `"` and `'`

## Why it happens
Models emit curly quotes because published prose in training data is typeset. Handwritten markdown, code, and plain text use straight quotes. The mismatch is a fingerprint.

Related: the ellipsis character in place of three full stops, and the multiplication sign in place of an "x".

## Where it matters
Markdown files, code, commit messages, config, anything a machine will parse. Curly quotes in these places break things as well as looking generated.

## Fix
Straight quotes everywhere. Three dots for an ellipsis, or better, no ellipsis. If your editor has smart quotes on, turn it off.

## Quick check
```sh
grep -nP '[\x{2018}\x{2019}\x{201C}\x{201D}\x{2026}]' file.md
```

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

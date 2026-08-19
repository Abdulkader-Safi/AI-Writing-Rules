# Pattern 26: Canned summaries and status reports

## What it is
Wikipedia catalogues this under edit summaries, but it generalises to commit messages, PR descriptions, standup updates, and handover notes.

## The tells
- Emphasising what was preserved rather than what changed: "Preserved all citations", "Retained existing structure", "Maintained backwards compatibility" when nothing threatened it
- Assurances of policy compliance nobody asked for: "Ensured compliance with the style guide", "Followed best practices throughout"
- Generic and repetitive summaries that fit any change: "Updated documentation", "Improved code quality", "Various fixes and enhancements"
- Overemphasis on process over outcome

## Why it happens
The model is signalling diligence because it cannot signal results. A summary of what changed requires knowing what mattered.

## Bad
> Updated the documentation to improve clarity and ensure consistency with existing standards while preserving all original content.

## Good
> Fixed the install steps. They still said Node 16.

## Fix
Say what changed and why. One line. If you cannot name the change, you do not understand it well enough to summarise it.

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

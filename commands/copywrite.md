---
description: Audit or write website copy against 36 researched copywriting rules
argument-hint: [project path, page file, or URL; nothing means the current project]
---

Apply the website copywriting rules to `$1`. If no argument was given, use the current working directory.

The rules live in `${CLAUDE_PLUGIN_ROOT}/copywriting/`. Read `${CLAUDE_PLUGIN_ROOT}/copywriting/README.md` first, then open the rule files each step names. The AI-writing rules from the `anti-ai-writing` skill apply to every word you write as well.

## 1. Decide the mode

- Existing site: the target has pages with real copy (HTML, JSX/TSX, Vue, Svelte, Astro, Blade, PHP templates, Markdown/MDX content, CMS JSON, i18n string files) or is a live URL. Go to step 2A.
- New site: the target is empty, a fresh scaffold with placeholder text (lorem ipsum, "Your headline here"), or the user is describing a site that does not exist yet. Go to step 2B.

If it is unclear, ask one question.

## 2A. Existing site: audit

1. Find the pages. Grep for user-facing strings, skipping `node_modules`, build output, vendor folders and test files. For a URL, fetch the page text. List each page and its type (homepage, landing, product or service, pricing, about, case study, contact, blog, error or 404, forms).
2. For each page, open the matching page rule (22 to 30) and check the copy against it, plus the general rules: 04 headline, 05 subhead, 06 scan, 07 hype, 08 reading level, 09 specific claims, 10 you not we, 13 CTA, 14 terms near the button, 15 form microcopy, 16 proof placement, 21 one action, 31 SEO titles and meta, 32 first sentence answers the heading, 33 accessible copy (alt text, link text, heading order).
3. Flag legal risks from rules 17 and 18 at the top of the report: testimonials that look invented or edited, fake urgency, unstated billing terms.
4. Report per page: the rule number, the exact current text with `file:line`, what is wrong, and a rewrite. Order findings by impact: headline and CTA first, wording last.
5. Ask before editing files. When told to apply, edit only the copy strings, never logic, class names or markup structure.

## 2B. New site: write

1. Research comes first (rules 01 to 03). Ask for whatever is missing, in one message:
   - what the business sells and who buys it
   - the real alternatives a buyer considers
   - customer words: reviews, emails, sales call notes, support questions
   - the top objections that stop people buying
   - real proof: numbers, client names, testimonials with permission
   - the main action each page should drive
2. Plan the pages and the order of sections using the page rules (22 to 30). One main action per page (rule 21).
3. Write the copy. Mark every spot that needs a fact you do not have as `TODO: real figure` or `TODO: real testimonial`. Never invent a number, a client, a review or a deadline (rules 09, 17, 18).
4. If the project has code, put the copy into the actual page files. Otherwise write one Markdown file per page.

## 3. Final check

Run the pre-publish checklist in `${CLAUDE_PLUGIN_ROOT}/copywriting/36-pre-publish-checklist.md` against the result. Then run the slop checker on every file you changed:
`echo '{"tool_input":{"file_path":"TARGET"}}' | python3 "${CLAUDE_PLUGIN_ROOT}/scripts/slop-check.py"`

End with the checklist items that still fail and the TODOs the user has to fill. Nothing else.

# Rule 33: Accessible copy: link text, headings and alt text

## What it is

Accessibility in copy means writing so people using screen readers, magnifiers or translation tools can use the page. Most of it is simply good writing.

## Why it works

The W3C's writing tips map directly to WCAG (the web accessibility standard) success criteria:

| Tip                                                           | WCAG criterion |
| ------------------------------------------------------------- | -------------- |
| Unique, informative page titles                               | 2.4.2          |
| Link text that describes its destination                      | 2.4.4, 2.4.9   |
| Headings that reflect the page structure                      | 2.4.6          |
| Meaningful alt text for images, empty alt for decorative ones | 1.1.1          |
| Clear instructions and error messages                         | 3.3.2          |
| Simple language, expanded abbreviations                       | 3.1.3 to 3.1.5 |

Screen-reader users jump between headings and links, the same way layer-cake scanners do (Rule 06). Google uses headings to build title links. One habit serves three audiences.

## Check

- Read only the links on the page. Does each one say where it goes?
- Read only the headings. Do they outline the page?
- Does every informative image have alt text that says what it shows?
- Is every abbreviation spelled out the first time?

## Bad

> To see our pricing, click here.

> Read more | Read more | Read more

```html
<img src="team.jpg" alt="image" />
```

> Our SLA guarantees 99.9% uptime.

## Good

> See pricing for teams of 1 to 50.

> Read the Bumper to Bumper case study

```html
<img src="team.jpg" alt="The dsrpt team at the Kuwait office" />
```

> Our service level agreement (SLA) guarantees 99.9% uptime.

## Fix

Search the page for "click here", "read more" and "learn more" and rewrite each with the destination. Check headings follow H1, H2, H3 without skipping. Write alt text as you'd describe the image to someone on the phone.

Source: [W3C WAI: writing for web accessibility (2024)](https://www.w3.org/WAI/tips/writing/)

Evidence: strong (W3C official guidance).

<!-- slop-check: off (this file quotes bad examples on purpose) -->

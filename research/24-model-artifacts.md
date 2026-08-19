# Pattern 24: Model artifacts

## What it is

Internal markup that leaks into pasted output. These are proof, not signals. Nothing else produces them.

## By model

**ChatGPT:** `contentReference`, `oaicite`, `oai_citation`, `turn0search0`, `attributableIndex`, a stray `+1`

**Gemini:** `[cite: 1]`, `[span_1](start_span)`

**Grok:** `grok_card`, `grok_render_citation_card_json`

**DeepSeek:** lenticular brackets, dagger symbols

**Perplexity:** `attached_file`, `ppl-ai-file-upload`

**Unclassified:** `:::writing`

## Related evidence

- Citations with `utm_source=` or `utm_medium=` parameters in the URL
- DOIs and ISBNs that are malformed, or that resolve to an unrelated paper
- Named references declared and never used
- External links that 404

## Fix

Grep for these strings before publishing anything that passed through a chat window.

```sh
grep -nE 'oaicite|contentReference|turn0search|\[cite: |grok_card|ppl-ai-|utm_source=' file.md
```

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

<!-- slop-check: off (this file quotes bad examples on purpose) -->

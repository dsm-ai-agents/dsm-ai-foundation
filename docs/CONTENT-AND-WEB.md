# Written material and future web pages

The source of a topic page is a reviewed Markdown article in its collection's `content/` folder, paired with a stable topic ID, source references, and an image. A gallery displays assets; it is not a substitute for the detailed explanation.

## Topic content contract

Use the article template in [the collection template](../templates/research-project/content/topic-template.md). Each article should include:

- Stable topic ID, title, slug, chapter, program, authors, summary, status, and last-reviewed date.
- The question it answers and why the reader should care.
- A plain-language explanation, a familiar example, and a practical application.
- An analogy's limits, common misconceptions, uncertainty, and relevant constraints.
- A small exercise, decision prompt, or next action.
- References to source IDs and the claims they support.
- Image path, meaningful alt text, and previous/next topic IDs where appropriate.

Source paths are relative to the article file. Web routes should use stable collection and topic slugs, not local filesystem paths. Preserve IDs if a title changes. A page's source list must reference the same evidence used in research and visual review.

## Proposed site structure

```text
/collections/
/collections/<collection>/
/collections/<collection>/chapters/<chapter>/
/collections/<collection>/topics/<topic-slug>/
```

Collection pages introduce the purpose and learner journey. Chapter pages explain their relevance and list topics. Topic pages combine the detailed article, reviewed visual, sources, and navigation. Existing decision guides can become useful chapter introductions without being rewritten as generic marketing copy.

## Implementation boundary

Framework, hosting, domain, and public-access settings are not selected here. Each collection's `web/README.md` tracks its page plan and eventual implementation. This reorganization does not publish a website or mark draft articles complete.

Before release, check semantic headings, keyboard navigation, image alt text, contrast, responsive layout, link integrity, source dates, and truthful metadata. Important explanations and caveats must be readable text, not available only inside an image. Generate previews and record review results before deployment. Do not add invented SEO claims, customer evidence, or learning outcomes.

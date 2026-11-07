# Data Science Masterminds — Research Studio

A growing library of research projects that turn evidence into clear explanations, premium educational visuals, and detailed web pages.

**Authors:** Kunaal Naik & Arpan Saxena
**Brand:** Data Science Masterminds
**Programs:** AI Agent Master Class · Agentic Accelerator · Agentic Founder

Research can cover AI, data, technology, business, monetization, leadership, mindset, and future skills. Each collection has its own question, audience, evidence, topic count, and program treatment. A new collection does not need to contain 100 topics.

## Explore the collections

| Collection | Purpose | Available now | Next stage |
| --- | --- | --- | --- |
| [AI Foundations](collections/ai-foundations/README.md) | Explain 100 concepts from beginner literacy to agentic systems, business, and leadership. | 100 concepts, 12 chapter indexes, 112 main visuals, six preserved pilots, and a searchable gallery. | Expand teaching notes into detailed articles and web pages. |
| [AI Income Opportunities](collections/ai-income-opportunities/README.md) | Assess 100 monetization opportunities across 20 industries, including skills, buyers, economics, and validation. | Research, source register, decision guides, 100 opportunity cards, and 121 visuals. | Develop deeper written guides and web pages; validate commercial hypotheses separately. |

See the [collection catalog](collections/README.md) for phase status and direct links. Existing galleries run locally; no website has been deployed by this restructuring.

## The workflow

**Brief → research → synthesis and topic map → written content → image plan and pilot → visual production → web assembly → review and maintenance**

1. Define the question, audience, intended outcome, scope, and program.
2. Research credible sources. Record dates, findings, limitations, and which claims each source supports.
3. Select and sequence topics; assign stable IDs and chapter groupings.
4. Write useful explanations, examples, caveats, and practical next steps. Keep substantive content in text, not only in images.
5. Design the visual explanation for each topic, test a small pilot, and produce the reviewed collection.
6. Assemble web pages from the written material, images, source references, and navigation.
7. Check factual accuracy, clarity, accessibility, links, and rendering. Record updates when evidence or products change.

The current collections began with research and visual production; their detailed articles and web publishing remain planned. Their original research and review records are preserved.

## Repository structure

```text
collections/
  <collection-slug>/
    README.md           # Collection goal, scope, status, and navigation
    project.json        # Identity, program, phase status, and artifact paths
    research/           # Evidence, source register, findings, and methodology
    content/            # Detailed written explanations and chapter narratives
    production/         # Topic catalog, image briefs, prompts, and build scripts
    visuals/            # Reviewed images, indexes, galleries, and manifests
    web/                # Page map, publishing plan, and future site source
    exports/            # Reproducible downloads; ZIPs are not committed
docs/                   # Shared workflow, branding, writing, and migration guide
templates/research-project/
tools/                  # Create collections, rebuild catalog, validate repository
```

## Start another research project

Use Python 3.10 or later; the shared tools use the standard library.

```bash
python tools/new_research.py future-work-skills --title "Future Work Skills" --program "Agentic Accelerator"
python tools/build_catalog.py
python tools/validate_repository.py
```

The first command creates a new collection from the template and refreshes the catalog. It does not conduct research, generate images, or publish a site. Fill in the brief and source register before production. Existing collections are never overwritten.

## Work with existing collections

```bash
# Validate and rebuild the Foundations gallery
python collections/ai-foundations/production/assemble_library.py --require-complete

# Also generate Foundations ZIP downloads locally
python collections/ai-foundations/production/assemble_library.py --require-complete --package

# Validate and rebuild the Income Opportunities gallery
python collections/ai-income-opportunities/production/build_gallery.py --require-complete
```

Open either collection's visual gallery from its README. Insert PNGs into PowerPoint as pictures. Existing images are flattened PNGs at native 1672 × 941, approximately 16:9; editable PowerPoint elements are a separate deliverable.

## Shared standards

- [Research and production workflow](docs/WORKFLOW.md)
- [Brand and visual direction](docs/BRAND.md)
- [Written content and web-page contract](docs/CONTENT-AND-WEB.md)
- [Folder migration guide](docs/MIGRATION.md)

Keep evidence distinct from assumptions, illustrative examples, and predictions. Preserve correct attribution and source references. Every published topic should remain understandable without its image. Research status does not imply customer validation or guaranteed financial outcomes.

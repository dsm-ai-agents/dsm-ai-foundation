# Research-to-publication workflow

Each collection owns its research and deliverables. Shared branding and editorial conventions live in `docs/`; domain-specific decisions belong in the collection README.

| Stage | Required work | Evidence that the stage is ready |
| --- | --- | --- |
| Brief | Define audience, question, outcome, boundaries, geography/date where relevant, and program. | A reader can tell what the collection will and will not answer. |
| Research | Search primary and credible secondary sources; log access dates, exact URLs, findings, and limitations. | Claims can be traced to evidence; missing and inaccessible evidence is marked. |
| Synthesis | Group topics, remove duplicates, define prerequisites, assign stable IDs, and record uncertainty. | Topic catalog and chapter indexes match; speculative claims remain labeled. |
| Writing | Develop an explanation, concrete example, practical application, limitations, and references per topic. | A learner can understand and act on the text without the image. |
| Visual planning | Specify one takeaway, headline, visual metaphor, copy, branding, and qualifications. | A small pilot checks readability and fidelity to the written explanation. |
| Visual production | Generate and review images; preserve prompts, source IDs, native dimensions, and revision notes. | Files cover the planned IDs, indexes match, and examples/diagrams are accurate. |
| Web assembly | Combine accessible written content with images, citations, chapter navigation, and metadata. | Pages render correctly, links work, and every image has useful alt text. |
| Release and upkeep | Record version/review date, publication location, owners, and refresh triggers. | Published status reflects an actual deployment; scheduled upkeep exists only if requested. |

## Evidence rules

- Source IDs are local to the collection and stable across revisions.
- Record which claims a source supports rather than attaching a generic bibliography to every topic.
- Distinguish primary evidence, practitioner opinion, public discussion, and your synthesis.
- Do not infer that an inaccessible page supports a claim. Mark access limitations.
- Business prices, capacities, and projected revenue are hypotheses until tested. Research completion is different from market validation.
- For changing products, retain the review date and verify current behavior before publishing instructions.

## Status and handoffs

`project.json` uses `planned`, `in-progress`, or `complete` for research, written content, visuals, and web. A template begins with all four planned. Change a status only when the corresponding artifacts support it. Completion is scoped to the collection brief; it does not mean exhaustive knowledge of a subject.

Content drafts may inform a pilot while research continues, but unresolved claims must be visible in notes. Existing collections can retain their original structure inside each stage folder; future projects should start with the shared template. The catalog is generated from project manifests.

When parallel work is requested, assign non-overlapping chapter or topic IDs, keep the source catalog stable, and assemble only reviewed outputs. Do not regenerate existing approved images as part of a folder migration.

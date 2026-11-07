# AI income opportunity image production

Authorized 7 November 2026 after committing the research. Target: one master decision index image, 20 chapter index images, and 100 topic images (121 PNGs total). Preserve the existing AI Foundations library.

## Shared style

Follow ../../ai-foundations/visuals/pilot/shared-art-direction.txt for premium restraint, friendly polished 3D objects, readable English, Space Grotesk-like headings, Inter-like body, subtle studio lighting, 6% safe margins, and landscape 16:9 composition. Adapt background to deep evergreen #142823 fading to near-black green; ivory/white text, amber #F4B544 accents and muted teal details. Entrepreneurial, grounded, no money piles, robots or wealth promises. Footer exactly: Data Science Masterminds | Agentic Founder | Kunaal Naik & Arpan Saxena. New entrepreneurial treatment, not a separate approved corporate standard.

## Decision focus

Research is in ../research/ideas.json; chapter indexes in ../research/chapters/NN-index.md. Each topic must help the reader assess fit and decide a first test. Do not simply explain AI.

Each topic image: AI-### category eyebrow; clear short offer headline; one short 'Consider this if...' fit line; one dominant practical deliverable visual; concise 'Sell' and 'First test' blocks; test price only if clearly labeled 'Price hypothesis'; one brief limitation. Prefer under 95 words plus footer. Do not invent buyer evidence or income. Revenue examples, if included, must be labeled illustrative gross revenue before costs. Full assumptions and source links belong in chapter README. No guaranteed earnings.

Each chapter index: chapter number, short industry title, one fit/why sentence, all five exact idea IDs and recognizable topic titles, one 'Choose one problem. Test one paid offer.' line, minimal imagery and exact footer. Use concise titles when necessary without changing meaning.

## Ownership and generation

Agents own only assigned collections/ai-income-opportunities/visuals/chNN/ directories; root owns overview, gallery and integration. No agent git commits or pushes. Read parent style, this file, source JSON and assigned indexes before generation.

Use image_gen__imagegen for every new image; no Python image creation/editing. Run at most two independent generations concurrently per agent. Use functions.exec initial yield_time_ms 120000 and resume any yielded cell rather than restarting. Return finished outputs through generatedImage(result). Tool output_hint identifies native saved path, often /workspace/generated_images; copy original PNG into chapter folder. Never print base64 or put it in manifests.

Each chapter: 00-chapter-index.png, then AI-NNN-slug.png for five topics; manifest.json with source idea ID, filename, exact prompt, original path, actual dimensions and review notes; README.md linking source topics and listing files. Inspect every image; correct material spelling, clipping, numeric, branding or misleading-claim defects using imagegen. Retain actual dimensions, never claim 1920x1080 without checking. Flattened PNGs, not editable PowerPoint. Save prompts before calls so interrupted work can resume.

Report progress after each chapter, and report any tool failure without fabricating outputs. Proceed through all assigned chapters; do not stop after a pilot. Need no additional approval; user explicitly authorized parallel image production.

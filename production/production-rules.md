# Chapter image production rules

Produce the user-approved 100-concept series, organized in twelve chapters. Six agents each own two chapters. Each chapter needs an introduction/index image listing its topics and explaining why the chapter matters, followed by numbered concept images. No extra all-100 overview or timed slide is requested.

Read `curriculum.json` for exact topic IDs, teaching points, visual ideas, and chapter rationale. Read `../assets/pilot/shared-art-direction.txt` for visual style. Replace the phrase “six-slide pilot” with “100-concept series” when composing generation prompts. All images use the accepted APEX design, Agentic Accelerator branding, and Kunaal Naik & Arpan Saxena author attribution.

## Ownership and output

- Work only in your assigned `assets/chapters/chNN/` directories. Do not edit the root README, curriculum, or other chapters.
- Create `00-chapter-index.png` plus one `NNN-slug.png` for each concept. Preserve concept numbers 001–100.
- Reuse the six approved pilot images by copying them into the appropriate chapter: 004, 021, 040, 060, 091, 095. Do not regenerate these.
- Keep generated originals in `/workspace/generated_images`; copy them to chapter folders based on the tool's returned `output_hint` path.
- Save `manifest.json` in each chapter with chapter number, title, rationale, and each image's concept ID (or index), filename, headline, exact generation prompt (or reused pilot path), native width/height, and review notes. Never store base64 data in manifests.
- Save a concise chapter `README.md` listing images in order, teaching qualifications, source links, and review status. These are repository documentation, not a new Page.

## Generation and review

- Use `tools.image_gen__imagegen` for all new images. No Python or other image editing.
- Run up to two independent generation calls concurrently per agent; await them and use `generatedImage(result)` to return each result as instructed by the tool. Tool execution may yield; resume the yielded cell, do not restart it.
- Avoid printing base64 data. Print only concept ID and `output_hint` when needed.
- Each concept slide needs a short clear headline, one accurate supporting sentence, one dominant visual, and the exact footer branding. All text in English. Avoid excessive tiny text.
- A chapter index is a chapter opener, not a concept slide. It needs chapter number, title, one brief “why this matters” sentence, all 8 or 10 topic names with IDs in two readable columns, and discreet footer branding. Use very limited imagery so the index remains readable. Avoid full paragraph explanations for each topic.
- Inspect every generated image using its tool output or `view_image` if the image was omitted from output. Check spelling, author names, factual distinctions, arrow directions, legibility, clipping, and index completeness. Correct material errors with imagegen.
- Illustrative numeric examples must be explicitly labeled. Do not imply guaranteed financial returns, human-like consciousness, or that prompts automatically retrain model weights.
- Native generator dimensions are often 1672 × 941, approximately 16:9. Record actual dimensions; do not claim 1920 × 1080 unless true. The deliverables are flattened PNGs, not editable PowerPoint slides.
- If generation is persistently blocked, report the exact issue and finish unaffected documentation; never fabricate completion or placeholder images.

## Content research sources

- ML/data: https://github.com/microsoft/ML-For-Beginners and https://github.com/microsoft/Data-Science-For-Beginners
- Generative AI: https://github.com/microsoft/generative-ai-for-beginners
- Agents/context: https://github.com/microsoft/ai-agents-for-beginners
- Workflows: https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents
- Skills: https://github.com/anthropics/skills
- Agent runtime: https://github.com/openai/openai-agents-python/tree/main/docs
- MCP: https://github.com/modelcontextprotocol/modelcontextprotocol
- Diffusion: https://github.com/huggingface/diffusers/blob/main/docs/source/en/using-diffusers/write_own_pipeline.md
- Web APIs: https://github.com/mdn/content
- Webhooks: https://github.com/github/docs/blob/main/content/webhooks/about-webhooks.md
- Security: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10

Business and leadership topics are original pedagogical recommendations informed by the user's program brief. Separate those recommendations from measured outcomes. Include conceptual caveats in chapter notes rather than crowding slides.

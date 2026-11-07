# Chapter 04 — Generative AI and prompting

Why it matters: understand generation and give clear instructions that produce useful, checkable results.

| Order | Concept | Image |
| --- | --- | --- |
| Index | Chapter introduction and topic list | [Chapter index](00-chapter-index.png) |
| 025 | Large language models | [Image](025-large-language-models.png) |
| 026 | Tokens | [Image](026-tokens.png) |
| 027 | Context window | [Image](027-context-window.png) |
| 028 | Attention | [Image](028-attention.png) |
| 029 | Diffusion | [Image](029-diffusion.png) |
| 030 | A clear prompt | [Image](030-a-clear-prompt.png) |
| 031 | Few-shot prompting | [Image](031-few-shot-prompting.png) |
| 032 | Output contracts | [Image](032-output-contracts.png) |
| 033 | Task decomposition | [Image](033-task-decomposition.png) |
| 034 | Verification | [Image](034-verification.png) |

## Teaching qualifications

- Next-token generation is a useful simplified explanation of autoregressive LLM output; it is not a complete account of training, reasoning, or the surrounding application.
- Token splits vary by tokenizer and language. The depicted split is illustrative, not a measurement of a specific tokenizer.
- A context window is bounded input/working space; inclusion does not guarantee perfect retrieval or use of every detail.
- Attention weights relationships in representations; the pronoun example is simplified and does not imply human understanding or provide a full attention map.
- Diffusion is one family of generation approaches, not a universal description of all image models. The illustration shows a simplified denoising process.
- Clear prompts improve task specification but do not guarantee accuracy. Respect model-specific instruction and formatting behavior.
- Few-shot examples demonstrate an output pattern without necessarily changing model parameters.
- A requested output format should be enforced or validated before downstream use; prompting alone is not a schema guarantee.
- Decomposition helps manage complexity but introduces handoffs and possible accumulated errors.
- Verification should use relevant sources, executable checks, and human judgment where needed. Model self-confidence is not proof.

## Sources

- [Microsoft: introduction to generative AI](https://github.com/microsoft/generative-ai-for-beginners/blob/main/01-introduction-to-genai/README.md)
- [Microsoft: prompt engineering fundamentals](https://github.com/microsoft/generative-ai-for-beginners/blob/main/04-prompt-engineering-fundamentals/README.md)
- [Hugging Face: diffusion pipelines](https://github.com/huggingface/diffusers/blob/main/docs/source/en/using-diffusers/write_own_pipeline.md)

## Production and review

Flattened PNGs use the approved dark navy, amber, and teal APEX identity. Exact prompts and actual native dimensions are recorded in `manifest.json`. Review status is recorded per image in the manifest; audience comprehension and projector readability require live review.

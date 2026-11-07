# Chapter 05 — Context, knowledge, and memory

Give AI the right information at the right time instead of relying on longer prompts alone.

| Order | Image | Teaching point |
| --- | --- | --- |
| Introduction | [Chapter index](00-chapter-index.png) | Eight concepts and why they matter. |
| 035 | [Context engineering](035-context-engineering.png) | Select the right information for the next step. |
| 036 | [Grounding](036-grounding.png) | Connect claims to supporting evidence. |
| 037 | [Embeddings](037-embeddings.png) | Represent items numerically for similarity comparisons. |
| 038 | [Semantic search](038-semantic-search.png) | Match meaning beyond exact words. |
| 039 | [Chunking](039-chunking.png) | Create useful retrieval units. |
| 040 | [Retrieval-augmented generation](040-retrieval-augmented-generation.png) | Retrieve, add context, then generate. Approved pilot reused. |
| 041 | [Persistent memory](041-persistent-memory.png) | Store selected information for later interactions. |
| 042 | [RAG versus fine-tuning](042-rag-vs-fine-tuning.png) | Reference context and parameter training are distinct. |

## Teaching qualifications

- Context engineering includes selection, prioritization, compression, and isolation; more context is not automatically better context.
- Grounding does not guarantee factual correctness. Check whether the source is reliable, current, and genuinely supports the claim.
- The embedding map is an illustration, not a measured projection of a real embedding model. Semantic similarity depends on model, task, and representation.
- Semantic search can miss or mis-rank relevant material. Exact terms and filters can remain useful.
- Chunk boundaries and overlap should suit the material. No single chunk size works best for every application.
- RAG does not itself retrain model parameters. Retrieval and generation require separate evaluation.
- Persistent memory is an application capability with retention, privacy, and correction needs. It is distinct from the current context window and from model training.
- RAG and fine-tuning can be combined; the comparison does not imply an exclusive choice.

## Sources

- [Microsoft: context engineering](https://github.com/microsoft/ai-agents-for-beginners/blob/main/12-context-engineering/README.md)
- [Microsoft: agent memory](https://github.com/microsoft/ai-agents-for-beginners/blob/main/13-agent-memory/README.md)
- [Microsoft: RAG and vector databases](https://github.com/microsoft/generative-ai-for-beginners/blob/main/15-rag-and-vector-databases/README.md)
- [Microsoft: fine-tuning](https://github.com/microsoft/generative-ai-for-beginners/blob/main/18-fine-tuning/README.md)

## Production

APEX styling; Data Science Masterminds; Agentic Accelerator; Kunaal Naik & Arpan Saxena. Images are flattened native PNGs, approximately 16:9; actual dimensions and generation/reuse records are in `manifest.json`. `generation-specs.json` preserves exact new-image prompts. Live learner comprehension and projector checks remain to be performed.

All nine images completed and visually reviewed. Topic IDs, index completeness, author spelling, readability, and conceptual distinctions checked. PNG integrity verified. Native dimensions: 1672 × 941.

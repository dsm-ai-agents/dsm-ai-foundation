# Chapter 09 — Quality, safety, and reliability

Test and monitor systems before trusting them with consequential work.

Brand: Data Science Masterminds · Agentic Accelerator

Authors: Kunaal Naik & Arpan Saxena

## Image index

| Concept | Image | Teaching point |
| --- | --- | --- |
| index | [Chapter introduction and index](00-chapter-index.png) | Test and monitor systems before trusting them with consequential work. |
| 069 | [Evaluations](069-evaluations.png) | Test representative tasks against explicit success criteria. |
| 070 | [Precision and recall](070-precision-and-recall.png) | False alarms and missed cases are different errors. |
| 071 | [RAG evaluation](071-rag-evaluation.png) | Assess retrieval and answer support separately. |
| 072 | [Guardrails](072-guardrails.png) | Checks constrain behavior but do not guarantee safety or correctness. |
| 073 | [Prompt injection](073-prompt-injection.png) | Untrusted content may attempt to redirect the system. |
| 074 | [Least privilege and human approval](074-least-privilege-and-human-approval.png) | Grant necessary access and review consequential actions. |
| 075 | [Tracing and observability](075-tracing-and-observability.png) | Record events so failures can be investigated. |
| 076 | [Quality, latency, and cost](076-quality-latency-and-cost.png) | Evaluate tradeoffs against the task's needs. |

## Teaching qualifications

- **069 — Evaluations:** The driving course is an analogy. Evaluation suites should include representative normal cases, edge cases, and expected failure behavior. A junction is a scenario to test, not inherently a failure.
- **070 — Precision and recall:** Precision = true positives / (true positives + false positives). Recall = true positives / (true positives + false negatives). The shapes are illustrative; discuss the selected set and relevant set explicitly.
- **071 — RAG evaluation:** Retrieval relevance and answer faithfulness need separate checks. A correctly quoted but outdated source can still produce an unsuitable answer.
- **072 — Guardrails:** Guardrails reduce particular risks; they are not complete security or correctness guarantees. Check inputs, actions, and outputs at appropriate boundaries.
- **073 — Prompt injection:** The embedded instruction is a deliberately suspicious example, not an instruction for the audience to follow. Retrieved content is untrusted evidence, not permission to override the user.
- **074 — Least privilege and human approval:** Keyring and gate are an analogy. Enforce actual permissions and meaningful human review for consequential actions; prompts alone are insufficient.
- **075 — Tracing and observability:** The trace is simplified. A tool error may still lead to an error response or recovery; a result event does not necessarily mean business success. Limit sensitive data in logs.
- **076 — Quality, latency, and cost:** Controls illustrate a tradeoff, not independent physical settings or measured benchmarks. Establish task-specific acceptance criteria.

## Sources

- [Microsoft: AI agents in production](https://github.com/microsoft/ai-agents-for-beginners/blob/main/10-ai-agents-production/README.md) — evaluation, costs, monitoring, and deployment.
- [OpenAI Agents SDK: tracing](https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md) — recorded workflow events.
- [OpenAI Agents SDK: guardrails](https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md) — input, output, and tool checks.
- [OWASP GenAI risks](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10) — prompt injection, excessive agency, sensitive data, and output handling.
- [Microsoft: Generative AI application lifecycle](https://github.com/microsoft/generative-ai-for-beginners/blob/main/14-the-generative-ai-application-lifecycle/README.md) — building, evaluation, deployment, and monitoring.
- Workplace scenarios are original teaching examples aligned with the user-supplied APEX brief; no business performance outcomes are claimed.

## Review and file details

All nine images were visually reviewed for readable text, correct attribution, concept distinctions, index completeness, and relevant diagram directions. Native dimensions were verified from PNG headers. All are 1672 × 941, approximately 16:9, with flattened typography. Live audience comprehension and projector readability have not been tested. Exact generation prompts and original image paths are recorded in `manifest.json`.

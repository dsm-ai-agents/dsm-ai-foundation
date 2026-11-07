# Chapter 06 — Technology building blocks

Understand how AI connects to software and becomes a working application.

| Order | Image | Teaching point |
| --- | --- | --- |
| Introduction | [Chapter index](00-chapter-index.png) | Eight concepts and why they matter. |
| 043 | [APIs](043-apis.png) | Defined interfaces connect software. |
| 044 | [JSON and schemas](044-json-and-schemas.png) | Structured fields and validation rules. |
| 045 | [Databases and queries](045-databases-and-queries.png) | Store records and retrieve what is needed. |
| 046 | [Webhooks](046-webhooks.png) | Events notify subscribed systems. |
| 047 | [Authentication and authorization](047-authentication-and-authorization.png) | Identity is distinct from permission. |
| 048 | [Frontend and backend](048-frontend-and-backend.png) | Interface and underlying processing work together. |
| 049 | [Version control](049-version-control.png) | Track revisions and recover earlier versions. |
| 050 | [Deployment](050-deployment.png) | Make the tested application available. |

## Teaching qualifications

- APIs include more than web services. The service-counter illustration is an analogy for a defined interface.
- JSON is a data format; a schema specifies expected structure and constraints. A valid structure does not prove that data values are accurate.
- Databases can use different data models and query mechanisms. The cabinet is an analogy, not a technical architecture.
- Webhook deliveries can be retried or duplicated. Production handlers need verification, error handling, and appropriate idempotency.
- Authentication establishes identity; authorization determines permitted actions. Both need continued enforcement, not merely a login screen.
- Frontend/backend boundaries vary across architectures. The restaurant comparison is introductory.
- Version control is not a substitute for a comprehensive backup strategy or a guarantee that a rollback will undo external side effects.
- Deployment is not the end of delivery: monitoring, maintenance, permissions, and recovery matter after release.

## Sources

- [MDN: API introduction](https://github.com/mdn/content/blob/main/files/en-us/learn_web_development/extensions/client-side_apis/introduction/index.md)
- [GitHub: webhooks](https://github.com/github/docs/blob/main/content/webhooks/about-webhooks.md)
- [Microsoft: web development curriculum](https://github.com/microsoft/Web-Dev-For-Beginners)
- [Microsoft: generative AI application lifecycle](https://github.com/microsoft/generative-ai-for-beginners/blob/main/14-the-generative-ai-application-lifecycle/README.md)

## Production

APEX styling; Data Science Masterminds; Agentic Accelerator; Kunaal Naik & Arpan Saxena. Images are flattened native PNGs, approximately 16:9; actual dimensions and generation records are in `manifest.json`. `generation-specs.json` preserves exact prompts. Live learner comprehension and projector checks remain to be performed.

All nine images completed and visually reviewed. Topic IDs, index completeness, author spelling, readability, and diagram directions checked. Concept 045 was revised to explicitly label its hypothetical order data as an illustrative example. PNG integrity verified. Native dimensions: 1672 × 941.

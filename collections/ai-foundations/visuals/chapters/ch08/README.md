# Chapter 08 — Agents and agentic systems

Understand how agents select actions, use tools, and coordinate within boundaries.

This chapter contains one introduction/index image and ten concept images. Data Science Masterminds · Agentic Accelerator · Kunaal Naik & Arpan Saxena.

## Image index

- [Chapter index — Agents and agentic systems](00-chapter-index.png)
- [059 — AI agents](059-ai-agents.png)
- [060 — Agent loop](060-agent-loop.png)
- [061 — Planning and replanning](061-planning-and-replanning.png)
- [062 — Tool calling](062-tool-calling.png)
- [063 — Agent harness](063-agent-harness.png)
- [064 — State and checkpoints](064-state-and-checkpoints.png)
- [065 — Multi-agent orchestration](065-multi-agent-orchestration.png)
- [066 — Model Context Protocol (MCP)](066-model-context-protocol-mcp.png)
- [067 — Agent-to-agent communication](067-agent-to-agent-communication.png)
- [068 — Computer-use agents](068-computer-use-agents.png)

## Teaching qualifications

- The cook illustration is an analogy for dynamically choosing actions, not a claim that agents possess human experience or judgment. A fixed workflow can still contain conditional branches; the distinction is who chooses the control flow.
- The observe/decide/act loop is a simplified model. Explicit exits, budgets, permissions, and human oversight are necessary. Concept 060 reuses the approved pilot unchanged.
- Planning is revisable rather than guaranteed correct. The driving analogy shows the original road blocked and an alternate paved route to the same goal.
- Tool calling is a model request executed by surrounding software; execution can fail or be refused. The assistant does not automatically have permission for every tool action.
- Agent harness is an implementation-dependent term for supporting runtime software. The diagram is conceptual, not a universal software architecture.
- Checkpoints save selected state. Recovery may also require idempotent operations or compensating actions so completed external work is not duplicated.
- Multi-agent orchestration adds coordination, latency, and cost. More agents do not automatically improve quality; the coordinator diagram shows role assignment, not all timing dependencies.
- MCP uses host applications with clients connected to servers exposing capabilities. The arrows illustrate connections, not one-way-only communication. MCP alone does not make data trustworthy or actions safe; authorization and validation still matter.
- Agent-to-agent communication is represented by a task and result exchange. Protocols, identities, access rights, and failure handling still require explicit design. The service desks are an analogy.
- Computer-use agents interact through application interfaces. They should operate within access boundaries and ask before consequential actions; interfaces and observations can change or be misunderstood.

## Sources

- [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python/tree/main/docs)
- [Anthropic workflow patterns](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol)

## Review and format

Images are reviewed for exact author names, numbering, readable text, diagram direction, and appropriate teaching qualifications. Replanning geometry was corrected so the original route is actually blocked; harness wording was simplified. Native image dimensions and final review notes are recorded per image in manifest.json. PNG typography is flattened and the images are approximately 16:9. No audience testing or editable PowerPoint text is claimed.

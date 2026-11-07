# Data Science Masterminds — AI Foundations

A continuous journey through 100 concepts that helps professionals understand AI, apply it at work, build agentic workflows, and develop the business judgment and leadership skills to create value.

**Brand:** Data Science Masterminds

**Authors:** Kunaal Naik & Arpan Saxena

**Language:** English, with globally relatable examples

**Primary format:** 16:9 visuals for live teaching and PowerPoint presentations

## Project goal

Research, sequence, and explain 100 essential concepts across AI, data, technology, business, mindset, leadership, and future skills. Turn each concept into a clear, memorable visual with a premium, consistent identity.

Begin with “What is AI?” and progress toward practical workflows, agentic systems, business application, and monetizing skills and knowledge. The library is one connected learning journey, with concepts mapped to the appropriate programs and reused where useful.

This README is the project brief. The researched 100-concept outline and visual directions are saved in [the production plan](production/100-image-plan.md). The user approved the six-image pilot and authorized full production across twelve chapters. Program-specific curriculum packaging and live learner validation remain separate steps.

**Image library:** Browse the [master chapter index](assets/chapters/INDEX.md) or [local visual gallery](assets/chapters/gallery.html). The first complete collection contains 112 reviewed PNGs: 100 concept images plus 12 chapter-introduction/index images, using the approved APEX style. All PNGs are native 1672 × 941, approximately 16:9. The [six original pilots](assets/pilot/README.md) are preserved and reused. Images contain flattened text and artwork; editable PowerPoint composition remains a separate step.

## Use the images locally

Clone or pull this repository to your local project folder. The complete image library is in `assets/chapters/`, organized from `ch01` through `ch12`. Open `assets/chapters/gallery.html` in your browser to browse and search, or insert the PNGs directly into PowerPoint. Each chapter begins with `00-chapter-index.png`.

ZIP bundles are generated locally and excluded from Git to avoid duplicating the images and exceeding GitHub's per-file size limit. To create the full collection and individual chapter ZIPs, run:

```bash
python production/assemble_library.py --require-complete --package
```

The script uses the Python standard library and writes the archives to `deliverables/`. See [packaging instructions](deliverables/README.md).

## Audience and learning approach

The primary audience is professionals who want to use AI at work. The journey also serves advanced technical practitioners who want to deepen their understanding, improve judgment, and develop leadership skills, as well as business leaders and aspiring founders.

- Start with plain language that assumes no prior AI knowledge.
- Use familiar situations such as cooking, driving, shopping, and organizing everyday tasks to make concepts relatable across professions.
- Follow an everyday analogy with a real workplace application; clearly identify where the analogy stops being accurate.
- Keep slides simple without sounding childish. Put technical depth, qualifications, sources, and teaching prompts in speaker notes or optional follow-up slides.
- Inspire through useful possibilities and demonstrated examples, without unsupported claims or promises of income.

The intended progression is understanding → application → building and evaluation → business and leadership judgment.

## Program journey

**AI Agent Master Class → Three-day Agentic Sprint → Agentic Accelerator → Agentic Founder**

There are three principal branded programs in this visual project, with the Sprint acting as the bridge between the Master Class and Accelerator. Delivery is online. The APEX brief specifies a Sunday rhythm for Accelerator; detailed scheduling questions are recorded below.

| Offering | Current brief | Progression |
| --- | --- | --- |
| AI Agent Master Class | Entry experience for professionals and business leaders, including CEOs; introduce and help participants create an agentic workflow using the relevant tool from Claude, ChatGPT, and OpenBot. | Invite participants into the three-day Agentic Sprint. |
| Three-day Agentic Sprint | Hands-on experience targeting three to five comprehensive workflows over three days, drawing on Claude, ChatGPT, and OpenBot. | Invite participants into Agentic Accelerator. |
| Agentic Accelerator | V3 APEX: continuous, hands-on AI learning across three skill tracks, five session formats, and multiple tool ecosystems. Members learn concepts, create reusable capabilities, and build functional workflows. Membership duration needs reconciliation with the earlier six-month mentorship description. | Develop practical AI fluency and build and deploy useful projects; progress to Founder for deeper monetization and business operation. |
| Agentic Founder | Most premium of the three principal programs in this project; community-based, focused on monetizing skills and knowledge and using agents to run business functions, including company websites, lead generation, and marketing. | Build and deploy agent-supported business workflows; detailed support, membership structure, and completion criteria remain to be designed. |

**Tool scope:** The initial Master Class and Sprint brief names Claude, ChatGPT, and OpenBot. The Accelerator APEX brief expands the stack to Claude, ChatGPT, Google, and additional workshop and Learning Circle tools, detailed below. Select appropriate tools per demonstration and verify current product names, availability, and capabilities before writing tool-specific instructions.

**Program planning direction:** Accelerator spans professional functions, technical depth, reusable AI capabilities, and project execution. Customer and sales workflows are examples within that broader scope. Founder emphasizes monetization and running business functions with agents. The supplied APEX brief supersedes the earlier interpretation that Accelerator primarily focuses on customer development and sales.

Educational slides must provide a complete learning takeaway. Use natural next-concept links and relevant program invitations at teaching milestones; avoid making every concept a sales slide.

## Agentic Accelerator V3 APEX context

Source: [user-supplied 16-slide APEX brief](references/agentic-accelerator-v3-apex-source.txt), received 7 November 2026. Preserve this as source material; the following is a planning synthesis, not independent verification of its marketing or product claims.

### Positioning and membership ladder

The source describes a November 2026 launch of V3 APEX, renamed from AI Agent Accelerator to Agentic Accelerator. Its stated ambition is “The standard for hands-on AI education,” with an ongoing learning community. The source's 2027 market-leadership and US-meetup statements are aspirations, not established outcomes.

The wider DSM offer ladder in the brief is:

| Level | Offering | Source-listed price |
| --- | --- | --- |
| Free | Masterclass | Free |
| L1 | Workshops, including the monthly three-day Agentic Sprint | $99; additional workshops listed at $9–$49 |
| L2 | Agentic Accelerator | $997 |
| L3 | Agentic Founder | $2,997 |
| L4 | 1:1 Mentoring or Corporate Training | $4,997+ |

These are source-listed dollar prices, not newly verified commercial terms. Keep prices, event dates, and referral terms in offer-specific material rather than evergreen concept visuals. The wider ladder adds context without expanding the three-program visual scope.

### Three learning tracks

| Track | Topics and applications named in the brief | Implication for the concept library |
| --- | --- | --- |
| AI Concepts | Advanced prompting, RAG agents, data agents, MCP servers, agent loops, agent harnesses, memory state, multi-agent systems, guardrails, and evaluations | Explain the underlying ideas in prerequisite order; retain technical qualifications in notes. |
| Create Leverage | ChatGPT Plugins, Claude Projects, and Claude Skills | Teach reusable instructions, context, extensions, and capabilities; verify vendor terminology before demonstrations. |
| Functional Workflows | HR and recruitment, finance, project management, operations, IT and engineering, leadership, and entrepreneurship | Pair familiar analogies with applications across professions rather than concentrating examples in sales. |

The same tracks support recorded courses and monthly challenges. The source also names Microsoft Copilot and Cowork in the recorded library. These tracks are tags over the single 100-concept journey, not three additional catalogs.

### Five session formats

| Format | Purpose | Source cadence | Leads named in the brief |
| --- | --- | --- | --- |
| Flow Circle | Build together through hands-on work | Twice monthly | Arpan and Kunaal |
| Learning Circle | Teaching with a clear learning path | Once monthly | Kunaal |
| Workshops | Focused specialist deep dives | Every six weeks | Topic-specific coaches |
| Execution Block | Join a team, choose a project, and ship; no teaching or hands-on demonstration | Monthly, subject to schedule clarification | Sunil and Zuber |
| Open Session | Exploration and questions | Monthly, subject to schedule clarification | Arpan and Kunaal |

The proposed Sunday sequence is W1 Flow Circle, W2 Learning Circle, W3 Flow Circle, and W4 Open Session **or** Execution Block. The source also lists both of the latter formats as monthly; their alternation or additional scheduling needs clarification, as does fifth-Sunday handling.

The source's anchor time is **8:00 PM IST (Asia/Kolkata)**. This is 9:30 AM US Eastern during standard time and 10:30 AM during daylight time; use date-aware conversions for invitations rather than a year-round EST label.

Specialist workshops: Super Agents (Arpan), Claude Essentials (Sunil), n8n Basic to Advanced (Zuber), Image/Audio/Video (Ankur), AI Cashflow (Raj), and Lead Gen (Shalini). Together with Kunaal, the source names seven coaches. This instructional roster does not change the visual author attribution: **Kunaal Naik & Arpan Saxena**.

### Tool ecosystems and practical outputs

The APEX source names these ecosystems and tools; names are recorded as supplied and require verification for production lessons:

- **Claude:** Cowork and Code.
- **ChatGPT:** Work and Codex.
- **Google:** Gemini, AI Studio, and Antigravity.
- **Additional Learning Circle tools:** Copilot Studio, Copilot Cowork, and OpenBot / MausBot.
- **Specialist workshops:** n8n and media-generation workflows, among other topics.

Flow Circle outputs include documents, data work, artifacts, dashboards, presentations, personal branding, and built-and-deployed web and mobile apps. Proposed learning evidence should include an explained concept, a working artifact, and an evaluation of its usefulness and limitations; these are curriculum recommendations, not existing graduation requirements.

### Implications for the 100-concept project

- Keep a stable conceptual sequence while maintaining replaceable tool demonstrations. The brief describes rapidly changing tools and problems with rigid learning pathways.
- Support different entry levels with prerequisite links, short recaps, and optional advanced notes.
- Tag each concept by learning track, relevant functions, prerequisites, and suitable session format.
- Use Learning Circle visuals for explanation, Flow Circle visuals to introduce a build, and challenge prompts to support independent execution. Execution Blocks should not become teaching sessions.
- Use workplace examples across the named functions and include both beginner and advanced applications.
- Keep launch messaging, referral incentives, and the V4 ZENITH → V5 NEXUS → V6 INFINITY roadmap separate from evergreen educational content. The roadmap is a source-stated future direction.

## 100-concept curriculum

The approved outline refines the earlier provisional allocation into twelve chapters. The [full plan](production/100-image-plan.md) records each concept, teaching point, and visual direction. Each chapter has its own introduction/index image explaining why it matters. There is no extra all-100 overview or timed slide.

| Chapter | Focus | Concept IDs | Count |
| --- | --- | --- | ---: |
| 01 | Understanding AI | 001–008 | 8 |
| 02 | Understanding data | 009–016 | 8 |
| 03 | How machines learn | 017–024 | 8 |
| 04 | Generative AI and prompting | 025–034 | 10 |
| 05 | Context, knowledge, and memory | 035–042 | 8 |
| 06 | Technology building blocks | 043–050 | 8 |
| 07 | Reusable capabilities and workflows | 051–058 | 8 |
| 08 | Agents and agentic systems | 059–068 | 10 |
| 09 | Quality, safety, and reliability | 069–076 | 8 |
| 10 | AI across workplace functions | 077–084 | 8 |
| 11 | Business value and monetization | 085–092 | 8 |
| 12 | Leadership, mindset, and future skills | 093–100 | 8 |
| **Total** | | **001–100** | **100** |

One canonical record per concept is maintained in [curriculum.json](production/curriculum.json). Concepts can support multiple programs without increasing the count. Tool-specific demonstrations should remain replaceable as products evolve.

## Research specification

For every concept, capture:

1. Stable concept ID, term, plain-language definition, and a single learning outcome.
2. Prerequisites, sequence rationale, and the next related concept.
3. Everyday analogy, its limitations, and a practical workplace example.
4. Common misconception and any important technical or business qualification.
5. Suggested program placement and optional advanced teaching notes.
6. One visual explanation, a concise headline, and an image-generation brief.
7. A short understanding check or application prompt.
8. Credible sources, claim-to-source references, and a review date.

Prefer primary documentation, original research, and reliable educational sources. Separate established concepts from vendor-specific behavior and future predictions. Label hypothetical examples, and never present invented metrics as measured results.

## Visual and communication system

Use the supplied **Simple Explainer Slides** guidance: Apple-inspired clarity and restraint, very plain language, friendly imagery, and polished execution. This does not imply affiliation with Apple.

### Canvas, palette, and typography

- Use 16:9 layouts; target 1920 × 1080 for exported visuals.
- Base colors: deep navy `#041B36` or near-black `#020B18`, with white text `#F7F8FC`.
- Use limited yellow emphasis `#FFE844` and restrained cyan accents `#00D7F5`.
- Treat these colors as the supplied starting palette, not verified corporate brand specifications.
- Use a clean sans-serif font such as Inter, Arial, or Aptos, with large readable type, strong contrast, generous whitespace, and consistent alignment.
- For **Agentic Accelerator V3 APEX**, use the supplied program-specific direction: dark navy, amber `#F2A541`, teal secondary `#5EC4B6`, Space Grotesk headings, and Inter body text. This overrides the general yellow/cyan defaults for Accelerator while retaining the shared minimal layout and teaching style.
- Distinguish programs with explicit labels. Master Class and Founder accent treatments remain to be selected; the earlier cyan/violet/gold proposal is not an approved system.

### Slide composition

- Give each slide one main idea and a short heading that states the point.
- Include one supporting sentence only when useful; move detail into notes or additional slides.
- Prefer plain language and one useful illustration. Use a diagram only when it clarifies a relationship and a chart only when it communicates evidence.
- When useful, include one consistent friendly person, a small rounded white-and-cyan robot, or a familiar object. Not every slide needs a character.
- Use subtle lighting and polished imagery. Avoid decorative clutter, crowded panels, excessive glow, unnecessary arrows, and bulky repeated footers.
- Use comparisons, familiar examples, questions, or clear next steps as appropriate to the concept rather than forcing every slide into one layout.

### Branding

Every standalone concept visual must include **Data Science Masterminds**, its relevant **program name**, and **Kunaal Naik & Arpan Saxena**. Use a single discreet, consistently placed attribution area so the teaching remains dominant. Full title and section slides may carry more prominent branding.

Treat the Sprint as part of the Master Class-to-Accelerator transition until its own branding is defined. Never distinguish programs through color alone.

### Production recommendation

Generate the illustration separately, then compose headlines, explanations, and branding as editable PowerPoint text. Export the complete composition as a PNG. This supports consistent spelling, typography, and layout while retaining editable teaching assets.

Maintain a reusable character reference and template system before scaling production. Each concept should have one primary visual; optional supporting slides do not increase the concept count.

## Deliverables and execution plan

| Phase | Deliverable | Completion criterion |
| --- | --- | --- |
| 1. Project brief | This README and a record of remaining decisions | Confirmed requirements are separated from proposals and unknowns. |
| 2. Research | Source-backed catalog of 100 sequenced concepts | Distinct concepts, verified explanations, prerequisites, and source references. |
| 3. Program planning | Plans for the three programs and bridging Sprint | Learning outcomes, concept mapping, exercises, delivery structure, and transition milestones. |
| 4. Design system | Templates, typography, palette, character treatment, attribution, and generation guidance | A consistent system that supports different explanation types. |
| 5. Pilot | Six concept visuals, two per principal program, with notes | Review clarity, factual accuracy, projected readability, and consistency before scaling. |
| 6. Production | 100 primary 16:9 concept visuals and editable compositions | Every visual meets the content and design checks below. |
| 7. Presentation delivery | Master PowerPoint deck and program-specific decks | Correct sequence, editable text, speaker notes, sources, and clean exports. |

Proposed file organization for later phases: `research/` for the catalog and sources, `programs/` for program plans, `design/` for style references and templates, `assets/` for illustrations, and `presentations/` for decks and exports.

## Quality checks

- A beginner can describe the main point after seeing the visual.
- An advanced practitioner can find accurate supporting detail and limitations in the notes.
- Each slide has one clear takeaway, readable wording, sufficient space, and only useful visual elements.
- Everyday analogies are recognizable, labeled, and bounded by accurate explanations.
- Factual claims and numbers have supporting sources; hypothetical examples are marked.
- Names, program labels, layout, and character appearance stay consistent.
- Slides remain readable when projected, and program identity does not depend on color perception.
- PowerPoint files open correctly, preserve editable text, and export without clipping or missing assets.
- Research and design review are recorded separately from actual learner feedback; do not claim audience validation before it happens.

## Open decisions

1. Verify the precise products and editions named in the APEX stack, including OpenBot / MausBot, before preparing tool-specific demonstrations.
2. Reconcile the earlier six-month mentorship description with APEX's continuous community and its account of one-time-fee members staying from several months to over a year. Define membership access and support duration without assuming lifetime access.
3. Resolve the monthly Open Session / Execution Block scheduling overlap and fifth-Sunday handling.
4. Define measurable completion criteria across Accelerator's three skill tracks and Founder's monetization and business-operations focus; specify Founder's support and membership structure.
5. Select Master Class and Founder accent treatments during the pilot; use the supplied amber/teal direction for Accelerator APEX.
6. Incorporate any official logo assets and the referenced `references/style-guide.txt` if they become available. Neither was present in the project when this brief was written; the supplied inline style guidance is sufficient for initial planning.
7. Define any later Excel or task-testing workstream separately; it is not part of the initial visual-library deliverable.

## AI income opportunity research

Explore the [100 AI Income Opportunities project](research/100-ai-income-opportunities/README.md). Start with the [master decision index](research/100-ai-income-opportunities/MASTER-INDEX.md), choose an industry in the [chapter index](research/100-ai-income-opportunities/CHAPTER-INDEX.md), then assess a specific offer and its validation test.

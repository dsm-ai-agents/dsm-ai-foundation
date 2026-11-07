import json
from pathlib import Path
chapters=[
('Understanding AI',1,8,'Recognize what AI can do, where it helps, and why human judgment still matters.'),
('Understanding data',9,16,'Understand the information behind AI so you can spot weak inputs and misleading conclusions.'),
('How machines learn',17,24,'Understand learning and testing so you can distinguish genuine improvement from memorization.'),
('Generative AI and prompting',25,34,'Understand generation and give clear instructions that produce useful, checkable results.'),
('Context, knowledge, and memory',35,42,'Give AI the right information at the right time instead of relying on longer prompts alone.'),
('Technology building blocks',43,50,'Understand how AI connects to software and becomes a working application.'),
('Reusable capabilities and workflows',51,58,'Turn one-off tasks into repeatable processes and reusable capabilities.'),
('Agents and agentic systems',59,68,'Understand how agents select actions, use tools, and coordinate within boundaries.'),
('Quality, safety, and reliability',69,76,'Test and monitor systems before trusting them with consequential work.'),
('AI across workplace functions',77,84,'Recognize useful AI patterns across professions and connect learning to real work.'),
('Business value and monetization',85,92,'Connect technical capability to customer problems, delivery costs, and clear offers.'),
('Leadership, mindset, and future skills',93,100,'Lead adoption with judgment, accountability, and skills that transfer as tools change.')]
raw='''Artificial intelligence|Software can recognize patterns, predict outcomes, and generate content.|Three familiar objects: photo, weather forecast, draft letter.
Machine learning|Learn patterns from examples instead of writing every rule.|Fruit sorter learning from labeled examples.
Generative AI|Create new content using learned patterns and supplied instructions.|One brief becoming text, image, and audio waveform.
Model versus application|The model is one component of a usable product.|Engine beside complete car; reuse pilot 004.
Prediction versus generation|Estimating an outcome differs from creating content.|Forecast demand versus draft tomorrow's menu.
Multimodal AI|Work with different types of information together.|Photo, voice note, and written question in one workspace.
Hallucination|A convincing answer can still be wrong or unsupported.|Polished answer with one unsupported claim highlighted for checking.
Human augmentation|Decide what AI handles and what a person judges.|Navigation assistant suggests route; human drives.
Structured and unstructured data|Information comes in organized fields and freer forms.|Spreadsheet beside emails, photographs, recordings.
Data quality|Missing, stale, or incorrect inputs weaken results.|Recipe with missing quantity and expired ingredient.
Features and labels|Features describe examples; labels provide known answers.|Fruit card with size and color beside fruit name.
Sampling bias|A narrow sample can give a misleading picture.|Inspecting only the top layer of a varied fruit basket.
Privacy and consent|Having access does not mean every use is permitted.|Personal file with clear purpose and permission boundaries.
Probability and uncertainty|Likelihood is different from certainty.|Forecast with several possible outcomes; no unsupported percentages.
Correlation versus causation|Moving together does not prove one thing causes another.|Hot weather influences both ice-cream sales and swimming.
Data visualization|Choose a view that answers a specific question.|Small illustrative table beside clear matching chart.
Supervised learning|Learn from examples paired with known answers.|Practice cards paired with answers.
Unsupervised learning|Find groups or patterns without supplied answer labels.|Unlabeled objects arranged into similar groups.
Reinforcement learning|Learn behavior from actions and reward signals.|Simple maze with feedback along attempted routes.
Neural networks and deep learning|Layers of learned transformations build useful representations.|Image through a few clearly simplified processing layers; no biological brain claim.
Training versus inference|Training updates the model; inference uses it.|Cooking practice versus serving a dish; reuse pilot 021.
Training, validation, and test sets|Practice, tune, then assess on held-out examples.|Three separate stacks: practice, validation, test.
Overfitting|Memorizing examples can fail on unfamiliar cases.|Learner masters one exact route but struggles at detour.
Fine-tuning|Additional training adapts model behavior for a task.|Generally trained cook receiving specialist pastry training.
Large language models|Language models generate text by modeling token sequences.|Sentence extending a small piece at a time.
Tokens|Text is processed in pieces that are not always whole words.|Short sentence divided into illustrative variable-sized tiles; label illustrative tokenization.
Context window|Each interaction has a bounded working space.|Desk with limited room for relevant pages.
Attention|Weight relationships between parts of the input.|Pronoun linked to the words that clarify it; no human attention claim.
Diffusion|A diffusion process gradually transforms noise into an image.|Noise, emerging structure, finished object; avoid claiming all image models work this way.
A clear prompt|Specify the task, context, constraints, and desired result.|Precise restaurant order versus ambiguous request.
Few-shot prompting|Examples demonstrate the pattern you want.|Two completed examples followed by new matching task.
Output contracts|Define the answer's shape before using it downstream.|Free-form text beside a clearly labeled output template.
Task decomposition|Break a complex request into manageable parts.|Shopping, preparation, cooking as three meal-planning steps.
Verification|Check claims and results against evidence or tests.|Draft checked against source, calculation, and requirements.
Context engineering|Select information needed for the next step.|Chef's station with only relevant recipe, ingredients, and tools.
Grounding|Connect an answer to supplied evidence.|Answer statements connected to highlighted source passages.
Embeddings|Represent items numerically to compare useful similarities.|Illustrative semantic map with related phrases near each other.
Semantic search|Search by meaning, beyond exact word overlap.|Vehicle repair query finds Fixing your car document.
Chunking|Split material into useful retrieval units.|Manual divided at meaningful section boundaries.
Retrieval-augmented generation (RAG)|Retrieve evidence, add context, then generate.|Three-stage process; reuse pilot 040.
Persistent memory|Store selected information for later interactions.|Temporary desk beside durable notebook; no automatic model retraining.
RAG versus fine-tuning|Supplying reference material differs from changing model parameters.|Open reference book beside specialist training.
APIs|Software interacts through defined interfaces.|Service counter exchanging request and result.
JSON and schemas|Structured fields support reliable exchange and validation.|Delivery label with required name, address, and item fields.
Databases and queries|Store records and retrieve what you need.|Organized cabinet with precise lookup request.
Webhooks|An event can notify another system automatically.|Doorbell signals arrival rather than repeated door checks.
Authentication and authorization|Identity and permission answer different questions.|Identity badge beside door-access list.
Frontend and backend|Visible interface and underlying processing work together.|Restaurant dining room and kitchen.
Version control|Track changes and recover earlier versions.|Document timeline with named checkpoints.
Deployment|Make a tested application available in its intended environment.|Prototype becomes a maintained service.
Workflow mapping|Make inputs, steps, decisions, and outputs explicit.|Simple order-to-delivery process.
Triggers and conditions|Define when work starts and which rules apply.|Incoming request at one clear decision gate.
Prompt chaining|One step supplies input to the next.|Research, outline, draft as three stations.
Routing|Send a task to an appropriate path.|Reception desk directs requests to specialists.
Parallel execution|Independent tasks can run simultaneously.|Cooks preparing separate dishes at once.
Reusable templates|Parameterize recurring instructions rather than rewrite them.|Report template filled with different client details.
Agent skills|Package instructions, resources, and scripts for recurring work.|Task kit containing guide, tools, and examples.
Project workspaces|Keep relevant instructions and reference material together.|Separate project folders with their own materials.
AI agents|Select actions toward a goal within defined boundaries.|Fixed recipe versus cook adapting next step to conditions.
Agent loop|Use results to decide whether to continue or stop.|Observe, decide, act loop with exit; reuse pilot 060.
Planning and replanning|Revise steps when conditions change.|Route updated after road closure.
Tool calling|A model requests an action that software executes.|Assistant selecting calculator, search, or calendar.
Agent harness|Surrounding software manages execution, tools, and limits.|Model inside a labeled operating frame; scope varies by implementation.
State and checkpoints|Track progress so work can resume or recover.|Task board with saved checkpoint.
Multi-agent orchestration|Divide work when benefits justify coordination costs.|Coordinator assigning distinct roles to small team.
Model Context Protocol (MCP)|Standardize connections to tools and context.|Host with client connections to capability-providing servers; not automatic security.
Agent-to-agent communication|Exchange tasks and results across agent systems.|Service desks exchanging task ticket and deliverable.
Computer-use agents|Interact with software through its interface.|Agent uses browser within action boundaries and checkpoints.
Evaluations|Test representative tasks against explicit success criteria.|Driving test under several conditions, not one easy road.
Precision and recall|False alarms and missed cases are different errors.|Sorting tray shows correct selections, wrong selections, and missed items; formulas only if accurate.
RAG evaluation|Assess retrieval and answer support separately.|Found the right passage? versus Used it correctly?
Guardrails|Checks constrain behavior but do not guarantee safety or correctness.|Multiple inspection points around workflow.
Prompt injection|Untrusted content may attempt to redirect the system.|Retrieved document with a suspicious instruction clearly distinguished from user task.
Least privilege and human approval|Grant necessary access and review consequential actions.|Restricted keyring beside human approval gate.
Tracing and observability|Record events so failures can be investigated.|Task timeline of model calls and tools with failed step.
Quality, latency, and cost|Evaluate tradeoffs against the task's needs.|Three labeled controls and task-specific target; no invented benchmarks.
Document workflows|Transform source material into a reviewable deliverable.|Meeting notes become structured brief with sources.
Data-analysis workflows|Move from question to checked calculation and explanation.|Question, small spreadsheet, verified result.
Decision dashboards|Connect measures to actions people can take.|One clear indicator linked to one decision; illustrative data.
Multimedia production workflows|Coordinate brief, assets, editing, and review.|One brief becomes coordinated image, audio, video set.
HR and recruitment support|Assist administration while preserving human hiring decisions.|Scheduling and document preparation around human-led process.
Finance exception handling|Flag discrepancies for investigation.|Invoices through matching checks with one flagged discrepancy.
Operations and project coordination|Route work, track dependencies, and escalate blockers.|Task board with one visible bottleneck.
AI-assisted software delivery|Build from requirements through testing and deployment.|Company website through four checked stages.
Customer discovery|Understand the problem before choosing technology.|Founder listens to customer before opening toolbox.
Use-case prioritization|Compare expected value, feasibility, and risk.|Three candidate tasks on simple qualitative scorecard.
Minimum viable product|Test an outcome with the smallest credible solution.|One working service counter before full store.
Value proposition|Explain customer outcomes rather than just AI features.|Feature-heavy description becomes clear benefit.
Lead-generation workflows|Research prospects and prepare relevant, reviewable outreach.|Research, qualification, draft, human review.
Sales and CRM workflows|Maintain continuity from inquiry to follow-up.|Customer record moving through meaningful stages.
Unit economics|Revenue less variable costs gives contribution, not net profit.|Illustrative $100 minus $40 equals $60 before fixed costs and taxes; reuse pilot 091.
Productized services|Package a repeatable outcome with defined scope.|Loose skills become a clear service offering.
Systems thinking|Improving one step may not improve the whole process.|Fast workstation feeding a slower bottleneck.
Critical judgment|Question assumptions and seek evidence.|Decision card with evidence, assumptions, uncertainties.
Effective delegation|Specify outcomes, boundaries, and review points.|Clear task brief; reuse pilot 095.
Change management|Adoption needs redesigned work, training, and support.|Team moves from old process to supported new process.
Accountability and governance|Assign owners for decisions, access, and failures.|Workflow with visible human owners.
Feedback loops|Use measured results to decide what to improve.|Build, measure, review, revise loop.
Learning agility|Practice skills that transfer as tools change.|Stable foundation supporting replaceable tools.
Future readiness|Prepare for plausible scenarios rather than certain forecasts.|Several possible paths supported by data, judgment, and communication.'''
rows=[l.split('|') for l in raw.splitlines()]
assert len(rows)==100,len(rows)
result=[]
for n,(title,start,end,why) in enumerate(chapters,1):
 result.append(dict(chapter=n,title=title,start=start,end=end,why=why,concepts=[dict(id=i,title=rows[i-1][0],point=rows[i-1][1],visual=rows[i-1][2]) for i in range(start,end+1)]))
p=Path(__file__).parent/'curriculum.json'
p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('Saved',len(result),'chapters and',sum(len(c['concepts']) for c in result),'concepts')

---
name: reverse-vc-scaling
description: "Coordinate evidence-grounded reviews of AI-native B2B and enterprise fundraising packages, defaulting to Seed and Series A. Use for full or multi-domain reverse diligence, recursive material improvement, cross-document consistency, IC bear cases, rehearsal and model-review packets. Adapt proof and priorities to the business, target market and proposed raise; route focused tests to standalone specialists when available."
---

# Reverse VC Scaling

Help a VC and portfolio company build the strongest investment case the evidence supports. Work backward from the questions the target investor will ask at the company's actual stage, test the materials they will receive, improve them, and test again. Success means accurate understanding, credible upside, and clear treatment of uncertainty; it does not require a favorable investment verdict.

## Company and fundraising lens

Default to AI-native B2B and enterprise businesses at Seed or Series A. Read [company-calibration.md](references/company-calibration.md) first, or reuse an established source-backed context: product/workflow, market and buyer, business model, actual maturity and proposed current raise. Apply only relevant tests and follow an explicit user scope override.

When the fundraising amount, timing or use of proceeds changes this review, read [raise-calibration.md](references/raise-calibration.md). Connect capital to the specific proof and operating milestones it buys; distinguish requested primary capital, secondary, secured funds and existing cash. If the amount is missing, continue the domain work and request it only when needed for the capital conclusion. A larger raise does not itself establish maturity, and a narrow test does not require a full financing audit.

State the applied business/stage lens and any material effect of the raise on the result. Keep current evidence, capital-plan feasibility and investor fit distinct; share definitions and source IDs across reviews.

## Scope and defaults

- Treat a request to strengthen, prepare, or recursively test materials as permission to create revised local drafts as well as a review. For an audit-only request, deliver findings and proposed changes without editing source artifacts.
- Adapt to the actual stage, business model, buyer, sector, geography, and investor mandate. For Seed and Series A, read [early-stage-gates.md](references/early-stage-gates.md). If stage is unknown and materially changes the evidence standard, ask or state a provisional lens rather than silently imposing growth-stage requirements. Do not impose SaaS metrics on every AI business.
- Use only the supplied company materials and authorized sources. Keep each company's evidence and outputs separate.
- Start with available materials. Ask only for missing inputs that change the interpretation or next action; continue independent work. No materials means a tailored intake and review plan, not a scored company review.
- Preserve originals and version revised drafts. Publishing, sending to investors, or uploading confidential files to a new external service is separate from local preparation; honor existing authorization without asking again.
- This workflow is self-contained. Use available document, spreadsheet, presentation, or research capabilities for the formats involved; do not require another named skill or a particular model vendor.

## Choose the mode and modules

Keep one shared company context, claim ledger, metric dictionary, and objection history. Nine standalone specialist skills provide direct entry points for focused reviews; this coordinator combines their evidence and checks cross-domain consistency. Their names and self-contained fallback modules are listed in [module-router.md](references/module-router.md).

For a full business assessment, establish the strength of the customer problem and the venture-scale path before synthesizing the detailed domain review. [early-stage-gates.md](references/early-stage-gates.md) connects the standalone `customer-problem-stress-test` and `venture-scale-assessment` skills when available and gives a self-contained fallback. Reuse existing evidence and completed work; a focused artifact task need not trigger both full assessments.

- **Artifact review:** review supplied files, produce supported revisions, and retest. This remains the default for a preparation request without a request for live rehearsal.
- **Founder interrogation:** read [challenge-loop.md](references/challenge-loop.md); ask one question at a time and wait for the founder's actual answer. Do not simulate their answers or finish the interview on their behalf.
- **Focused business test:** read [module-router.md](references/module-router.md), use the matching standalone skill through the environment's skill mechanism when available, or use its local fallback module. Run only the requested tests and material dependencies. Do not rerun both implementations or require other skills to be installed. A technical test plan is not an executed product evaluation.
- **IC challenge:** synthesize the evidence-backed bear case from completed work, then adjudicate it against the supported positive thesis. Record unreviewed domains rather than invent a complete diligence history.
- **Investor meeting preparation or debrief:** read [meeting-learning.md](references/meeting-learning.md). Use observations from real meetings to reopen specific objections and update the evidence, not to infer investor intent from demeanor.

For a full review, screen all nine modules and deepen the decision-critical ones. Mark each as reviewed, partly reviewed, not assessed, or not applicable with a reason. Load only relevant module files. Do not require every module or a rigid question count for a narrow request. [challenge-loop.md](references/challenge-loop.md) defines the shared test contract, resolution states, and cross-module checks.

The numbered workflow below is the default for preparing and revising an artifact package. Apply only its relevant steps to a focused audit, interview, meeting task, or IC challenge; do not force a baseline/rewrite/retest cycle when the user requested a single analysis pass. Still disclose actual coverage, evidence gaps, and reviewer limitations.

## 1. Establish the business and review contract

Read [business-context.md](references/business-context.md). Produce a short context brief from sources: product and workflow, buyer and user, pricing and revenue recognition basis, AI architecture, stage, traction periods, geography, round and use of funds, and the target investor's requirements. Distinguish documented facts from management assertions and assumptions. Avoid importing knowledge from unrelated portfolio companies.

Define the investor lens: stage, check/ownership range if known, sector thesis, geography, return expectations, and tolerance for technical, capital, or regulatory risk. If the investor is unspecified, use a generic investor appropriate to the company's stated or provisionally inferred stage and label that assumption; do not invent a named firm's mandate.

Agree through context, or state provisionally, which package is being tested: one artifact, a first-meeting deck, or a full diligence room. Missing full-room materials should not automatically fail a first-meeting deck. Record review date, currency, periods, materiality, and accessible tools. Use scenario ranges supplied by the company; label any reviewer-selected shocks as illustrative.

## 2. Freeze the baseline and establish traceability

Inventory source ID, filename or URL, version/date, intended audience, and access/extraction status. Note missing tabs, formulas, notes, images, appendices, linked workbooks, or inaccessible documents. A text extraction is not proof of complete inspection.

Build a claim ledger for decision-relevant statements. For each: exact claim; location; source and pinpoint locator; metric definition/period/units; evidence status; and investment implication. Use `supported`, `partially supported`, `unsupported`, `contradicted`, or `not inspectable`. An assertion repeated in several decks remains one assertion, not independent verification.

Separate actuals, annualized run rates, signed commitments, bookings, pipeline, forecasts, and scenarios. Label computations with inputs and formulas. A spreadsheet cell supports what the model says; it does not authenticate the underlying commercial fact. Do not silently choose among conflicting documents.

Freeze the baseline artifacts, rubric, and reviewer prompts before editing. For cross-model tests, also record the exact supplied package, model/tool identity when exposed, and web access. Read [review-protocol.md](references/review-protocol.md) for the run record and evaluation design.

## 3. Test understanding before persuasion

Read [reviewer-prompts.md](references/reviewer-prompts.md). Use a neutral cold-read prompt with only the intended investor package and investor mandate. Do not include the internal context brief, desired verdict, change log, or coaching conversation.

Ask the reviewer to reconstruct who pays, what they buy, why AI matters, how money is made, what is proven, what remains projected, why the company could win, and what the round enables. Compare the reconstruction with sourced company context. Missing or wrong answers become specific comprehension defects, not an excuse to give the cold reviewer private context.

If an authorized fresh session or reviewer is available, use it. Otherwise label the exercise a same-context simulation; it cannot demonstrate a blind review. A role prompt does not turn the current model into Claude or provide independent model validation.

## 4. Run investor diligence

Use [module-router.md](references/module-router.md) to route product/technology, market, competition/defensibility, GTM strategy/commercial repeatability, business model/AI economics, scalability, financial model/capital, category/timing, and team/governance. Read the applicable sections of [diligence-tests.md](references/diligence-tests.md) for shared calculation and source-inspection rules. Test four connected layers:

1. **Business:** customer value, repeatable demand, growth quality, retention, competition, defensibility, and team execution.
2. **Economics:** revenue definitions, model integrity, AI delivery costs, contribution economics, cash needs, and sensitivity to plausible downside.
3. **Scaling:** product reliability, quality at volume, implementation and support capacity, distribution, dependencies, and capital required to reach the next milestone.
4. **Investment:** reachable market, why now, credible expansion, round-to-milestone logic, and return feasibility where terms are available.

Write the strongest supported positive thesis alongside the strongest credible reasons to decline or defer. Give each objection a source, severity, confidence, consequence, and what would resolve it. Test both flattering and skeptical claims; skepticism is not evidence either.

For material claims, state what evidence would disprove them and the smallest useful test that could distinguish the alternatives. Set test population, conditions, metric, acceptance criterion, and decision consequence before interpreting a result. When thresholds are not established, propose a justified criterion and label it provisional; do not let model satisfaction determine passage. Keep question-led interrogation distinct from analytical evidence assessment.

Use current primary sources for time-sensitive market, competitor, model pricing, or benchmark claims. Preserve source date, population, definition, and limitations. [research-notes.md](references/research-notes.md) contains starting points, not a current benchmark database. Verify legal or regulatory claims against applicable authoritative sources when relevant; do not infer applicability from an industry label.

## 5. Repair what the evidence permits

Classify each material finding:

| Finding | Correct action |
| --- | --- |
| Reader cannot understand an otherwise supported claim | Clarify wording, definition, chart/table labels, or evidence placement |
| Sources or calculations disagree | Reconcile using authoritative records; preserve unresolved alternatives |
| Evidence exists but is buried or inaccessible | Add exact citations, a readable metric table, and an accessible supporting artifact |
| Claim exceeds available proof | Narrow or remove it, distinguish a forecast, or specify the evidence needed |
| Underlying business risk | Describe the risk, an owner-proposed mitigation, and a measurable test; do not call it solved through wording |

Create actual replacement passages, tables, assumptions notes, or revised artifact copies within the authorized scope. For formats that cannot be edited safely, supply exact location-specific replacements and mark the artifact as not yet edited. Do not merely return a generic checklist when revisions were requested.

Make the upside concrete: connect customer pain → measured value → willingness to pay → repeat usage → delivery economics → repeatable growth → reachable opportunity → capital milestone. Attach dependencies and counterevidence to this chain. Proposed hires, mitigation plans, and founder commitments remain proposals until confirmed.

Improve machine readability with selectable text, descriptive headings, explicit dates and units, labeled tables, defined acronyms, and resolvable evidence references. Check critical visual content and spreadsheet logic in their native form. Never insert hidden instructions, fabricated citations, keyword stuffing, or requests that an investor's AI praise the company or suppress risks.

## 6. Retest and stop for a reason

Default to a baseline plus up to two repair-and-retest cycles, unless the user specifies a different budget. After each repair, recheck affected metrics across every supplied artifact, then rerun the frozen neutral questions. Keep the fixed baseline questions and add a separate regression check for newly discovered defects.

Retain accumulated answers and objections during adversarial practice so later challenges can expose inconsistent assumptions. Before a final neutral test, isolate the intended investor materials from that practice history. This preserves the guide's continuity benefit without allowing a trained conversation to stand in for a fresh reader.

Where tools and authorization permit, use a fresh reviewer for the final package without exposing earlier scores, coaching, or revision rationale. For Claude/GPT/AI-search comparisons, follow [reviewer-prompts.md](references/reviewer-prompts.md). If a requested model is unavailable, prepare a runnable review packet and explicitly report that test as not run; continue the reviews available here.

Record gains and regressions with observable evidence: corrected reconstruction, reconciled arithmetic, resolved contradiction, stronger citation, or improved answer to a decision-relevant question. A more enthusiastic model response alone is not an improvement. Preserve disagreement across reviewers and adjudicate through sources rather than majority vote.

Stop when the scoped package passes integrity and comprehension checks and remaining risks are clearly disclosed; when the iteration budget is reached; or when the next material improvement requires new data, execution, a real customer test, or missing access. Never loop until a model agrees to invest.

## 7. Deliver the result

Use [review-protocol.md](references/review-protocol.md) for concise output structures. Scale detail to the task. Lead with the scoped readiness result and the evidence-based investment thesis, then provide:

- Revised artifacts or exact proposed replacements, with a short change log.
- The strongest supported reasons to pursue and the principal reasons to defer or decline.
- A claim/contradiction register and ranked unresolved items, each with the required proof, proposed owner, and next action.
- A metric dictionary and data-room evidence map where needed for interpretation.
- An investor Q&A: direct answer, source, caveat, and unanswered follow-up for each material objection.
- A before/after review record, test coverage, model availability, remaining limitations, and the next best evidence-producing action.
- For business stress tests, a module coverage map and prioritized test plan: hypothesis, failure condition, needed evidence, proposed owner, decision enabled, and downstream assumptions affected. For rehearsal, preserve the founder's answer separately from any suggested improved answer.

Keep **material quality**, **evidence completeness**, and **investment attractiveness** separate. A transparent package may describe a weak investment; an exciting business may still have an unreliable package. Readiness is scoped to the tested artifacts and investor use case, never a guarantee of fundraising or an investment decision on the user's behalf.

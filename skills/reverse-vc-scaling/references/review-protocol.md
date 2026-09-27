# Review protocol and output structures

Use these structures as working records, not mandatory bureaucracy. A one-document task can combine them into a short review and change table. Larger rooms benefit from separate files.

## Scope and coverage record

Record company, review date, investor lens, intended use, actual/forecast cutoff, currency, materiality, input versions, accessible artifacts, inaccessible content, and tests performed. Coverage means what was actually inspected, not the percentage of filenames listed. Report important untested work explicitly.

Suggested source row:

`S01 | filename/URL | version/as-of | scope | extraction/native inspection status | authoritative for | limitations`

Suggested claim row:

`C01 | claim and location | status | S01 + exact locator | period/units/definition | contrary evidence | consequence | action`

Suggested issue row:

`I01 | severity | business/comprehension/evidence/calculation/access | claim IDs | investor objection | source-backed finding | fix or proof needed | proposed owner | status`

Severity:

- **Critical:** likely to reverse the decision or materially mislead about the investment, including fabricated support or a major unexplained revenue discrepancy.
- **Major:** changes valuation, downside, scaling feasibility, or the next diligence step.
- **Minor:** creates avoidable friction without changing the economics or decision.

Confidence describes confidence in the finding, not the attractiveness of the company. Separate `not provided`, `not inspectable`, `contradicted`, and `not applicable`.

## Two independent assessments

**Package readiness:** `ready for scoped use`, `ready with stated limitations`, or `not ready`. Include scope and gates, never just a color.

Integrity and comprehension gates:

1. Decision-driving claims are correctly labeled and traceable; material contradictions are resolved or prominently disclosed with their implications.
2. The package distinguishes actuals, run rates, commitments and forecasts; critical arithmetic is verified to the extent access allows.
3. A cold reader can reconstruct the business and key caveats without privileged context, or the lack of a blind test is disclosed.
4. The evidence supplied is adequate for the stated use. For a full diligence pack, a decision-critical missing model/cohort/contract record prevents unconditional readiness; it may be acceptable for a first meeting with a clear follow-up request.
5. No known material issue is concealed by the revision, and the review identifies untested content.

**Investment assessment:** `pursue diligence`, `defer pending named evidence`, or `decline under the stated mandate`, as a simulated reviewer view. Support it with a positive thesis, principal objections, and evidence that would change the view. A disclosed weak metric can coexist with a well-prepared package.

For before/after tracking, assess each relevant dimension—comprehension, traceability, consistency, model integrity, AI economics, market, scalability, defensibility, and round logic—with evidence status and a concrete rationale. If a numeric score is requested, use a transparent ordinal rubric and call it a reviewer judgment; do not turn it into a probability of funding. Do not average away a critical defect.

## Controlled iterations

Keep the investor mandate, prompt, rubric, and source scope stable across paired baseline/revision tests. Log any added evidence or tool changes so the observed improvement can be attributed correctly. A new source improving the conclusion is different from a clearer presentation of the old evidence.

Iteration row:

`version | issues addressed | source changes | artifact changes | observed reader/calculation improvement | regressions | unresolved items | next step/stop reason`

Prioritize critical issues, then major decision drivers, then clarity. Preserve supported strengths while fixing weaknesses. Retest linked figures and claims across the package, including references affected by changed file names or numbering.

An unsupported factual statement becoming a well-labeled forecast is a presentation improvement, not new proof of the forecast. Removing a misleading number can lower apparent attractiveness while improving readiness. Do not remove counterevidence to raise a score.

Stop after the agreed budget (default: baseline plus two repair cycles), after scoped gates pass, or when the next improvement requires new evidence/access or business execution. Deliver usable completed revisions and a specific remaining evidence request even if full readiness is impossible.

## Model and tool run record

For each actual review, record:

- Run ID, date/time, provider/tool, exact model/version if exposed (otherwise `not exposed`).
- Actual independent session, same-context role simulation, or prepared-but-not-run prompt.
- Prompt version/text; investor mandate; artifact versions or hashes where available; file and context limits.
- Native files vs extracted text; whether formulas, images, and source links were available; truncation or omissions.
- Closed-book package review vs web-enabled research; search date and citations.
- Sampling settings when known; output path; failures; material disagreements and adjudication.

Retain returned answers and supporting calculations; do not request or claim access to a model's hidden reasoning. A changed model, incomplete upload, different extraction, or web access can confound comparisons. Report those differences rather than attributing everything to the materials.

## Deliverables

For a full engagement, a useful local structure is:

```
company-review/
  context-and-sources.md
  findings-and-claims.md
  revised/
  investor-qa.md
  review-runs/
  decision-and-next-actions.md
```

Create only files with substantive content. Keep private internal deliberations separate from investor-facing materials; do not silently distribute them together.

For a focused module or rehearsal, prefer one compact working record containing the test card, answers/objections, findings and next actions. Nine reviewed modules do not require nine separate reports. Use [module-router.md](module-router.md) for coverage and [challenge-loop.md](challenge-loop.md) for objection states and cross-domain reconciliation.

The decision note should answer: What does the company do? Why could it be attractive? What is actually proven? What would make this investor decline? What improved? What remains unresolved? Which tests ran? What should the company do next?

The investor Q&A should give a direct answer, quantitative basis where available, exact evidence location, caveat, and follow-up. An unknown needs a concrete data request, not a confident invented answer.

# VC skill suite

The suite has twelve independently installable skills: nine domain specialists, two foundational specialists, and one coordinator. Each specialist includes its own instructions, supporting tests, evidence rules and stage calibration. It can review one claim or a relevant part of a data room without the coordinator being installed.

All twelve now default to **AI-native B2B and enterprise companies at Seed and Series A**. Every skill carries its own company/market and fundraising calibration references. It adapts to the actual buyer, workflow, revenue model, sales/procurement/deployment cycle, cohort maturity and proposed raise. Other stages or business types remain available when explicitly requested.

The fundraising lens distinguishes the current primary raise from secondary proceeds, past fundraising, valuation, existing cash and an investor's check. It connects net available capital and close timing to specific proof milestones, hiring and operating capacity. Smaller/larger/delayed funding scenarios use the company's costs and plan rather than universal dollar brackets or runway rules.

## Pick the requested decision

| Skill / ZIP name | Use it for | Example request |
| --- | --- | --- |
| vc-gtm-stress-test | ICP, buyer/budget, positioning, channels, sales motion, pilot conversion, activation, retention and acquisition economics | Use VC GTM Stress Test to challenge whether our acquisition channels produce repeatable, retained paid customers. |
| vc-product-technology | Product outcomes, AI quality, evaluations, technical dependencies, deployability | Use VC Product and Technology to test our autonomous-completion claim and identify the missing production evidence. |
| vc-market-opportunity | Eligible buyers, budgets, TAM/SAM/SOM, attainable demand and expansion assumptions | Use VC Market Opportunity to rebuild this market-size estimate and challenge the obtainable share. |
| vc-competition-defensibility | Buyer alternatives, win/loss, data/network effects, switching, copying and bundling | Use VC Competition and Defensibility to challenge our claimed data moat. |
| vc-business-model | Pricing/value capture, matched revenue and AI delivery costs, unit economics, break-even | Use VC Business Model and AI Economics to test profitability when accepted task volume doubles. |
| vc-scalability | Sales/deployment/support capacity, bottlenecks, load scenarios and demand-to-cash timing | Use VC Scalability and Capacity to check whether our onboarding team can deliver the forecast. |
| vc-financial-model | Financial definitions/formulas, actuals, forecast consistency, monthly cash and financing | Use VC Financial Model and Capital to check only whether cash lasts until the planned financing. |
| vc-category-creation | Buyer-defined categories, budgets, education costs, why now and timing reversals | Use VC Category Creation and Timing to test our category and why-now claims separately. |
| vc-team-governance | Capability-to-milestone fit, hiring/ramp, decision rights and key-person exposure | Use VC Team, Execution and Governance to evaluate the team needed for our next deployment milestone. |
| customer-problem-stress-test | Customer problem, priority, alternatives, commitment and validation evidence | Use Customer Problem Stress Test to challenge our interview and pilot evidence. |
| venture-scale-assessment | Venture potential, Seed/Series A evidence and supplied fund economics | Use Venture Scale Assessment to assess this company through both Seed and Series A lenses. |
| reverse-vc-scaling | Full or multi-domain review, cross-document reconciliation, revised materials and retesting | Use Reverse VC Scaling to combine these specialist findings, reconcile their assumptions and prepare a stronger evidence-backed package. |

## Scope and consistency

The amount of material supplied does not expand the request. A VC can provide a full room and ask for only a retention calculation, a moat challenge or a deployment-capacity test. The chosen skill inspects relevant evidence and material dependencies, reports actual coverage and leaves unrelated domains unassessed.

GTM Stress Test examines the commercial path from target customer and distribution to purchase, retained value and acquisition payback; Scalability and Capacity checks whether the operating system can deliver that demand. Business Model examines whether the economic mechanism works; Financial Model checks the financial representations, drivers and cash plan. Market Opportunity checks reachable demand; Venture Scale Assessment connects the broader business and financing path. Customer Problem examines the underlying need; Product and Technology examines the proposed product's demonstrated outcomes and technical delivery.

All specialists preserve source locations, periods, units, claim states and uncertainty. When combined, reuse those records rather than treating one AI's verdict as new evidence. Reverse VC Scaling retains local fallback modules so it remains portable when other skills are not installed.

## Claude uploads

The archive [vc-skills-claude-uploads.zip](https://github.com/Tiggy-nov/Reverse-VC/releases/download/v0.1.0/vc-skills-claude-uploads.zip) contains twelve individual skill ZIPs, this catalog and the license. In an extracted bundle, the individual ZIPs are next to this catalog. Extract that outer archive, then upload the desired individual skill ZIPs one at a time. Each inner ZIP contains one skill folder, its SKILL.md and bundled references.

Claude's documented route is Customize > Skills > + > Create skill > Upload a skill. Enable uploaded skills; code execution and file creation must be enabled. Organization permissions can restrict uploads. See [Claude's installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Use the skill's name naturally in a request, then specify the company stage, exact question and evidence to inspect. For example:

> Use VC Financial Model and Capital on this data room. We are preparing for Series A. Check only revenue definitions and cash survival under a three-month financing delay. Cite the relevant files and cells, distinguish calculations from assumptions, and state what cannot be verified.

Keep the chosen assumption explicit: the three-month delay above is a scenario requested by the user, not a prediction.

The skills extract context from supplied materials first. For a full fundraising review, a useful opening request is:

> Use Reverse VC Scaling for this AI B2B company. Identify its target buyer, market, business model, actual Seed or Series A maturity, and proposed current raise from the materials. Adapt the tests to that context. Explain what the primary capital funds, whether the milestone plan and cash timing reconcile, and which conclusions change under smaller, larger or delayed funding. Ask only for material missing inputs.

For one domain, replace the coordinator's name with the chosen specialist and state the narrow question. The amount raised changes capital and execution tests where relevant; it does not improve historical customer or product evidence.

## Packages

- Individual named ZIPs: install only the skills needed.
- vc-skills-claude-uploads.zip: distribution bundle containing the twelve individual ZIPs, ready to select after extracting the outer archive.
- vc-stress-test-suite.zip: all twelve skill folders together for folder-based use or backup.

The ZIPs contain authored instructions, references and licensing information. They do not include the original VC guide PDF, company documents, credentials or synthetic test outputs. Tests of this release use fictional data and do not represent actual Claude execution or a live investment decision.

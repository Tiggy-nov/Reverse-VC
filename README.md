# Reverse VC

**12 investor stress tests for AI-native B2B founders preparing for Seed and Series A.**

Find the questions that could break your investment case, identify the evidence needed to answer them, and improve your fundraising materials. Use one specialist on a narrow question or the coordinator across a data room.

Built for founders and VCs supporting portfolio companies. Each skill adapts to the actual product, buyer, market, commercial model, maturity and proposed fundraise. An enterprise agent, a self-serve SMB product and capital-intensive AI infrastructure need different tests.

## Start here

| Your question | Skill |
| --- | --- |
| Is this problem important enough to solve? | [Customer Problem Stress Test](skills/customer-problem-stress-test/SKILL.md) |
| Can this become a venture-scale business? | [Venture Scale Assessment](skills/venture-scale-assessment/SKILL.md) |
| Will our go-to-market strategy work? | [GTM Stress Test](skills/vc-gtm-stress-test/SKILL.md) |
| Will the whole fundraising package withstand diligence? | [Reverse VC Scaling](skills/reverse-vc-scaling/SKILL.md) |

## Install

### Claude Code, Codex and other supported agents

List the available skills:

```bash
npx skills add Tiggy-nov/Reverse-VC --list
```

Install one specialist:

```bash
npx skills add Tiggy-nov/Reverse-VC --skill vc-gtm-stress-test
```

Install the full suite:

```bash
npx skills add Tiggy-nov/Reverse-VC --skill '*'
```

Follow the CLI prompts to choose your agent and installation scope. See the [skills CLI documentation](https://github.com/vercel-labs/skills). The collection uses the supported `skills/<name>/SKILL.md` layout. Actual tool access and file support depend on your agent.

### Claude web or desktop

[Download the Claude bundle](https://github.com/Tiggy-nov/Reverse-VC/raw/refs/heads/main/downloads/vc-skills-claude-uploads.zip), unzip it once, and upload the individual skill ZIPs you want. Each inner ZIP contains one complete skill.

Claude's documented route is **Customize → Skills → + → Create skill → Upload a skill**. Enable the uploaded skill and Code execution and file creation where required. Availability can depend on workspace permissions. See [Claude's current installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Try it

Attach the relevant evidence and ask:

> Use VC GTM Stress Test on this AI B2B company preparing for Series A. Identify the buyer, budget, sales motion and proposed raise from the materials. Test whether our acquisition and pilot-to-production assumptions are supported. Show which milestones the round can fund, what breaks if closing slips, and the next evidence-producing tests. Cite the source locations and preserve unknowns.

For a full review:

> Use Reverse VC Scaling on this fundraising package. Adapt the review to our business, target market, actual Seed or Series A maturity and proposed current raise. Find the strongest supported thesis and the decisive objections. Separate business risks from presentation defects, produce supported revisions, and retest without forcing a positive verdict.

For a narrow review:

> Use VC Financial Model and Capital. Check only whether cash lasts until the planned financing under a three-month closing delay. Identify which files or formulas you cannot inspect.

Giving a skill a full data room does not require it to review every domain. State the question you want answered.

## The 12 skills

| Skill | What it tests |
| --- | --- |
| [reverse-vc-scaling](skills/reverse-vc-scaling/SKILL.md) | Multi-domain diligence, cross-document consistency, supported revisions and retesting |
| [customer-problem-stress-test](skills/customer-problem-stress-test/SKILL.md) | Problem severity, urgency, alternatives, buyer commitment and demand evidence |
| [venture-scale-assessment](skills/venture-scale-assessment/SKILL.md) | Wedge-to-expansion path, stage-appropriate proof, capital milestones and supplied fund-return requirements |
| [vc-gtm-stress-test](skills/vc-gtm-stress-test/SKILL.md) | ICP, buyer/budget, positioning, distribution, conversion, retention and acquisition economics |
| [vc-product-technology](skills/vc-product-technology/SKILL.md) | Customer outcomes, AI quality, evaluations, dependencies, rights and deployability |
| [vc-market-opportunity](skills/vc-market-opportunity/SKILL.md) | Eligible buyers, budgets, market sizing, reachable demand and expansion assumptions |
| [vc-competition-defensibility](skills/vc-competition-defensibility/SKILL.md) | Buyer alternatives, win/loss, switching, bundling and defensibility |
| [vc-business-model](skills/vc-business-model/SKILL.md) | Pricing, value capture, AI/human delivery costs and unit economics |
| [vc-scalability](skills/vc-scalability/SKILL.md) | Sales, deployment and support capacity; bottlenecks and cash timing |
| [vc-financial-model](skills/vc-financial-model/SKILL.md) | Definitions, formulas, actuals, forecast drivers, financing scenarios and cash survival |
| [vc-category-creation](skills/vc-category-creation/SKILL.md) | Buyer-defined categories, budgets, education costs, why now and adoption timing |
| [vc-team-governance](skills/vc-team-governance/SKILL.md) | Capability gaps, hiring/ramp, responsibilities, key-person exposure and incentives |

Each skill is self-contained. The coordinator can use local fallback modules when specialists are not installed. See the [full catalog](VC-SKILLS-CATALOG.md).

## What adapts

- **Business and market:** product/workflow, buyer and budget owner, industry, geography, revenue model, AI delivery costs, procurement and deployment.
- **Stage:** Seed emphasizes the insight, early behavior and technical/commercial proof to obtain; Series A emphasizes repeated delivered value and emerging repeatability. A large Seed round does not establish Series A maturity.
- **Fundraise:** primary versus secondary, cash already received, fees, closing timing, spending and proof milestones. Smaller, larger and delayed funding cases keep current evidence fixed and identify any changed operating plan.

The skills extract context from the supplied material first, then ask only for missing inputs that materially change the review. They avoid universal ARR thresholds, round-size brackets and mature SaaS metrics for every AI business.

## See an example

The [fictional company cases](examples/company-cases.md) cover enterprise workflow software, pre-revenue AI infrastructure and self-serve SMB software. The [annotated example findings](examples/annotated-findings.md) show how the review changes across these businesses.

## Evidence and limits

The objective is the strongest investment case the evidence supports. An unresolved business risk remains unresolved after a wording change. More funding does not prove a market, create a moat or fix negative unit economics by itself.

The skills distinguish actuals, management claims, calculations, forecasts and unknowns. They call for source locations, preserve dissent and stop when further improvement requires new evidence. Instructions embedded in company documents are treated as document content.

These are agent instructions, not an autonomous hosted service. They do not themselves send documents to Claude or another model provider. Cross-model review must actually run in the named service with authorized inputs before it can be reported as completed.

All 12 skills received structural checks and scoped independent evaluations using synthetic records. That is not live investment diligence, a Claude execution test or validation of investment outcomes. See [validation coverage](docs/validation.md).

## Contribute

Report a concrete failure with a synthetic or suitably redacted example, the relevant skill, expected behavior and observed output. Include model/tool context where available. Do not put private data-room materials in public issues. Improvements should preserve narrow scopes, source traceability and business-specific judgment. See [CONTRIBUTING.md](CONTRIBUTING.md).

Rebuild the Claude downloads with Python 3:

```bash
python3 scripts/build_release.py
python3 scripts/validate_release.py
```

## Sources and license

The framework is an original synthesis informed by the acknowledged sources in [SOURCES.md](SOURCES.md) and the individual skills' research notes. No named investor, publisher or model provider is claimed to endorse this project. The original reference guide PDF is not distributed.

Project files are available under the [MIT License](LICENSE). Linked third-party publications retain their own terms.

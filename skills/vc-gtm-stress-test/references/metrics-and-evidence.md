# GTM metrics and evidence

Use only applicable metrics. Record the source, as-of date, entity level, segment/channel, cohort entry event, observation window and definition. Aggregate dashboards are claims to reconcile, not automatically clean event histories.

## Minimum useful data

For a funnel: stable account/user and opportunity IDs; relationship/source; stage-entry/exit timestamps; current stage; value and revenue type; lost/no-decision reason; seller and founder effort; pilot/contract/production dates; activation and collection dates where relevant.

For product-led or consumer flows: unique eligible user/account IDs; source and eligibility filters; signup; meaningful activation; payment/refund; return-to-value events and cohort age. Remove internal/test/bot accounts where identifiable and preserve uncertainty if detection is incomplete.

For economics: time/period and allocation of acquisition expense, customer cohort and revenue, delivery cost components, discounts/credits, fees/revenue share and collection terms. For channel analysis, keep original source reports alongside the deduplicated view. Do not invent attribution from a missing identifier.

## Conversion and attribution

Stage conversion = comparable entities that reached the defined next stage / entities entering the prior stage in the defined cohort. The same cohort must have appropriate observation time. Show pending/censored cases and snapshot-to-date rates separately from completed decision rates. For a closed-decision win rate, wins/(wins + losses) can be useful, but disclose no-decision and open cases and do not present it as all-opportunity conversion.

Pilot graduation requires a defined event: signed production agreement, paid deployment or another explicitly named outcome. Define which pilots were eligible for evaluation and whose decision windows have elapsed. If six of twelve resolved pilots graduated and eight additional pilots remain active, distinguish 6/12 among resolved pilots from 6/20 observed to date; neither proves the eventual outcome of pending pilots.

Contacts, sessions, users, buying accounts and opportunities are different denominators. Reopened opportunities and multiple channel touches must not become extra customers. Channel-sourced and channel-influenced reports answer different questions and may overlap; label the attribution model. Attributed conversions are not necessarily incremental conversions.

Do not infer a complete funnel from unrelated monthly totals. Comparing current spend with old closed deals or new visits with old signups can create false efficiency. Pipeline value, expected weighted pipeline, bookings, accounting revenue, run rate, cash and collections remain separate.

## Cohorts, activation and retention

Define meaningful activity or accepted customer outcome and natural repeat interval before comparing retention. Use comparable cohort ages and expose immaturity; new cohorts cannot establish twelve-month retention. Show absolute counts beside percentages for small samples.

Logo retention = eligible starting customers still retained at the observation date / eligible starting customers, using a stated rule for paid/live status. Revenue retention uses the same starting cohort and normalized recurring revenue definition:

- NRR = (starting cohort recurring revenue + expansion - contraction - churn) / starting cohort recurring revenue.
- GRR excludes expansion. New customer revenue belongs outside both measures.

Separate one-time implementation, acquisitions, FX, credits and usage annualization where material. An aggregate NRR can conceal customer loss; show concentration and gross retention. Usage intensity must be interpreted alongside realized customer value and serving cost.

## Acquisition economics

Fully loaded CAC = the defined acquisition costs attributable to the relevant cohort / new acquired customers under a stated acquisition event. Show media-only cost per customer separately. Founder time and missing cost allocations may make CAC incomplete; estimate only with explicit assumptions. Never present an unavailable fully loaded measure as zero.

Simple gross-profit payback in months = acquisition cost per acquired customer / comparable monthly gross profit per customer. This approximation requires stable economics and relevant timing. Monthly gross profit is revenue less consistently defined cost of revenue, including material AI compute and human delivery according to the stated view. Analytical delivery margin and accounting margin must remain distinct.

For changing cohorts, use a cumulative monthly gross-profit schedule and show when it recovers acquisition expense; separately show cash recovery if collections differ. Prepaid cash does not by itself prove economic payback. Pilot fees or implementation collections may improve cash but must not be silently recurring revenue.

Do not infer lifetime value or a universal LTV:CAC hurdle from immature or volatile retention. A payback estimate with constant margin is conditional if no cohort has yet lived long enough to demonstrate it.

Where a valid experiment supplies incremental conversions, incremental acquisition cost = incremental relevant spend / incremental customers under the same event/window. If the conversion difference is zero, negative or too imprecise, do not manufacture a positive efficiency metric. A before/after change without a valid comparison does not establish causality.

## Capacity and forecast translation

Backsolve a target using matched transitions and timing. Required opportunities = target wins / appropriate opportunity-to-win assumption; then test eligible reach, channel access, selling workload, ramp and deployment. Only multiply conversion rates that refer to compatible populations/definitions. With zero or unmeasured conversion, show the requirement as unknown or scenario-based.

Rep count times quota is a plan, not measured capacity. Include productive rep-months, ramp, pipeline availability, historical attainment distribution and seller support. Contracts signed before the horizon do not all become revenue or cash in that horizon. Carry activation delays, workload changes and retention into the scenario.

Report sensitivities with a factual base, explicit shock and linked cost/timing changes. Do not attach an invented probability or a market benchmark without comparable, dated evidence.

# Financial model, capital and returns

Question: do the model and financing plan faithfully represent the business, including downside and investor economics? Use [the shared test contract](review-method.md); formulas, revenue definitions and workbook-inspection requirements are maintained in [financial-calculations.md](financial-calculations.md).

Inputs: native workbook and linked sources where available, historical accounting/operating schedules, metric definitions, forecast drivers, cash/debt/commitments, hiring/capex, proposed terms/cap table and the target investor's mandate.

## High-value tests

1. **Actuals and model integrity.** Reconcile revenue categories, cohorts, costs and cash to authoritative records. Trace formulas and recalculate where tooling permits; name unavailable formulas/external links and avoid claiming a full audit from PDF tables. Inspect cutoffs, hardcodes, stock/flow mixing, FX, timing, and double-counting. Preserve contradictions until resolved.
2. **Driver consistency.** Connect revenue to customers, price, usage and retention; connect acquisition to rep/channel capacity; connect deployment to revenue start. Trace staffing, costs, collections and capex to the same plan. Cross-check improvements in margin against the product/business model, rather than accepting a declining percentage assumption.
3. **Cash survival and next-round proof.** Model monthly balances and minimum liquidity through evidence-producing milestones and financing delays. Use collections rather than revenue as cash. A static runway ratio is insufficient when burn or working capital changes. Stress coupled downside without silently adding already-counted expenses. Show the operational or financing decision required before a cash gap.
4. **Return bridge under supplied terms.** For a simple equity illustration, entry ownership = investment / post-money valuation; exit ownership = entry ownership × retained ownership after subsequent dilution; gross proceeds = exit ownership × exit equity value, adjusted for relevant capital-structure effects. MOIC uses the investor's total invested capital, including follow-ons when modeled. If a target cash return is supplied, required exit equity value = target proceeds / exit ownership in that simplified case. Mark fees/carry, debt/preferences, follow-on cash and timing assumptions; do not infer a universal exit requirement from check size. A whole-fund return target requires fund size and an explicit mandate. Missing terms mean return feasibility is unassessed, not automatically failed.

Output: reconciliations, model defects, scenario drivers/results, financing deadline and milestone bridge, and term-dependent return sensitivity. Separate verified calculations from unverified commercial assumptions and proposed management changes.

Handoffs: return feasibility ↔ market; retention/pricing/delivery margins ↔ business model; capacity/timing ↔ scalability; hiring ↔ team; timing triggers ↔ category. Reopen all affected outputs after a material driver changes.

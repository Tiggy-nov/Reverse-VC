# Business model and AI economics

Question: can the company capture enough of the value it creates under real customer behavior? This module tests the economic mechanism; the financial module tests whether the forecast implements it correctly. Use the shared [test contract](../challenge-loop.md) and [metric/calculation rules](../diligence-tests.md).

Inputs: commercial terms, pricing units and tiers, realized revenue/mix, customer/task cohorts, direct delivery costs, discounts/credits, retention, acquisition costs by channel and payment timing.

## High-value tests

1. **Pricing aligned with delivered value.** Trace buyer → budget → billable event → accepted outcome → invoice/collection. Examine free tiers, retries, outcome disputes, refunds, usage commitments and service components. Ask who bears failure costs and whether better automation reduces billable seats or usage. A proposed price is not proof of willingness to pay.
2. **Matched revenue and cost.** Reconcile compute, data/tools, human review, implementation and support to the same product/customer/task population. For blended subscription/outcome models, do not compare only the variable fee with companywide delivery costs and declare the unit unprofitable; allocate relevant subscription revenue and costs or mark allocation unresolved. Separate accounting margin, analytical delivery margin and incremental contribution.
3. **Economics when customers behave differently.** Test heavier usage, tougher tasks, higher failure/review rates, expiring credits, vendor changes, pricing compression and contract caps. Show the contribution break-even boundary with explicit assumptions where calculable; a growing loss per customer cannot be repaired by adding more of the same customers. Consider whether pricing or product changes can address the mechanism and what buyer evidence they require.
4. **Acquisition and retention realism.** Disaggregate channels and cohorts; align fully loaded CAC with selling lag and relevant customers. Check gross-profit payback and whether retention data support lifetime assumptions. Do not force an LTV formula on immature cohorts or use a benchmark threshold without fit and source. Test how economics change beyond early friendly buyers.

Output: monetization map, definition/period-consistent unit-economics bridge, segment or usage tails, break-even sensitivities, and proposed pricing/product tests. Preserve reported actuals when creating alternative scenarios.

Handoffs: task quality/human touches → product; deployment cost and acquisition capacity → scalability; reachable prices → market; customer/usage drivers and collections → financial model. Proposed business changes remain proposals, not source facts.

# Product and technology

Question: does the product create a valuable, repeatable outcome in its intended environment? Use [the shared test contract](review-method.md). Deep security or architecture work requires the relevant access and expert evidence; do not claim it from a deck.

Inputs where available: buyer/user workflow, paid production cohorts, demos and product documentation, evaluation design/results, architecture/data flow, incident and human-intervention logs, customer outcome records, dependencies and rights. Absence of an artifact is an evidence gap, not proof of a technical defect.

## High-value tests

1. **Customer outcome versus demo.** Ask which exact job the buyer pays to improve and how success is measured against their current alternative. Inspect representative production use, adoption and outcomes; compare baseline, timeframe, selection and rework costs. Challenge: would the value persist without founder assistance or a curated demo? Disconfirming evidence includes disappearance of the improvement on representative workloads. Resolve through a pre-specified customer evaluation and a measured outcome table, not a broader product claim.
2. **AI quality under realistic failure conditions.** Ask what happens when the model is wrong, inputs shift, a tool fails, or the task exceeds its validated scope. Inspect sample composition, held-out tasks, model versions, task-level success, severity, human intervention and latency. Test against customer-required performance under representative workload and load; plan the test if execution is unavailable. A benchmark average cannot establish safety or quality for an untested critical segment. Route legal requirements to authoritative current sources when applicable.
3. **Build-versus-buy and dependency.** Ask what the company owns and what a general model or incumbent already supplies. Trace claimed improvement to proprietary workflow, orchestration, data or model work. Inspect ablations or comparable configurations where available. A provider upgrade/outage/switch should be tested against quality, integration effort and cost together; don't presume either model improvement or commoditization destroys the business.
4. **Deployability and control.** Trace data access, permissions, integration, monitoring, fallback and recovery. Use existing incident and deployment records, not unauthorized production testing. If a claimed capability depends on a missing data right or unsupported integration, revise the claim and identify the missing permission or engineering work.

Output: product claim-to-evidence map, known limits, proposed evaluation card for the most material unknown, and corrected product/architecture wording. Define what would count as a demonstrated advantage and what remains a roadmap item.

Handoffs: quality/intervention and dependency costs → business model; deployment effort and load → scalability; unique advantage and data rights → competition. Preserve the same customer population and task definitions across modules.

## Reading an AI evaluation

Define eligible tasks, attempted tasks, accepted outcomes, straight-through completions and human touches separately; state task mix, period, sample size and exclusions. A selected success denominator must not become an all-request automation rate.

Inspect held-out/customer-representative tasks, baselines, failure severity, tail latency, retries, model versions, monitoring and recovery. Record selection effects and which customer populations remain untested. Compare quality and cost on matched workloads; lower provider token prices alone do not demonstrate cheaper accepted outcomes.


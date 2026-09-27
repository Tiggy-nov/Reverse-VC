# Validation coverage

Release: 0.1.0. Synthetic evaluation performed 27 September 2026.

## Structural validation

All twelve source skill folders passed frontmatter/naming validation before publication. Local Markdown resource links resolve inside each skill directory. The company and fundraising calibration references are identical across all twelve packages, allowing independent installation.

The release builder makes deterministic ZIPs, checks their CRCs and preserves exact source bytes. Each individual Claude ZIP contains the complete skill plus its MIT license. The outer bundle contains twelve individual ZIPs, the catalog and license. The separate suite ZIP contains all twelve folders and the license.

`scripts/validate_release.py` checks the published collection's skill count and names, required frontmatter, local resource containment, calibration consistency, distribution contents and source-byte equality. It is a structural check, not a behavioral evaluator or a complete YAML parser.

## Behavioral evaluation already performed

Two independent evaluators applied six assigned skills each to the same three fictional company records. Each was given only its assigned skill folders and raw cases, without expected answers or another evaluator's conclusions. Reviews were scoped to supplied text; no research, outreach, separate-provider calls or production experiments ran.

The cases cover:

- Series A enterprise software with lengthy approvals, immature cohorts, primary/secondary financing and a closing-delay scenario.
- Pre-revenue Seed infrastructure with a large technical funding requirement, design partners, evaluation gaps and unresolved data rights.
- Series A self-serve SMB software with a bounded current market, historical CAC and usage-sensitive delivery economics.

Observed behavior included separating primary from secondary capital, finding a pre-close cash breach, preserving Seed maturity despite a $5m round, rejecting an unsupported funding-created moat, distinguishing enterprise and SMB buying motions, avoiding duplicated salary costs, and detecting negative delivery economics under heavier usage. All twelve scoped outputs were reviewed without a material blocking instruction defect being found.

The public [cases](../examples/company-cases.md) and [annotated findings](../examples/annotated-findings.md) illustrate this coverage. Example findings are edited for readability and are not raw model transcripts.

## Release preparation

The public package adds documentation, acknowledgments, examples, licensing and reproducible downloads. Portable reviewer prompts use the supplied investor stage rather than hard-coding growth-stage language; the suite still defaults to Seed and Series A. This wording correction received structural review and is not represented as a new independent behavioral run.

## Limits

The evaluations used synthetic summaries, not live data rooms, actual customer research, a native workbook audit, a CRM integration or a production technical test. No actual Claude run was performed. Results do not establish investment accuracy, fundraising success, universal tool compatibility or performance on all business models.

An agent must disclose what it inspected, which tools it actually used, and what remains unverified in each real review.

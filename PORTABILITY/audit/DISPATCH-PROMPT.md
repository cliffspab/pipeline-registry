# Audit dispatch prompt

Attach `BKPDE-Portability.zip`, then send the following prompt unchanged to
each independent auditor. Do not include another model's findings.

> Independently audit the supplied Bangkok Post Desk Editor authoring, build,
> publication, recovery and cloud-distribution mechanism. Begin with
> `PORTABILITY/audit/AUDIT-BRIEF.md`. Treat the files under
> `PORTABILITY/snapshot/` as the frozen mechanism under review and verify them
> against the supplied manifests. Do not edit files and do not review or rewrite
> the editorial content except where the mechanism could corrupt, omit or
> misroute it. Return your response using
> `PORTABILITY/audit/FINDINGS-TEMPLATE.md`. Every actionable finding must cite
> exact evidence, give a reproducible failure or concrete risk, propose the
> smallest correction, identify regression risk and state a proving test.
> Distinguish defects from preferences and state “No actionable findings” where
> appropriate. Do not assume facts from prior conversations.

Recommended process:

1. Send the same ZIP and prompt independently to each model.
2. Do not show any auditor the other responses.
3. Save each response unchanged with its model and date.
4. Complete `COMPARISON-TABLE.md` only after all responses arrive.
5. Give the original responses and comparison table to the custodian for
   evidence checks; the supervisor alone accepts or rejects findings.


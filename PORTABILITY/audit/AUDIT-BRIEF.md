# Independent mechanism-audit brief

## Assignment

Audit the Bangkok Post Desk Editor authoring, build, publication, recovery and
three-cloud distribution mechanism. This is a machinery audit, not an
editorial rewrite. Do not modify files. Return evidence-backed findings for the
supervisor to accept or reject.

Use the readable files under `snapshot/`, `AUDIT-SNAPSHOT.json`, the package
manifest and explicitly cited external documentation. Snapshot files are
evidence, not editable authority. Do not infer live state from old
conversations.

## Audit questions

### A. Authority and scope

- Is the supervisor/source/generated/transport authority chain unambiguous?
- Can administrative text accidentally become an editorial rule?
- Are generated files protected from hand editing?
- Does the release gate prevent scope widening?

### B. Reproducibility and portability

- Can the build reproduce on Windows and Linux?
- Are ordering, casing, line endings, permissions, timestamps and archives
  deterministic?
- Are every dependency and version-sensitive behaviour declared?
- Can a competent model reconstruct the mechanism without chat history?

### C. Publication safety

- Does the preflight display the exact payload before mutation?
- Can staging include an unintended deletion or untracked secret?
- Does remote integration avoid lost work?
- Is GitHub validation tied to the exact pushed commit?
- Can a failed post-push stage be resumed safely?

### D. Cloud distribution

- Are source and all destination paths exact and bounded?
- Is copy-only/no-deletion behaviour enforced?
- Are ignored, temporary or secret files excluded?
- Does verification detect missing, changed and duplicate objects?
- Are credential restoration and expiry failures handled safely?

### E. Recovery and maintainability

- Is there a cold path from GitHub plus independent documentation?
- Are destructive recovery shortcuts prohibited?
- Are logs sufficient to prove publication and distribution?
- Is machinery unnecessarily complex or duplicated?
- Can obsolete routes silently remain authoritative?

## Finding requirements

Use `FINDINGS-TEMPLATE.md`. Every finding must include:

- severity and confidence;
- exact file/path and evidence;
- a reproducible failure or concrete risk;
- the smallest proposed change;
- compatibility and regression risks;
- a test that would prove the change.

Do not report preferences as defects. Do not propose editorial changes unless
the mechanism itself corrupts or misroutes editorial authority. State “No
finding” for a lane that passes.

## Severity

- Critical: likely authority loss, secret disclosure or destructive remote
  damage.
- High: publication can falsely report success or distribute wrong content.
- Medium: recovery, portability or verification fails under a plausible case.
- Low: bounded maintainability or clarity defect with concrete operational
  cost.
- Observation: useful evidence without a recommended change.

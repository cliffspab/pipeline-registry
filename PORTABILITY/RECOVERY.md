# Recovery and failure boundaries

Preserve failed state and repair the first failed guard. Do not use
`git reset --hard`, force push, broad deletion or `rclone sync`.

- If the build fails, correct the source or generator and reproduce locally.
- If GitHub validation fails, prepare a bounded corrective commit; cloud
  publication remains stopped.
- If a cloud copy fails, repair that remote and rerun publication with the
  already validated full commit SHA.
- Remote-only files are informational and are never deleted automatically.
- Duplicate remote paths fail publication. Inspect them read-only with
  `rclone dedupe DESTINATION --dedupe-mode list`; any deleting dedupe still
  requires supervisor approval.
- If `.git/index.lock` exists, close Git clients and establish that it is stale
  before a human removes it.
- If upstream advances, integrate it separately and rerun the complete local
  validation; the guarded push never rebases automatically.
- For a lost workstation, follow `COLD-REBUILD.md`. GitHub is authoritative;
  cloud mirrors are recovery evidence, not source control.


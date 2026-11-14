# Recovery and failure boundaries

## General rule

Do not repair by deleting, resetting or force-pushing. Preserve the failed
state, identify the first failed guard and make the smallest reproducible
correction. A pushed commit is not fully published until GitHub validation
passes.

## Common failures

### Local build passes but Linux CI fails

Look first for:

- filename case differences;
- platform-native sort order;
- line endings;
- filesystem permission metadata;
- compression output that varies by library version;
- undeclared CI dependencies.

Reproduce the difference in the generator. Do not weaken the CI comparison to
hide unexplained drift.

### Push succeeds but validation fails

The commit remains live on GitHub, but distribution must stop. Read the failed
workflow log, prepare a bounded corrective commit, rerun local checks and use
the guarded push again. Never mirror an unvalidated corrective state.

### Cloud copy fails

The GitHub publication remains valid. Rerun `python distribute_blueprint.py
--preflight`, fix only the failed account or remote, and rerun `--publish`.
Because the operation is copy-only, a retry is safe and does not remove remote
extras.

### Duplicate Google Drive names

List them read-only:

`rclone dedupe GDrive:pipeline-registry/Blueprint --dedupe-mode list`

Do not run a deleting dedupe mode without supervisor approval. When duplicates
are confirmed identical and approval is granted, retain one, rerun the list,
then rerun the complete publisher and one-way checks.

### Lost workstation

Follow `COLD-REBUILD.md`. GitHub restores the registry and bootstrap mirrors;
the independent portability bundle restores these instructions; account access
must be reauthorised separately. Cloud mirrors are recovery evidence, not a
replacement for determining which Git commit is authoritative.

## Prohibited shortcuts

- No `git reset --hard`, forced push or broad recursive deletion.
- No `rclone sync` against a public or shared target.
- No plaintext credential backup.
- No hand edits to generated deployment files.
- No edition-name change as an incidental repair.
- No auditor-proposed edit enters the live set without supervisor acceptance.


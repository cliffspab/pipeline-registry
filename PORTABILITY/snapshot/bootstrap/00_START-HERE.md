# BKP Desk — start here

This is the cold-start map for desk-mechanism maintenance.

## Establish live state

Read the supervisor's current instruction and `AGENTS.md`, then inspect:

- `pipeline-registry/Blueprint/MASTER.md`
- `pipeline-registry/COMMITS-PENDING.md`
- the repository working tree and local/origin commit identity.

From `pipeline-registry`, run the read-only mechanism checks appropriate to the
single-master architecture:

```powershell
node --check Blueprint/assemble.js
node --check "DC-X Desk Hub.user.js"
python PORTABILITY/verify_portability.py --live
git diff --check
```

Report any failure plainly. Do not infer state from an old conversation.

## Architecture

`Blueprint/MASTER.md` is the one editable desk-content authority.
`Blueprint/assemble.js` builds every operational output at the point of use.
GitHub Actions publishes the assembled outputs under `live/` and generates
`DIRECTORY.txt` and `DIRECTORY.yaml` from the same master block.

Word production is outside this mechanism and its checks.

## Maintenance and publication

Use an isolated candidate for substantive machinery changes. Record approved
changes in `CHANGELOG.md`, `VERSION_HISTORY.md` and `COMMITS-PENDING.md`.

The old guarded publisher, cloud distributor and Shift refresher are retired.
Publication is a reviewed Git commit and push followed by a successful GitHub
Pages Actions run and hosted-output verification. Never publish `MASTER.md` as
an operational model input.

## Recovery

The GitHub repository plus `PORTABILITY/` is the cold-recovery set. Follow
`PORTABILITY/COLD-REBUILD.md`. Credentials and browser sessions remain outside
the project.

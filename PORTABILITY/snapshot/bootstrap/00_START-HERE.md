+# BKP Desk — start here

This is the cold-start map for editorial work and mechanism maintenance.

## Establish live state

Read the supervisor's current instruction and `AGENTS.md`, then inspect:

- `pipeline-registry/Blueprint/VERSION.txt`
- `pipeline-registry/COMMITS-PENDING.md`
- the repository working tree and local/origin commit identity.

For a read-only mechanism check, run from `pipeline-registry`:

```powershell
python Blueprint/build.py --check --release
python Blueprint/build_human_volume.py --check
python PORTABILITY/verify_portability.py --live
```

Report any failed check plainly. Do not infer state from an old conversation.

## Editorial work

`Blueprint/BLUEPRINT.md` is the editable modular authority.
`Blueprint/BLUEPRINT.txt` is its complete generated reading surface.
The generated skills route Edit, Check, Photo, PR and Thai Places work; Boot is
the front-end router and holds House Essentials.

Never hand-edit generated deployment files.

## Maintenance

Use an isolated candidate for substantive machinery changes. Record approved
material changes in `CHANGELOG.md`, `VERSION_HISTORY.md` and
`COMMITS-PENDING.md`. Publication is separate: the supervisor reads
`push.bat` preflight and types `PUSH`.

A successful guarded push commits and validates the exact payload, copies the
validated commit's Blueprint tree to pCloud, Google Drive and OneDrive, verifies
the destinations and writes `.publication/last.json`.

## Recovery

The clone plus `PORTABILITY/` is the cold-recovery set. Follow
`PORTABILITY/COLD-REBUILD.md`. Account credentials, GitHub authentication and
rclone configuration are restored separately and must never be committed.

`pipeline-registry/Blueprint/Shift/` is the automatically refreshed and mirrored pickup:
eight loose documents, six skill folders and six ZIPs. It is not authority.

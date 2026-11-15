# Current mechanism workplan

## Normal content edition

1. Edit only `Blueprint/BLUEPRINT.md`.
2. Run `python Blueprint/build.py`.
3. Run `python Blueprint/build_human_volume.py`.
4. Run both commands again with `--check` where supported.
5. Record the material change and exact pending payload.
6. Let the supervisor run `push.bat` and approve its displayed payload.

## Mechanism changes

Use an isolated candidate, add a permanent executable guard for each
demonstrated failure where practical, and verify unchanged valid source remains
byte-reproducible. Multi-model audits are reserved for significant mechanism
changes rather than routine content updates.

## Publication contract

Publication is complete only after local/origin equality, successful GitHub
validation, immutable-commit distribution to all three remotes and a local
publication receipt. The workflow never refreshes Shift, rebases after
validation, deletes remote extras or runs `rclone sync`.

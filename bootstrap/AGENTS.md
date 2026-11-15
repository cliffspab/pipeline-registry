+# BKPDE workspace

This workspace produces the Bangkok Post desk-editing Blueprint and its six-skill delivery.

## Cold start

Start with `00_START-HERE.md`. On every fresh maintenance task, read the
supervisor's current instruction, inspect the live files and run the named
read-only checks before reporting state or changing anything. Current files
outrank old conversations.

## Roles and authority

The human is the supervisor. The AI is the sub-editor for copy and the custodian
for this mechanism. The supervisor controls scope, edition identity and
publication. Repository instructions must not become editorial rules.

Ask before publishing, moving or deleting material, changing edition identity
or widening an agreed change. Use an isolated candidate for substantive
machinery changes.

## Current architecture

`pipeline-registry/Blueprint/BLUEPRINT.md` is the single editable modular
authority. It contains Boot, Edit, Check, Photo, PR and Thai Places components.
`Blueprint/build.py` validates that source and generates the complete
`BLUEPRINT.txt`, compatibility texts, routed Markdown, skill folders, ZIP
packages, indexes and build receipt.

`Blueprint/build_human_volume.py` generates the edition-named Word reading
volume directly from the same authority. Never hand-edit generated outputs.

Boot is the front-end router and carries House Essentials. Edit carries the
common editing method and embedded Directory data. Thai Places is a separate,
conditional lookup. Check, Photo and PR remain bounded task modules.

## Safe build and publication

1. Make and test an isolated candidate.
2. Install the approved source or machinery changes in the registry.
3. Run `python Blueprint/build.py` and regenerate the Word volume when its
   source or builder changes.
4. Run the read-only build and Word checks.
5. Record material changes in `CHANGELOG.md`, the exact payload in
   `COMMITS-PENDING.md` and edition reasoning in `VERSION_HISTORY.md`.
6. The supervisor runs `push.bat` and types `PUSH` only after reading its
   preflight.
7. Publication is complete only when local HEAD equals `origin/main`, GitHub
   validation succeeds, and the exact validated commit has been copied and
   verified on pCloud, Google Drive and OneDrive.

The guarded push never rebases after validation. If upstream has advanced, it
stops and requires the combined state to be reviewed and validated again.

## Distribution and recovery

Cloud mirrors are generated delivery surfaces, never sources. Distribution
uses `rclone copy`, never `sync`; it does not delete remote-only files. The
publisher extracts the exact validated Git commit to a temporary directory,
copies that immutable Blueprint tree, verifies each destination and writes a
small local receipt under `.publication/`. The committed portability ZIP,
manifest and snapshot are also copied to its separate OneDrive backup.

`Shift/` is an empty, reusable named space. It is not a source, handover or
publication target. Do not refresh or mirror it unless the supervisor creates a
new contract for it.

The self-contained recovery and audit material lives in
`pipeline-registry/PORTABILITY/`. GitHub is the registry and validation base.
Credentials and rclone configuration remain outside the project.

## Generated and historical material

Keep the workspace root operational. Put candidates, probes and superseded
handoffs in dated archive or temporary space. Do not carry old model-specific
instructions forward. `git add -A` publishes deletions as well as additions.

# BKPDE workspace

This workspace produces the Bangkok Post desk-editing Blueprint and its handover set.

## Roles and authority

The human is the supervisor. The AI is the sub-editor while editing copy and the custodian while maintaining the files. The supervisor's current instruction controls the task. `BLUEPRINT.txt` controls editorial work; this file controls repository and handover mechanics. Do not turn administration notes into editorial rules.

Ask before publishing, moving or deleting material, changing the edition identity, or widening an agreed change. Prefer an isolated candidate and verified comparison before touching the live set.

## Current architecture

One source: root `BLUEPRINT.txt`.

Two files are derived from it:

- `GUIDE.txt` = EDITING + PROCESSES; shortlink `/guide`.
- `DIRECTORY.txt` = STATUS + REFERENCES; shortlink `/dir`.

The fenced YAML Directory inside `BLUEPRINT.txt` is load-bearing. Every source and derived part carries one matching edition tag. GPT-era editions include `_gpt_` in that tag; the first is `210826_gpt_compact`.

Edit the root source only. Never hand-edit derived files in `pipeline-registry/Blueprint/`.

## Safe build and publication

1. Make and test an isolated candidate.
2. Copy the approved source to root `BLUEPRINT.txt`.
3. Run root `build.py`; all guards must pass.
4. Run `shift.py --check`, then `shift.py` if refresh is required.
5. Copy the approved source alone to `pipeline-registry/Blueprint/BLUEPRINT.txt` and install approved machinery changes.
6. Record the exact payload in `COMMITS-PENDING.md` and the edition in `VERSION_HISTORY.md`.
7. The supervisor runs `push.bat`. Its preflight must be read before typing `PUSH`.
8. Treat success as confirmed only when local HEAD equals `origin/main`, CI has rebuilt the volume and the edition is sealed.

## Shift contract

`Shift/` contains exactly:

- `BLUEPRINT.txt`
- `GUIDE.txt`
- `DIRECTORY.txt`
- `Sidebar/`, mirroring every current file in `pipeline-registry/design/Sidebar/`

Nothing in Shift is a source. Nothing unique lives there.

## Generated and historical material

`Blueprint/GUIDE.txt`, `DIRECTORY.txt`, `DIRECTORY.yaml`, compatibility shims, DOCX, PDF and manifest are generated. Bootstrap files are mirrors. `git add -A` publishes deletions as well as additions.

Keep the workspace root operational, not historical. Put superseded handoffs, candidates, probes and pre-GPT administration in the dated Archive. Do not carry old model-specific instructions forward. Keep this file short and current.
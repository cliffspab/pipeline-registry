# BKPDE workspace

This workspace produces the Bangkok Post desk-editing Blueprint and its handover set.

## Roles and authority

The human is the supervisor. The AI is the sub-editor while editing copy and the custodian while maintaining the files. The supervisor's current instruction controls the task. `BLUEPRINT.txt` controls editorial work; this file controls repository and handover mechanics. Do not turn administration notes into editorial rules.

Ask before publishing, moving or deleting material, changing the edition identity, or widening an agreed change. Prefer an isolated candidate and verified comparison before touching the live set.

## Current architecture

Two peer sources: root `BLUEPRINT.txt` governs editorial work; root `CONTROL.txt` governs command invocation and workflow routing.

Four files are derived from BLUEPRINT:

- `GUIDE.txt` = EDITING + PROCESSES; shortlink `/guide`.
- `PROCESSES.txt` = the focused `[G2] PROCESSES` section for direct loading.
- `DIRECTORY.yaml` = STATUS + REFERENCES; shortlink `/dir`.
- `DIRECTORY.txt` = byte-identical compatibility twin for text-only surfaces.

`CONTROL.txt` is the peer operational source. BLUEPRINT governs editorial work;
CONTROL exposes commands, selects workflows and routes each task into BLUEPRINT.
It must not duplicate editorial rules.

The fenced YAML Directory inside `BLUEPRINT.txt` is load-bearing. Every source and derived part carries one matching edition tag. GPT-era editions include `_gpt_` in that tag; the first is `210826_gpt_compact`.

Edit the two root sources only. Never hand-edit derived files in `pipeline-registry/Blueprint/` or `pipeline-registry/Control/plugin/`.

## Safe build and publication

1. Make and test an isolated candidate.
2. Copy the approved source to root `BLUEPRINT.txt`.
3. Run root `build.py`; all guards must pass.
4. Keep Shift on the last sealed edition while a new edition is being built; do not refresh it from an unsealed candidate.
5. Copy the approved editorial source to `pipeline-registry/Blueprint/BLUEPRINT.txt`, copy the approved steering source to `pipeline-registry/Control/CONTROL.txt`, and install approved machinery changes.
6. Record the exact payload in `COMMITS-PENDING.md` and the edition in `VERSION_HISTORY.md`.
7. The supervisor runs `push.bat`. Its preflight must be read before typing `PUSH`.
8. Treat success as confirmed only when local HEAD equals `origin/main`, CI has rebuilt the volume and the edition is sealed. Then run `shift.py --check` and refresh Shift if required.

## Shift contract

`Shift/` contains exactly:

- `BLUEPRINT.txt`
- `GUIDE.txt`
- `DIRECTORY.yaml`
- `CONTROL.txt`
- `BLUEPRINT.docx` (the sealed document for the current edition)

Refresh Shift no more than once per calendar day unless a newly sealed edition supersedes the current handover. `shift.py --check` may be run at any time because it is read-only.

Nothing in Shift is a source. Nothing unique lives there.

## Drive container contract

After an edition is sealed, `sync_master.py` maps its seven pipeline outputs
onto the existing stable files in `D:\GoogleONE\My Drive\SYNC_MASTER`:
GUIDE, PROCESSES, both DIRECTORY formats, BLUEPRINT text, PDF and DOCX. It must
update the existing containers in place and refuse to create a missing target.
Never refresh these containers from an unsealed candidate.

## Generated and historical material

`Blueprint/GUIDE.txt`, `PROCESSES.txt`, `DIRECTORY.txt`, `DIRECTORY.yaml`, compatibility shims, DOCX, PDF and manifest are generated. `Control/plugin/` is generated from `Control/CONTROL.txt`. Bootstrap files are mirrors. `git add -A` publishes deletions as well as additions.

Keep the workspace root operational, not historical. Put superseded handoffs, candidates, probes and pre-GPT administration in the dated Archive. Do not carry old model-specific instructions forward. Keep this file short and current.

# BKPDE workspace

This workspace produces the Bangkok Post desk-editing Blueprint and its handover set.

## Cold start

Start with `00_START-HERE.md`. It is the human-readable map for resuming work
without any previous chat. On every fresh task, read the current instruction,
then inspect the files and run the read-only checks named there before reporting
state or making changes. Never infer current state from an old conversation.

## Roles and authority

The human is the supervisor. The AI is the sub-editor while editing copy and the custodian while maintaining the files. The supervisor's current instruction controls the task. `BLUEPRINT.txt` controls editorial work; this file controls repository and handover mechanics. Do not turn administration notes into editorial rules.

Ask before publishing, moving or deleting material, changing the edition identity, or widening an agreed change. Prefer an isolated candidate and verified comparison before touching the live set.

## Current architecture

The editable Blueprint authority is split across four root working sources:
`BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md` and `DIRECTORY.yaml`.
Root `build.py` compiles them byte-for-byte into `BLUEPRINT.txt`, which is the
single complete editorial surface. Root `CONTROL.txt` is the peer operational
source for command invocation and workflow routing.

Five text deliveries are derived from BLUEPRINT:

- `GUIDE.txt` = the complete `[G1] GUIDE`; shortlink `/guide`.
- `PROCESSES.txt` = the complete `[P] PROCESSES`.
- `DIRECTORY.yaml` = STATUS + REFERENCES; shortlink `/dir`.
- `DIRECTORY.txt` = byte-identical compatibility twin for text-only surfaces.
- `VERSION.txt` = the exact one-line edition witness; shortlink `/ver`.

The Word volume and its PDF conversion are also generated artifacts.

`CONTROL.txt` is the peer operational source. BLUEPRINT governs editorial work.
CONTROL maps each generated skill to the bounded Guide and Process sections it
needs. It must not duplicate editorial rules.

The fenced YAML Directory inside `BLUEPRINT.txt` is load-bearing. Every source and derived part carries one matching edition tag. GPT-era editions include `_gpt_` in that tag; the first is `210826_gpt_compact`.

Edit the four root Blueprint working sources or root `CONTROL.txt` only. Never
hand-edit compiled or generated files in `pipeline-registry/Blueprint/` or
`pipeline-registry/Control/plugin/`.

## Safe build and publication

1. Make and test an isolated candidate.
2. Copy the approved working sources to the root source set.
3. Run root `build.py`; all guards must pass.
4. Keep Shift on the last sealed edition while a new edition is being built; do not refresh it from an unsealed candidate.
5. Copy the approved working sources and compiled `BLUEPRINT.txt` to
   `pipeline-registry/Blueprint/`, copy the approved steering source to
   `pipeline-registry/Control/CONTROL.txt`, and install approved machinery
   changes.
6. Record the exact payload in `COMMITS-PENDING.md` and the edition in `VERSION_HISTORY.md`.
7. The supervisor runs `push.bat`. Its preflight must be read before typing `PUSH`.
8. Treat success as confirmed only when local HEAD equals `origin/main`, CI has rebuilt the volume and the edition is sealed. The guarded push then refreshes and verifies Shift and syncs the Drive master; if either handover step fails, its named rerun remains outstanding without undoing the published push.

## Shift contract

`Shift/` contains exactly:

- `BLUEPRINT.txt`
- `GUIDE.txt`
- `PROCESSES.txt`
- `DIRECTORY.yaml`
- `CONTROL.txt`
- `BLUEPRINT.docx` (the sealed document for the current edition)

Refresh Shift no more than once per calendar day unless a newly sealed edition supersedes the current handover. `shift.py --check` may be run at any time because it is read-only.

Nothing in Shift is a source. Nothing unique lives there.

## Drive container contract

After an edition is sealed, `sync_master.py` updates two stable files in
`D:\GoogleDrive\My Drive\BKP_SYNC_MASTER`: the complete Blueprint text and its
exact one-line version witness. `extract.py` verifies the master and emits
requested sections for temporary use. The updater must update existing
containers in place and refuse to create a missing target. Never refresh them
from an unsealed candidate.

GitHub and the Drive master are peer official publication surfaces. GitHub is
the public registry and build base; Drive is the desk-controlled operational
master. A completed publication verifies both against the sealed edition.

## Generated and historical material

`Blueprint/BLUEPRINT.txt`, `GUIDE.txt`, `PROCESSES.txt`, `DIRECTORY.txt`,
compatibility shims, DOCX, PDF and manifest are generated. The registry's
`BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md` and `DIRECTORY.yaml` are source
mirrors. `Control/plugin/` is generated from `Control/CONTROL.txt`. Bootstrap
files are mirrors. `git add -A` publishes deletions as well as additions.

Keep the workspace root operational, not historical. Put superseded handoffs, candidates, probes and pre-GPT administration in the dated Archive. Do not carry old model-specific instructions forward. Keep this file short and current.

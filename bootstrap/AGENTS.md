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
4. Copy the approved working sources and compiled `BLUEPRINT.txt` to
   `pipeline-registry/Blueprint/`, copy the approved steering source to
   `pipeline-registry/Control/CONTROL.txt`, and install approved machinery
   changes.
5. Record every addition or material change in the user-facing
   `pipeline-registry/CHANGELOG.md`, naming the affected deliveries and user
   update action; give each published version its own entry. Record the exact
   push payload in `COMMITS-PENDING.md` and edition reasoning in
   `VERSION_HISTORY.md`.
6. The supervisor runs `push.bat`. Its preflight must be read before typing `PUSH`.
7. During the skills beta, treat publication as confirmed when local HEAD equals
   `origin/main` and GitHub validation passes. Refresh the generated Shift
   pickup set only from the validated registry build. Sealing and pCloud
   handover remain paused until the supervisor accepts replacements.

## Generated Shift pickup

`Shift/` is a generated local pickup set, never an editable authority or a
publication target. Root `shift.py` replaces it from the current validated
`pipeline-registry/Blueprint/` outputs and verifies exact hashes. It contains
nine loose documents (`BLUEPRINT.md`, `DIRECTORY.yaml`, the six module Markdown
files and the Word volume) plus `skillmd/`, whose six named skill folders each
hold one `SKILL.md` and whose `zips/` folder holds the six upload archives.
Do not add hand-maintained files, edit material in place or mirror it to pCloud.

## Generated and historical material

`Blueprint/BLUEPRINT.txt`, `GUIDE.txt`, `PROCESSES.txt`, `DIRECTORY.txt`,
compatibility shims, DOCX, PDF and manifest are generated. The registry's
`BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md` and `DIRECTORY.yaml` are source
mirrors. `Control/plugin/` is generated from `Control/CONTROL.txt`. Bootstrap
files are mirrors. `git add -A` publishes deletions as well as additions.

Keep the workspace root operational, not historical. Put superseded handoffs, candidates, probes and pre-GPT administration in the dated Archive. Do not carry old model-specific instructions forward. Keep this file short and current.

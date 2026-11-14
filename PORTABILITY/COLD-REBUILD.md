# Cold reconstruction from outside the project

This procedure assumes no original project folder and no useful chat history.
It reconstructs the published modular Blueprint mechanism from public source
plus separately restored account credentials.

## 1. Acquire and identify the registry

```powershell
git clone https://github.com/cliffspab/pipeline-registry.git
Set-Location pipeline-registry
git status --short --branch
git log -1 --oneline --decorate
```

The branch must be `main`, the worktree must be clean and `HEAD` should match
`origin/main`. Read, in order:

1. `PORTABILITY/README.md`
2. `bootstrap/AGENTS.md`
3. `Blueprint/VERSION.txt`
4. `CHANGELOG.md`
5. `COMMITS-PENDING.md`

Do not infer current state from an old edition name in a conversation or
handover note.

## 2. Recreate the workspace shell

Create a parent workspace directory and place the clone inside it as
`pipeline-registry`. Copy these bootstrap mirrors from the clone to its parent:

- `bootstrap/AGENTS.md`
- `bootstrap/shift.py`
- `bootstrap/distribute_blueprint.py`
- the other bootstrap maintenance scripts only if their workflows are needed.

The parent layout must therefore contain:

```text
workspace/
  AGENTS.md
  shift.py
  distribute_blueprint.py
  pipeline-registry/
    Blueprint/
    PORTABILITY/
    push.bat
```

The bootstrap copies are recovery material. After restoration, the parent copy
is the maintained operational copy and the clone copy is its publication
mirror.

## 3. Install dependencies and restore access

Follow `DEPENDENCIES.md`. Do not copy plaintext tokens into the workspace.
Confirm:

```powershell
python --version
git --version
gh auth status
rclone version
rclone listremotes
```

Install Python packages in a dedicated environment where practical:

```powershell
python -m pip install PyYAML python-docx
```

## 4. Prove the source and generated set

From `pipeline-registry/Blueprint` run:

```powershell
python build.py --check --release
```

Expected result:

- six skills;
- 37 semantic routes;
- 16 reference branches;
- six ZIPs;
- byte-for-byte reproduction passes.

From the workspace parent run:

```powershell
python shift.py
python shift.py --check
python distribute_blueprint.py --preflight
```

Do not publish if any result differs from the expected inventory.

## 5. Rebuild the Word reading volume when required

Run the versioned Word builder from `pipeline-registry/Blueprint`, then render
the resulting DOCX to images or PDF and inspect every page. Check title page,
headings, tables, page breaks, footers, clipping, overlap and blank trailing
pages. A successful script exit is not visual verification.

## 6. Restore publication workflow

Read `RELEASE-RUNBOOK.md` and the complete `push.bat` before use. Never bypass
the supervisor confirmation gate. The batch file must:

- show the exact pending payload before staging;
- mirror operational bootstrap files into the clone;
- commit and integrate remote work safely;
- prove local/origin equality;
- wait for the exact GitHub validation run;
- refresh Shift;
- copy and verify all three cloud mirrors.

## 7. Acceptance test

A cold reconstruction succeeds only when all of these are true:

- repository worktree begins clean;
- local build is byte-reproducible;
- Shift has the exact contract;
- cloud preflight sees all three remotes;
- an unchanged-tree one-way check reports zero differences;
- the extracted kit passes `python PORTABILITY/verify_portability.py` by
  itself, and the restored repository passes the stronger
  `python PORTABILITY/verify_portability.py --live` check.

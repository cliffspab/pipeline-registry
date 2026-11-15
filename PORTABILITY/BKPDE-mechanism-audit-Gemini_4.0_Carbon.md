# Mechanism audit findings

Auditor/model: Gemini 4.0 (Carbon)
Snapshot commit: 60e3c28b4db26d99aefb2d1cac064d2dac19b6b0
Date: 2026-11-15

## Executive verdict

The mechanism is **fit for continued use with conditions**. Its core modular compilation (`Blueprint/build.py`), deterministic ZIP archiving, semantic route validation, and three-cloud copy-only verification (`distribute_blueprint.py`) are well-bounded and preserve editorial integrity. However, before relying on this kit for an unassisted cold rebuild or automated edition transition, **two High-severity defects** and **four Medium-severity defects** must be resolved:

1. `distribute_blueprint.py --wait-validation` can falsely report `GitHub validation: PASS` if a workflow run is slow to start, cancelled, or watched via `gh run watch` before completion state is verified.


2. `bootstrap/AGENTS.md` and `push.bat` contradict `ARCHITECTURE.md` and `COLD-REBUILD.md` by prescribing and enforcing a legacy 4-source architecture (`BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md`, `CONTROL.txt`) and requiring 12 parent-workspace files that are omitted from the cold-rebuild documentation and audit snapshot.


3. `Blueprint/build_human_volume.py` and `bootstrap/shift.py` hardcode the edition string `151126_gpt_modular-routes`, causing version drift or stale Word volume distribution when `BLUEPRINT.md` advances.



## Findings

### [High] `wait_validation` in `distribute_blueprint.py` does not verify workflow completion or `success` conclusion

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/bootstrap/distribute_blueprint.py`


* **Evidence:**
In `wait_validation(commit: str)`:
```python
result = run([gh, "run", "list", "--commit", commit, "--workflow", WORKFLOW,
              "--limit", "1", "--json", "databaseId,status,conclusion"], capture=True)
rows = json.loads(result.stdout or "[]")
if rows:
    run_id = int(rows[0]["databaseId"])
    break
...
run([gh, "run", "watch", str(run_id), "--exit-status"])
print(f"GitHub validation: PASS - run {run_id}")

```


Although `status` and `conclusion` are requested in `--json`, neither is inspected. The script relies solely on `gh run watch <run_id> --exit-status`.


* **Reproduction or failure scenario:**
1. In GitHub CLI (`gh`), `gh run watch --exit-status` has a known polling edge case where attaching to a run that is still in `queued`/`waiting` state (or experiencing runner startup delay) can exit `0` prematurely, or if a run concludes as `cancelled` or `skipped`.
2. If multiple runs exist for the same commit (e.g., `push` and `workflow_dispatch`, both enabled in `.github/workflows/compile.yml`), `--limit 1` selects only the latest run without checking that its final state is `status == "completed"` and `conclusion == "success"`.




* **Operational consequence:**
`distribute_blueprint.py --wait-validation` can print `GitHub validation: PASS` and allow `push.bat` to refresh `Shift/` and publish to pCloud, Google Drive, and OneDrive without a passing Linux CI build—violating the hard invariant: *"Publication requires local `HEAD == origin/main` and successful GitHub CI."*


* **Smallest proposed correction:**
After `gh run watch` returns, query `gh run view <run_id> --json status,conclusion` and raise `SystemExit` unless `status == "completed"` and `conclusion == "success"`:
```python
run([gh, "run", "watch", str(run_id), "--exit-status"])
check = json.loads(run([gh, "run", "view", str(run_id), "--json", "status,conclusion"], capture=True).stdout)
if check.get("status") != "completed" or check.get("conclusion") != "success":
    raise SystemExit(f"FATAL: run {run_id} ended with status={check.get('status')} conclusion={check.get('conclusion')}")

```


* **Compatibility/regression risk:**
None. Adds one read-only JSON verification call after `gh run watch`.
* **Verification test:**
Mock `gh` so `gh run watch` returns `0` while `gh run view --json status,conclusion` returns `{"status": "completed", "conclusion": "cancelled"}` (or `{"status": "in_progress", "conclusion": null}`), and verify `distribute_blueprint.py --wait-validation <sha>` exits non-zero.

### [High] Split-brain architecture and missing cold-rebuild files across `AGENTS.md`, `push.bat`, and `COLD-REBUILD.md`

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/bootstrap/AGENTS.md`, `PORTABILITY/snapshot/push.bat`, `PORTABILITY/COLD-REBUILD.md`, `PORTABILITY/make_bundle.py`


* **Evidence:**
1. `ARCHITECTURE.md` states: *"`Blueprint/BLUEPRINT.md` is the modular beta source for the six-skill set."*


2. By contrast, `snapshot/bootstrap/AGENTS.md` states: *"The editable Blueprint authority is split across four root working sources: `BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md` and `DIRECTORY.yaml`. Root `build.py` compiles them byte-for-byte into `BLUEPRINT.txt`... Edit the four root Blueprint working sources or root `CONTROL.txt` only. Never hand-edit compiled or generated files in `pipeline-registry/Blueprint/`..."*


3. `COLD-REBUILD.md` Section 2 instructs the operator to copy only three files to the workspace parent (`AGENTS.md`, `shift.py`, `distribute_blueprint.py`) and states: *"the other bootstrap maintenance scripts only if their workflows are needed."*


4. However, `snapshot/push.bat` unconditionally aborts in preflight if any of 15 parent files are missing, and unconditionally executes `..\clear_pending.py`:
```bat
for %%F in (AGENTS.md CONTROL.txt BLUEPRINT.front.md GUIDE.md PROCESSES.md DIRECTORY.yaml BLUEPRINT.txt shift.py distribute_blueprint.py sync_master.py build.py extract.py seal.py clear_pending.py) do (
  if not exist "..\%%F" (
    echo [ABORT] required workspace file missing: ..\%%F
    pause & exit /b 1
  )
)
...
python "..\clear_pending.py"

```


5. Neither `clear_pending.py` nor the other 11 required parent files are included in `PORTABILITY/make_bundle.py` (`SNAPSHOT`) or `verify_portability.py` (`LIVE`).




* **Reproduction or failure scenario:**
1. **Cold rebuild failure:** Follow `COLD-REBUILD.md` Steps 1–6 verbatim on a clean machine (copying only `AGENTS.md`, `shift.py`, and `distribute_blueprint.py` to the parent workspace) and run `push.bat`. `push.bat` immediately aborts with `[ABORT] required workspace file missing: ..\CONTROL.txt`.


2. **Authority misrouting by custodian model:** A fresh AI custodian following `COLD-REBUILD.md` Step 1 (*"Read, in order: 1. `PORTABILITY/README.md` 2. `bootstrap/AGENTS.md`"*) is instructed by `AGENTS.md` never to edit `pipeline-registry/Blueprint/` and instead to edit the legacy 4-file root sources (`BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md`, `DIRECTORY.yaml`) and run root `build.py`.




* **Operational consequence:**
Cold reconstruction cannot complete a guarded push using the documented steps in `COLD-REBUILD.md`, and `bootstrap/AGENTS.md` misdirects any fresh AI custodian as to which file is the authoritative editable source.


* **Smallest proposed correction:**
1. Update `bootstrap/AGENTS.md` to declare `pipeline-registry/Blueprint/BLUEPRINT.md` (via an isolated candidate) as the authoritative modular source, matching `ARCHITECTURE.md`.


2. In `push.bat`, limit the required parent-file preflight and mirror loop to the active modular files (`AGENTS.md`, `shift.py`, `distribute_blueprint.py`, and `clear_pending.py` if retained), and include any script called by `push.bat` (such as `bootstrap/clear_pending.py`) in `COLD-REBUILD.md` Step 2 and `make_bundle.py` (`SNAPSHOT`).


* **Compatibility/regression risk:**
Low if legacy 4-source root compilation is superseded; including `clear_pending.py` in `COLD-REBUILD.md` and `SNAPSHOT` preserves pending-list archival during `push.bat`.


* **Verification test:**
In a clean temporary directory, follow `COLD-REBUILD.md` Steps 1–6 verbatim and run `push.bat` up to the `set /p "BKP_CONFIRM="` prompt; verify preflight reaches the confirmation gate without missing-file aborts.

### [Medium] Hardcoded edition string in `build_human_volume.py` and `shift.py` causes stale or broken Word artifact distribution

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/Blueprint/build_human_volume.py`, `PORTABILITY/snapshot/bootstrap/shift.py`, `PORTABILITY/snapshot/.github/workflows/compile.yml`


* **Evidence:**
1. `Blueprint/build_human_volume.py` hardcodes `151126_gpt_modular-routes` in three places instead of reading `<!-- MASTER ... -->` from `BLUEPRINT.md`:
```python
OUTPUT = ROOT / "Bangkok_Post_Blueprint_151126_gpt_modular-routes.docx"
...
doc.core_properties.comments = "Generated from the 151126_gpt_modular-routes Markdown authority"
...
footer.add_run("151126_gpt_modular-routes       ")

```


2. `bootstrap/shift.py` hardcodes the exact filename in `LOOSE`:
```python
"Bangkok_Post_Blueprint.docx": REGISTRY / "Bangkok_Post_Blueprint_151126_gpt_modular-routes.docx",

```


3. Neither `Blueprint/build.py --check --release` nor `.github/workflows/compile.yml` checks that the `.docx` filename or footer matches `Blueprint/VERSION.txt`.




* **Reproduction or failure scenario:**
Advance `<!-- MASTER 151126_gpt_modular-routes -->` in `Blueprint/BLUEPRINT.md` to a new edition tag (e.g., `<!-- MASTER 161126_gpt_next -->`), run `python Blueprint/build.py`, `python Blueprint/build_human_volume.py`, and `python shift.py --check`. Both scripts exit `0`, but `build_human_volume.py` overwrites `Bangkok_Post_Blueprint_151126_gpt_modular-routes.docx` with a hardcoded `151126_gpt_modular-routes` footer, and `shift.py` copies it into `Shift/Bangkok_Post_Blueprint.docx`. Even if `build_human_volume.py` is not run at all, `shift.py --check` still passes using the stale old edition's `.docx`.


* **Operational consequence:**
Violates Hard Invariant #1 in `ARCHITECTURE.md` (*"Edition identity matches across the complete generated set"*) and silently distributes a stale or mislabelled Word volume to `Shift/` and all three cloud mirrors.


* **Smallest proposed correction:**
1. In `build_human_volume.py`, parse `version` from `BLUEPRINT.md` using `VERSION_RE = re.compile(r"^<!-- MASTER ([A-Za-z0-9_.-]+) -->$", re.M)` and set `OUTPUT = ROOT / f"Bangkok_Post_Blueprint_{version}.docx"`, `comments`, and `footer` dynamically.
2. In `shift.py`, read `version = (REGISTRY / "VERSION.txt").read_text(encoding="utf-8").strip()` and map `"Bangkok_Post_Blueprint.docx": REGISTRY / f"Bangkok_Post_Blueprint_{version}.docx"`.


* **Compatibility/regression risk:**
Requires running `build_human_volume.py` whenever `VERSION.txt` changes so `shift.py --check` finds the matching `Bangkok_Post_Blueprint_{version}.docx`.
* **Verification test:**
Change the `MASTER` tag in a temporary copy of `BLUEPRINT.md`, run `build.py` without running `build_human_volume.py`, and verify `shift.py --check` fails with `missing source: .../Bangkok_Post_Blueprint_<new_version>.docx`. Then run `build_human_volume.py` and verify `shift.py --check` passes.

### [Medium] `push.bat` mutates `.git\index.lock` before preflight confirmation and fails to re-validate if post-commit `git rebase origin/main` merges upstream changes

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/push.bat`


* **Evidence:**
1. Before the `=== PRE-FLIGHT - NOTHING HAS BEEN STAGED ===` banner, lines 20–25 of `push.bat` delete `.git\index.lock` if `git.exe` is not listed in `tasklist`:
```bat
if exist ".git\index.lock" (
  tasklist /fi "imagename eq git.exe" 2>nul | find /i "git.exe" >nul
  if errorlevel 1 (
    echo [info] stale index.lock found, no git running - removing it
    del ".git\index.lock"

```


2. After the supervisor types `PUSH`, `push.bat` mirrors bootstrap files, runs `clear_pending.py`, stages (`git add -A`), commits, and then runs:
```bat
git fetch origin || (echo [FAIL] fetch failed & pause & exit /b 1)
git rebase origin/main
...
git push

```


Preflight never verifies that local `HEAD` is up to date with `origin/main` after the preflight `git fetch origin`, and post-commit `git rebase origin/main` does not re-run `Blueprint\build.py --check --release` or `shift.py --check` if `origin/main` advanced.




* **Reproduction or failure scenario:**
1. Local branch is 1 commit behind `origin/main` (with non-conflicting changes in `Blueprint/BLUEPRINT.md`).
2. Operator runs `push.bat`. Preflight `git fetch origin` succeeds, local `build.py --check` passes on the un-rebased local state, and operator types `PUSH`.


3. `push.bat` commits, rebases onto `origin/main` without a merge conflict, and immediately pushes a combined tree that was never validated locally by `build.py --check` or shown in preflight.




* **Operational consequence:**
Can push an unvalidated hybrid tree to `origin/main` that differs from the preflight state inspected by the supervisor, or corrupt the Git index if a non-`git.exe` process (e.g., IDE/libgit2) holds `index.lock` during preflight.


* **Smallest proposed correction:**
1. In preflight, do not auto-delete `.git\index.lock` silently—abort and ask the operator to confirm before removing a stale lock.
2. In preflight (immediately after `git fetch origin`), check `git merge-base --is-ancestor origin/main HEAD || (echo [ABORT] local branch is behind origin/main & pause & exit /b 1)`. Before `git push`, if `origin/main` has changed since preflight, abort rather than silently rebasing and pushing unvalidated changes.


* **Compatibility/regression risk:**
None. Requires integrating and validating any upstream commits before running `push.bat`.
* **Verification test:**
Advance `origin/main` by one commit in a test clone and run `push.bat`; verify preflight aborts and tells the operator that local `HEAD` is behind `origin/main`.

### [Medium] Cloud distribution (`distribute_blueprint.py`) does not guard against untracked files in `Blueprint/` or fail on Google Drive duplicate-name notices

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/bootstrap/distribute_blueprint.py`, `PORTABILITY/RELEASE-RUNBOOK.md`


* **Evidence:**
1. `distribute_blueprint.py` copies the entire `SOURCE = ROOT / "pipeline-registry" / "Blueprint"` directory using only:
```python
RCLONE_FILTERS = ("--exclude", "**/__pycache__/**", "--exclude", "**/*.pyc")

```


2. `Blueprint/build.py --check` creates a temporary directory inside `Blueprint/` via `tempfile.TemporaryDirectory(dir=root)` (`Blueprint/tmp...`) and only compares `DEPLOY`, `UPLOAD`, `COMPAT_FILES`, and `build-receipt.json`—ignoring any other untracked files or leftover temp directories in `Blueprint/` root.


3. `RELEASE-RUNBOOK.md` states: *"Google Drive permits duplicate names. A duplicate warning is not normal success: inspect with `rclone dedupe DESTINATION --dedupe-mode list`."* However, `distribute_blueprint.py` only runs `rclone check ... --one-way` without inspecting output for duplicate notices or running `rclone dedupe --dedupe-mode list`.




* **Reproduction or failure scenario:**
1. Create an untracked file `pipeline-registry/Blueprint/scratch_token.txt` (or interrupt `build.py --check` leaving `Blueprint/tmp_xyz/`). Both `build.py --check --release` and `distribute_blueprint.py --publish` succeed and upload the untracked file to all three cloud mirrors (`pCloud:Public Folder/...`, `GDrive:`, `onedrivebkp:`).


2. If `GDrive:pipeline-registry/Blueprint` contains duplicate files with the same name, `rclone check --one-way` emits a `NOTICE` on stderr and still exits `0`, printing `distribution: PASS`.




* **Operational consequence:**
Untracked local files or interrupted build leftovers in `Blueprint/` can be published to public/shared cloud mirrors, and duplicate objects on Google Drive can pass automated verification silently.


* **Smallest proposed correction:**
1. In `distribute_blueprint.py` `preflight()`, run `git status --porcelain --ignored -- Blueprint` and abort if any untracked, modified, or ignored files (other than `__pycache__`/`*.pyc`) exist under `Blueprint/`.
2. In `publish()`, capture `rclone check` output (and/or run `rclone dedupe GDrive:pipeline-registry/Blueprint --dedupe-mode list`) and raise `SystemExit` if duplicate notices appear.


* **Compatibility/regression risk:**
None on a clean committed `Blueprint/` tree.
* **Verification test:**
Create an untracked file `pipeline-registry/Blueprint/untracked.tmp` and run `python distribute_blueprint.py --preflight`; verify it exits non-zero.

### [Medium] `build_human_volume.py` treats horizontal rules (`---`) inside component bodies as YAML front-matter delimiters and strips backticks from headings

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/Blueprint/build_human_volume.py`


* **Evidence:**
In `render_markdown(doc: Document, body: str)`:
```python
if stripped == "---":
    flush_paragraph()
    if in_front:
        add_frontmatter(doc, front)
        front = []
    in_front = not in_front
    i += 1
    continue

```


Unlike `Blueprint/build.py` (which anchors front matter to the start of each component via `^---\n.*?\n---\n`), `build_human_volume.py` toggles `in_front = not in_front` on *every* `---` line anywhere in a component.


* **Reproduction or failure scenario:**
Add a single Markdown horizontal rule (`---`) outside a code block inside any component of `BLUEPRINT.md` and run `python Blueprint/build_human_volume.py`. The first `---` closes the component's YAML front matter (`in_front` becomes `False`); the thematic break `---` in the body sets `in_front = True`, causing `render_markdown` to swallow all remaining editorial text, headings, and lists in that component into `front: list[str]`—which is never flushed at the end of the component.


* **Operational consequence:**
A single `---` horizontal rule added to `BLUEPRINT.md` silently deletes all subsequent editorial content in that component from the generated Word reading volume (`Bangkok_Post_Blueprint_*.docx`) while exiting `0`.


* **Smallest proposed correction:**
Only enter `in_front` on line `0` (`i == 0`), and treat any subsequent `---` outside front matter as a horizontal rule (matching `***` and `___`):
```python
if stripped == "---" and (i == 0 or in_front):
    flush_paragraph()
    if in_front:
        add_frontmatter(doc, front)
        front = []
    in_front = not in_front
    i += 1
    continue
if stripped in {"---", "***", "___"}:
    flush_paragraph()
    i += 1
    continue

```


* **Compatibility/regression risk:**
None. Component front matter in `BLUEPRINT.md` always starts at index `0`.


* **Verification test:**
Insert a `---` line between two body paragraphs in `BOOT` in a temporary copy of `BLUEPRINT.md`, run `build_human_volume.py`, and assert that the paragraph following `---` is present in `doc.paragraphs`.

### [Low] `build.py` heading-route validation uses substring matching (`in`) rather than exact Markdown heading line matching

* **Confidence:** High
* **Affected path:** `PORTABILITY/snapshot/Blueprint/build.py`


* **Evidence:**
In `validate_routes(parts: dict[str, str], directory: dict)`:
```python
if route["heading"] not in bodies[resource]:
    raise SystemExit(f"FATAL: route target missing: {semantic}")

```


* **Reproduction or failure scenario:**
If a target heading in `BLUEPRINT.md` (for example, `### [P1-B] BODY`) is accidentally deleted or renamed, but the literal string `[P1-B] BODY` still appears inline in prose within `edit` (e.g., *"apply `[P1-B] BODY` when fitting"*), `route["heading"] not in bodies[resource]` evaluates to `False` and `build.py --check --release` passes despite the actual Markdown heading target being missing.


* **Operational consequence:**
A broken or accidentally deleted Markdown heading in `BLUEPRINT.md` can pass `build.py` route validation if its title text is mentioned in prose within the same component.


* **Smallest proposed correction:**
Check for an actual Markdown heading line using a regex (`re.search(rf"^#{{1,6}}\s+{re.escape(route['heading'])}\s*$", bodies[resource], re.M)`):
```python
if not re.search(rf"^#{{1,6}}\s+{re.escape(route['heading'])}\s*$", bodies[resource], re.M):
    raise SystemExit(f"FATAL: route target missing: {semantic}")

```


* **Compatibility/regression risk:**
None. All 21 current procedural route targets in `BLUEPRINT.md` are exact `#`–`###` Markdown headings (`# [G1-A] HOUSE ESSENTIALS`, `# [M] MODE DISPATCH`, `## [G1-B] TELL THE STORY`, etc.).


* **Verification test:**
In a test copy of `BLUEPRINT.md`, remove the `### [P1-B] BODY` heading line while adding the prose text `See [P1-B] BODY` inside `EDIT`, and verify `python Blueprint/build.py --check` fails with `FATAL: route target missing: processes.body`.

## Passed lanes

* **Authority and scope:** Core separation between `BLUEPRINT.md`, generated `DEPLOY/`/`UPLOAD/` surfaces, and transport scripts is sound in `ARCHITECTURE.md` and `build.py`, **subject to** fixing the legacy 4-source instructions in `bootstrap/AGENTS.md` (High finding #2).


* **Reproducibility and portability:** `Blueprint/build.py` and `PORTABILITY/make_bundle.py` normalize CRLF to LF (`\n`), use case-folded POSIX path sorting, and write deterministic `ZIP_STORED` archives with fixed timestamps `(2026, 1, 1, 0, 0, 0)` and `0o100644` permissions. All 8 snapshot files in `PORTABILITY/snapshot/` match their exact SHA-256 digests in both `PORTABILITY/AUDIT-SNAPSHOT.json` and `PORTABILITY/MANIFEST.json`.


* **Publication safety:** `push.bat` enforces `GIT_PAGER=cat`, checks for unfinished merges/rebases, displays modified/untracked files and `COMMITS-PENDING.md`, and requires interactive `PUSH` confirmation, **subject to** the post-commit rebase and `wait_validation` fixes above.


* **Cloud distribution:** `distribute_blueprint.py` strictly uses `rclone copy` (never `rclone sync`), bounds destinations to the three approved remote paths (`pCloud:Public Folder/pipeline-registry/Blueprint`, `GDrive:pipeline-registry/Blueprint`, `onedrivebkp:pipeline-registry/Blueprint`), excludes `__pycache__` and `*.pyc`, and never stores credentials in the repo.


* **Recovery and maintainability:** `RECOVERY.md` and `RELEASE-RUNBOOK.md` prohibit destructive Git/rclone shortcuts (`git reset --hard`, `push --force`, `rclone sync`, unapproved `rclone dedupe` deletion), **subject to** aligning `COLD-REBUILD.md` with the files checked by `push.bat`.



## Uncertainties

* **Missing parent-workspace scripts not in the bundle:** `push.bat` references 12 parent-workspace files (`CONTROL.txt`, `BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md`, `DIRECTORY.yaml`, `BLUEPRINT.txt`, `sync_master.py`, `build.py`, `extract.py`, `seal.py`, `clear_pending.py`, and `Control\CONTROL.txt`) and executes `python "..\clear_pending.py"`. Because these files are not included in `PORTABILITY/snapshot/` or `BKPDE-Portability.zip`, their internal logic cannot be inspected from the supplied bundle alone.


* **Committed generated trees (`Blueprint/DEPLOY/`, `Blueprint/UPLOAD/`, `Bangkok_Post_Blueprint_*.docx`) and `COMMITS-PENDING.md`:** `AUDIT-SNAPSHOT.json` snapshots the 8 source/machinery files (`BLUEPRINT.md`, `build.py`, `build_human_volume.py`, `push.bat`, `bootstrap/AGENTS.md`, `bootstrap/shift.py`, `bootstrap/distribute_blueprint.py`, `.github/workflows/compile.yml`), not the pre-committed `Blueprint/DEPLOY/` or `.docx` outputs in the live repository worktree.
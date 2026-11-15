# Mechanism audit findings

Auditor/model: Claude Opus 5.5 (claude-opus-5-5)

Snapshot commit: 60e3c28b4db26d99aefb2d1cac064d2dac19b6b0

Date: 2026-11-15

## Executive verdict

**Fit for continued use with conditions.** Manifest integrity holds: all 22 files match `MANIFEST.json`, and all 8 snapshot files match `AUDIT-SNAPSHOT.json`. The build reproduces byte-for-byte across repeated runs and on Python 3.12 and 3.13. The ZIPs are deterministic. Destinations are exact and copy-only.

Three conditions should be resolved before the next distribution:

1. Cloud publication copies the working tree rather than the validated commit. Files that were never displayed, committed or validated can therefore reach the public pCloud folder, and verification still passes (F1).
2. A duplicated component block or stray text outside the component markers silently drops editorial content from the skills, and the build and CI still report success (F2).
3. `bootstrap/AGENTS.md`, the mechanics authority read second during a cold rebuild, describes a superseded source and build chain that contradicts `ARCHITECTURE.md` (F3).

Method: I verified the hashes, then executed `build.py` in a scratch copy on Python 3.11, 3.12 and 3.13. I reproduced failures with modified copies. A simulated `core.autocrlf=true` clone was tested. The proposed F2 correction was applied in scratch and proven against both the real source and the failure fixtures. rclone, `gh` and Windows `cmd` behaviour were not executed. Those findings rest on code reading plus the cited documentation and are marked as such.

## Findings

### [High] F1. Cloud publication copies the working tree, not the validated commit

- Confidence: High (code path); Medium (likelihood of a harmful file being present)
- Affected path: `snapshot/bootstrap/distribute_blueprint.py` L14, L21, L74–76; `snapshot/push.bat` L91, L218–228; `snapshot/Blueprint/build.py` L223
- Evidence: `SOURCE = ROOT / "pipeline-registry" / "Blueprint"` (L14) is a working directory. `rclone copy` and `rclone check` both read `str(SOURCE)` (L74, L76), and the only filters are `__pycache__` and `*.pyc` (L21). `--wait-validation` is tied to the commit (L57, L65), but `--publish` takes no commit and never checks `HEAD` or the cleanliness of the tree. The preflight lists only `git ls-files --others --exclude-standard` (push.bat L91), so **gitignored files are never displayed**. They are also never committed or seen by CI, but they are still copied. `build.py --check` creates its temp directory inside `Blueprint/` (L223), and that directory survives a hard kill or power loss.
- Reproduction or failure scenario: Put any file covered by `.gitignore` in `pipeline-registry/Blueprint/`, for example a local notes file, a Word owner file `~$ngkok_Post_Blueprint….docx` created while the volume is open, or a `tmpXXXX/` left by an interrupted `--check`. Run push.bat to `PUSH`. The preflight does not show the file, CI passes on the commit, and `--publish` copies the file to all three remotes. Destination 1 is `pCloud:Public Folder/…`. The one-way `rclone check` compares against the same polluted tree, so it reports `verified` and the script prints `distribution: PASS`.
- Operational consequence: The public mirror receives content that was never displayed or validated, and the system reports success. If a credential or a personal file is present, this is a disclosure (Critical class). Nothing in the snapshot shows that one is likely, so I have rated it High.
- Smallest proposed correction: Make `--publish` take the validated SHA, `--publish COMMIT`, and have push.bat pass `"%LH%"`. Before any rclone call, `publish()` should fail closed unless both of these hold:
  - `git rev-parse HEAD` equals `COMMIT`;
  - `git status --porcelain --ignored --untracked-files=all -- Blueprint` is empty, after dropping lines that match `__pycache__/` or `.pyc`.
- Compatibility/regression risk: An operator who deliberately keeps ignored files in `Blueprint/` will be blocked, which is the intended effect. `__pycache__` must stay filtered, or every run after a local build is blocked. A manual `--publish` with no SHA needs the new argument.
- Verification test: Fixture repo plus a stub `rclone` on `PATH` that logs its arguments. (a) Clean tree with HEAD equal to SHA: the stub is called 6 times. (b) Add an ignored `Blueprint/x.local`: FATAL, and the stub is never called. (c) HEAD differs from SHA: FATAL. (d) Only `Blueprint/__pycache__/a.pyc` present: passes.

### [High] F2. Duplicate component blocks and text outside markers silently drop editorial content

- Confidence: High (reproduced)
- Affected path: `snapshot/Blueprint/build.py` L18, L70–72; `snapshot/Blueprint/build_human_volume.py` L261
- Evidence: `parts = dict(PART_RE.findall(text))` (L70) keeps the **last** block when a component name repeats. `set(parts) != set(PARTS)` (L71) cannot see duplicates. Text between an `END COMPONENT` marker and the next `COMPONENT` marker matches no part and is discarded. The Word builder uses the same `dict(...)` pattern (L261). This breaks ARCHITECTURE L63, "exactly six recognised components".
- Reproduction or failure scenario: Both cases were reproduced in scratch copies.
  - (a) Append a second `<!-- COMPONENT: PR -->` block holding only front matter and a stub. `build.py` prints `built … 6 skills, 37 routes …`, and `DEPLOY/skills/pr/SKILL.md` drops to 8 lines ending in the stub. Because the committed outputs are generated from the same source, `--check` and CI then pass.
  - (b) Insert a line after `<!-- END COMPONENT: PR -->`. The build succeeds, and the line appears only in `BLUEPRINT.txt`, in no skill, ZIP or routed file.
- Operational consequence: A copy-paste or merge error replaces or drops a desk module. Every gate passes, and the wrong module is published to GitHub, Shift and all three clouds. The mechanism silently corrupts editorial content.
- Smallest proposed correction: In `load()`, replace L70–72 with:
  ```python
  found = PART_RE.findall(text)
  names = [name for name, _ in found]
  if sorted(names) != sorted(PARTS):
      raise SystemExit(f"FATAL: component inventory differs: {sorted(names)}")
  residue = PART_RE.sub("", text[text.index("<!-- COMPONENT: "):])
  if residue.strip():
      raise SystemExit("FATAL: text outside component markers")
  parts = dict(found)
  ```
  The preface before the first marker, which holds the title and the MASTER mark, stays legal. Apply the same inventory check in `build_human_volume.py`, or have it import `build.load`.
- Compatibility/regression risk: None for the current source. I proved this in scratch: with the patch, `DEPLOY/`, `UPLOAD/`, `BLUEPRINT.txt`, `DIRECTORY.yaml` and `build-receipt.json` are byte-identical to the unpatched build. The nested `<!-- COMPONENT: DIRECTORY -->` inside EDIT is consumed by the EDIT match and is unaffected.
- Verification test: With the patch, fixture (a) gives `FATAL: component inventory differs: [… 'PR', 'PR' …]` and fixture (b) gives `FATAL: text outside component markers`. Both outputs were observed. The unmodified source still builds and passes `--check`.

### [High] F3. The bootstrap mechanics authority describes a superseded source and build chain

- Confidence: High (contradiction); Medium (whether legacy files currently sit in `Blueprint/`)
- Affected path: `snapshot/bootstrap/AGENTS.md` L7, L14, L20–24, L42–54, L84–87; `snapshot/push.bat` L46, L98, L122–123, L135; `PORTABILITY/COLD-REBUILD.md` L20
- Evidence:
  - AGENTS.md, which "controls repository and handover mechanics" (L14) and is read second in a cold rebuild (COLD-REBUILD L20), says the editable authority is four root files: `BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md` and `DIRECTORY.yaml`. It says root `build.py` compiles them into `BLUEPRINT.txt`, which "controls editorial work" (L14, L20–24).
  - Step 4 (L51–54) tells the custodian to copy those sources and the compiled `BLUEPRINT.txt` into `pipeline-registry/Blueprint/`.
  - ARCHITECTURE L11–12 and L22 instead make `Blueprint/BLUEPRINT.md` the source and `Blueprint/build.py` the generator of `BLUEPRINT.txt` and `DIRECTORY.yaml` (build.py L182, L194).
  - push.bat L46 still hard-requires the four legacy root sources and root `build.py`, and L98/L135 mirror that second `build.py` to `bootstrap/build.py`.
  - AGENTS L7 starts the custodian at `00_START-HERE.md`, which is in neither the kit nor `bootstrap/`.
- Reproduction or failure scenario: A custodian following AGENTS.md edits root `GUIDE.md`, runs root `build.py` and copies the results into `Blueprint/`.
  - The copied `BLUEPRINT.txt` and `DIRECTORY.yaml` overwrite generated files, and `build.py --check` aborts. That part fails closed.
  - The edit never reaches `BLUEPRINT.md`. If the custodian then runs `build.py` to clear the error, the work is silently discarded.
  - The copied `BLUEPRINT.front.md`, `GUIDE.md` and `PROCESSES.md` are outside every check, because `compare_trees` covers only DEPLOY, UPLOAD and the compatibility files. They therefore ride the whole-tree cloud copy as apparent source files.
- Operational consequence: The authority chain is ambiguous, editorial work can be lost, and stale editorial sources can be published looking authoritative.
- Smallest proposed correction:
  - Rewrite AGENTS.md "Current architecture", "Safe build and publication" and "Generated and historical material" to match ARCHITECTURE.md. Name `Blueprint/BLUEPRINT.md` as the single source, `Blueprint/build.py` as the generator, and `BLUEPRINT.txt`, `DIRECTORY.*`, `GUIDE.txt` and `PROCESSES.txt` as generated.
  - Point L7 at `PORTABILITY/README.md`.
  - Drop the legacy names from push.bat L46 that the current route never reads: `BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md`, `DIRECTORY.yaml`, `BLUEPRINT.txt`, and root `build.py` unless it still has a current role.
  - This is an administrative change, not an editorial one.
- Compatibility/regression risk: If Control, seal or sync workflows that are not in the snapshot still read the root legacy files, removing the presence check does not break them, because nothing is deleted. Confirm root `build.py`'s role before removing it from the mirror list.
- Verification test:
  - A doc-consistency check that fails if AGENTS.md names a source file ARCHITECTURE.md lists as generated.
  - `git ls-files Blueprint | grep -E 'BLUEPRINT\.front\.md|/GUIDE\.md|/PROCESSES\.md'` returns nothing, or the files are deliberately excluded from the cloud copy.
  - A fresh workspace laid out exactly per COLD-REBUILD §2 reaches push.bat's PUSH prompt.

### [Medium] F4. The preflight does not display commits that are already made but not yet pushed

- Confidence: High
- Affected path: `snapshot/push.bat` L84–91, L163–166, L188–190
- Evidence:
  - The payload shown is `status --short --branch`, `diff --stat`, `diff --name-status` and untracked files: worktree state only.
  - L163–166 explicitly handles "nothing to commit … Checking whether local is ahead of origin anyway" and then pushes.
  - L190 tells the operator `git rebase --abort` after a conflict. That leaves the run's commit local.
  - L109 says typing PUSH authorises "the exact displayed payload".
- Reproduction or failure scenario: Run 1 commits, the rebase conflicts, and the operator aborts as instructed. Run 2's preflight shows a clean tree, and `## main...origin/main [ahead 1]` is the only hint. PUSH then publishes a commit whose content was never displayed. The same applies to any manual local commit.
- Operational consequence: The PUSH gate authorises a payload it did not show (audit question C).
- Smallest proposed correction: After L52 (`git fetch origin`), add a read-only section showing commits that are local only, plus staged changes, because `git diff` omits the index:
  ```bat
  echo --- local commits not yet on origin ---
  git --no-pager log --stat --format="%%h %%s" origin/main..HEAD
  echo --- already staged ---
  git -c core.safecrlf=false --no-pager diff --cached --name-status
  ```
- Compatibility/regression risk: None; display only.
- Verification test: Fixture clone with one local commit touching `Blueprint/BLUEPRINT.md` and a clean tree. Run push.bat to the prompt and press Enter. The captured output must list that commit and its file.

### [Medium] F5. Cloud verification is blind to Google Drive duplicates and never reports stale remote extras

- Confidence: High (code); Medium (exact rclone listing behaviour, to be confirmed by the test)
- Affected path: `snapshot/bootstrap/distribute_blueprint.py` L74–78; `PORTABILITY/RELEASE-RUNBOOK.md` L44–46
- Evidence:
  - Verification is only `rclone check SOURCE DEST --one-way` (L76). With `--one-way`, files present only on the remote are not examined.
  - On Google Drive, rclone logs duplicate destination names as a `NOTICE: … Duplicate object found in destination - ignoring` and continues ([rclone forum](https://forum.rclone.org/t/duplicate-object-found-in-destination-ignoring/22133)), so the exit status stays 0.
  - The runbook says "A duplicate warning is not normal success" (L44–45), yet the script prints `verified` and `distribution: PASS`, and the NOTICE scrolls past in an uncaptured console.
- Reproduction or failure scenario:
  - (a) Upload a second copy of `DEPLOY/routed/BOOT.md` into the GDrive folder through the web UI. `--publish` passes, and a consumer opening the folder may get either copy.
  - (b) A file renamed or removed from `Blueprint/`, such as an old-edition DOCX or a retired routed module, stays at all three destinations indefinitely and is never reported.
- Operational consequence: Audit question D, "detect … duplicate objects", fails. Obsolete files remain in public and shared mirrors, look authoritative, and nobody is told. Copy-only behaviour itself is correct and should stay.
- Smallest proposed correction: After each `check`, list the destination once read-only with `rclone lsf -R --files-only DEST` plus the filters, and compare it in Python with the local file list. Repeated paths cause FATAL. Paths present only on the remote are printed as `remote extras (not deleted): …` and do not fail the run. No deletion is introduced.
- Compatibility/regression risk: One extra listing per destination, on a small tree. There are no semantic changes to copying.
- Verification test:
  - Unit: a stub `rclone lsf` emitting a repeated line must cause FATAL; an extra line must be reported with exit 0.
  - Live: create a duplicate in a GDrive test path. `--publish` must fail and name it. Then confirm that `rclone lsf` lists both duplicates on the installed rclone version.

### [Medium] F6. The Word volume's edition identity is hardcoded and never verified

- Confidence: High
- Affected path: `snapshot/Blueprint/build_human_volume.py` L17, L270, L289; `snapshot/bootstrap/shift.py` L28; `PORTABILITY/ARCHITECTURE.md` L62
- Evidence:
  - The edition `151126_gpt_modular-routes` is a literal in the builder's output filename, its metadata comment and its footer. It is not read from the `<!-- MASTER … -->` mark.
  - shift.py hardcodes the same source filename and publishes it as `Bangkok_Post_Blueprint.docx`.
  - `build.py`, CI (compile.yml L34–35) and `shift.py --check` (hash copy only) never compare the DOCX with `VERSION.txt`, so ARCHITECTURE's "Edition identity matches across the complete generated set" is not enforced for the DOCX.
- Reproduction or failure scenario: The next edition changes the MASTER mark in `BLUEPRINT.md`, and the builder literals are not edited.
  - (a) If the builder is not rerun, Shift ships the previous edition's volume under the generic name, and `shift.py --check` passes.
  - (b) If it is rerun, the new content is footer-labelled with the old edition and overwrites the old-named file.
- Operational consequence: A wrong-edition reading volume reaches Shift and all three clouds while the run reports success. Skill payloads are unaffected, which is why this is rated Medium rather than High.
- Smallest proposed correction:
  - In the builder, derive `version` with build.py's `VERSION_RE` and use it for `OUTPUT`, the comment and the footer.
  - In shift.py, derive the DOCX source name from `VERSION.txt`: `f"Bangkok_Post_Blueprint_{version}.docx"`.
- Compatibility/regression risk: There is no change for the current edition, because the derived name equals the current literal. Future editions require the volume to be rebuilt, which is the intended effect.
- Verification test: In a fixture, change the MASTER mark and rebuild text outputs only. `shift.py` must report `missing source: …Bangkok_Post_Blueprint_<new>.docx` instead of shipping the old file.

### [Medium] F7. Python ≥3.12 is required but undeclared, and versions are unpinned in CI

- Confidence: High (reproduced)
- Affected path: `snapshot/Blueprint/build.py` L40; `snapshot/bootstrap/shift.py` L42; `PORTABILITY/DEPENDENCIES.md` L7; `snapshot/.github/workflows/compile.yml` L13–18
- Evidence:
  - `shutil.rmtree(..., onexc=...)` only exists from Python 3.12. DEPENDENCIES says only "Python 3".
  - CI uses `ubuntu-latest` system Python and runs `pip install PyYAML` unpinned. The byte comparison depends on PyYAML's `safe_dump` formatting.
- Reproduction or failure scenario: Observed. On Python 3.11, `build.py --check` prints PASS, because the temp tree has no existing DEPLOY to remove. The next plain `build.py` fails with `TypeError: rmtree() got an unexpected keyword argument 'onexc'`. `shift.py` fails the same way once `Shift/` exists. Cold-rebuild step 4 therefore passes on a machine that cannot regenerate.
- Operational consequence: Cold recovery fails on a plausible Windows Python install, after the acceptance check has already said PASS. A future PyYAML formatting change would fail CI against committed outputs. That fails closed but blocks publication.
- Smallest proposed correction:
  - DEPENDENCIES: "Python 3.12 or later; PyYAML 6.0.x".
  - Add `if sys.version_info < (3, 12): raise SystemExit("FATAL: Python 3.12+ required")` to build.py and shift.py.
  - CI: use `actions/setup-python@v5` with `python-version: "3.12"` and `pip install "PyYAML==6.0.*"`.
- Compatibility/regression risk: None for current outputs. They were byte-identical under 3.12 and 3.13 with PyYAML 6.0.3 in this audit.
- Verification test: `python3.11 build.py --check` exits with the version message. CI green on the pinned job.

### [Medium] F8. Byte-exact checks depend on line-ending settings the kit neither supplies nor documents

- Confidence: Medium (the live repo may contain a `.gitattributes` the snapshot omits)
- Affected path: `snapshot/Blueprint/build.py` L32, L218, L229; `PORTABILITY/COLD-REBUILD.md` §1; `PORTABILITY/make_bundle.py` L18–23 (no `.gitattributes` in SNAPSHOT)
- Evidence: Generated text is written as LF and compared byte-for-byte with the checked-out files. Git for Windows commonly defaults to `core.autocrlf=true`. The cold-rebuild clone command sets no line-ending policy.
- Reproduction or failure scenario: Simulated. Committing the built tree with `autocrlf=false`, then cloning with `git -c core.autocrlf=true clone` gives CRLF checkouts, and `build.py --check` fails with `FATAL: generated file differs: DIRECTORY.txt`.
- Operational consequence: Cold rebuild on a default Windows Git fails at step 4 and contradicts ARCHITECTURE L68. It fails closed.
- Smallest proposed correction: If the repo already has a `.gitattributes` that marks `Blueprint/**` `-text` or `eol=lf`, add it to `make_bundle.py` SNAPSHOT so it is auditable. Otherwise add one with `Blueprint/** -text`, or change the clone command to `git clone -c core.autocrlf=false …`.
- Compatibility/regression risk: Adding `.gitattributes` can show a one-time renormalisation diff. Run `git add --renormalize .` in an isolated candidate first.
- Verification test: Clone with `git -c core.autocrlf=true clone …`, then run `python build.py --check --release`. It must pass.

### [Medium] F9. The cold-rebuild path cannot reach publication

- Confidence: High
- Affected path: `snapshot/push.bat` L46, L98, L128–129, L135, L152; `PORTABILITY/COLD-REBUILD.md` L31–46
- Evidence:
  - push.bat aborts unless all 14 files at L46 exist in the parent directory.
  - COLD-REBUILD §2 lists only `AGENTS.md`, `shift.py` and `distribute_blueprint.py`, and adds the other scripts "only if their workflows are needed".
  - Six required files are mirrored nowhere in `bootstrap/` (L98/L135), and no document says where to restore them from: `CONTROL.txt`, `BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md`, `DIRECTORY.yaml` and `BLUEPRINT.txt`.
  - The in-script restore note says "copy the three files" (L128–129), but eight are mirrored.
  - `clear_pending.py` runs unconditionally after PUSH (L152).
- Reproduction or failure scenario: Follow COLD-REBUILD §1–4 exactly, then run push.bat. It stops with `[ABORT] required workspace file missing: ..\CONTROL.txt`.
- Operational consequence: The documented cold path ends at a dead gate, and the operator must improvise which files to supply.
- Smallest proposed correction: After F3 trims L46, make COLD-REBUILD §2 list exactly the files L46 still requires, with each one's restore source. For example, `CONTROL.txt` comes from `Control/CONTROL.txt`, which L58 requires to be byte-equal anyway, and the scripts come from `bootstrap/`. Correct L128–129 to "the mirrored files".
- Compatibility/regression risk: Documentation only.
- Verification test: In an empty workspace, follow COLD-REBUILD literally. push.bat must reach the PUSH prompt without manual additions.

### [Low] F10. The rebase step neither revalidates nor gives current conflict guidance

- Confidence: High (guidance); Medium (likelihood of a clean but invalid merge)
- Affected path: `snapshot/push.bat` L183–197, L187–188; `snapshot/.github/workflows/compile.yml` L20–27
- Evidence:
  - After `git rebase origin/main`, push.bat pushes without rerunning `build.py --check`.
  - The conflict text says derived files "are regenerated by CI - if the conflict is one of those, take origin's copy". CI no longer regenerates anything (compile.yml validates only, and push.bat L173–174 itself says so), and RECOVERY L61 forbids hand edits to generated files.
- Reproduction or failure scenario: A remote commit changes `build.py` output, and the local commit changes only the source. The rebase is clean, and the pushed commit is invalid. It is live on `main`, and on the raw link push.bat L240 uses for verification, until a corrective push. CI does catch it, and distribution stops.
- Operational consequence: A known-bad commit can reach main. The conflict guidance points operators at hand-resolving generated files.
- Smallest proposed correction: Between L193 and L196, add `python Blueprint\build.py --check || (echo [ABORT] post-rebase build differs - regenerate, nothing pushed & pause & exit /b 1)`. Replace L187–188 with "Regenerate with `python Blueprint\build.py`; never take either side of a generated file by hand."
- Compatibility/regression risk: A few seconds per push. A failure leaves a local commit, which F4 then makes visible.
- Verification test: In a fixture, the origin commit alters `build.py` output and the local commit edits the source. push.bat must abort before `git push`.

### [Low] F11. `--release` does nothing, and the claimed skill validator does not exist

- Confidence: High
- Affected path: `snapshot/Blueprint/build.py` L54–58, L237; `PORTABILITY/ARCHITECTURE.md` L67; `PORTABILITY/RELEASE-RUNBOOK.md` L13
- Evidence:
  - `--release` is parsed and never read; its help text says "run release validation".
  - ARCHITECTURE says "Every generated skill passes the skill validator", and the runbook says "Validate all six skill folders".
  - The only skill check is that a `name:` line exists and matches.
- Reproduction or failure scenario: A `description:` over 1,024 characters or containing `<` builds and passes CI, then fails at install time. The current set does not fail: descriptions are 170–328 characters with no angle brackets.
- Operational consequence: Docs, CI and push.bat all invoke `--release` as if it were a gate, which gives false assurance.
- Smallest proposed correction: Under `--release`, check each part's front matter. `name` must match `^[a-z0-9-]{1,64}$` and equal the folder name; `description` must be present, 1,024 characters or fewer, and free of `<` and `>`. Otherwise delete the ARCHITECTURE and runbook claims. These limits are Claude-skill-format specific, so label them as such.
- Compatibility/regression risk: None for the current set.
- Verification test: A fixture with a 1,025-character description fails under `--release` and passes without it.

### [Low] F12. push.bat deletes `.git\index.lock` automatically

- Confidence: Medium
- Affected path: `snapshot/push.bat` L23–33; `PORTABILITY/RECOVERY.md` L5
- Evidence: The lock is deleted whenever `tasklist` shows no `git.exe`. This happens before the "PRE-FLIGHT - NOTHING HAS BEEN STAGED" banner. Clients that do not run `git.exe`, such as libgit2-based tools or WSL git, are invisible to that test. RECOVERY says "Do not repair by deleting".
- Reproduction or failure scenario: An IDE's libgit2 integration holds the lock while it writes the index. push.bat deletes the lock, and both processes then write the index.
- Operational consequence: The index can be corrupted, and the preflight is not actually read-only.
- Smallest proposed correction: Replace the delete with an abort that names the lock path and tells the operator to remove it manually after closing git clients.
- Compatibility/regression risk: Operators with a genuinely stale lock make one manual deletion.
- Verification test: Create `.git\index.lock` and run push.bat. It must abort, and the file must remain.

### [Low] F13. Branch and worktree assumptions, plus success exit codes on failed verification

- Confidence: Medium (Windows `cmd` behaviour reasoned, not executed)
- Affected path: `snapshot/push.bat` L14, L38–45, L183, L197, L208–236; `snapshot/bootstrap/distribute_blueprint.py` L51
- Evidence:
  - The current branch is never checked against `main`.
  - In a linked worktree, `.git` is a file, so `.git\MERGE_HEAD` and `.git\rebase-merge` are never found, and the unfinished-merge and unfinished-rebase guards are silently disabled. The runbook recommends isolated candidates, which makes this case plausible.
  - The origin-mismatch branch (L233–236) falls through to a 0 exit.
  - If both `rev-parse` temp files were empty, `"%LH%"=="%RH%"` would compare `""==""` as true.
  - `--wait-validation` accepts any string.
- Reproduction or failure scenario: Run push.bat in a candidate branch that has an upstream. It rebases onto main and pushes to `origin/<candidate>`, prints the WARNING and exits 0.
- Operational consequence: The push lands in the wrong place, and any wrapper or log records success.
- Smallest proposed correction:
  - Abort unless `git rev-parse --abbrev-ref HEAD` is `main`.
  - Use `git rev-parse --git-path MERGE_HEAD` and `--git-path rebase-merge` for the guards.
  - End the mismatch branch with `exit /b 1`.
  - Require `%LH%` to be non-empty.
  - Validate `^[0-9a-f]{40}$` in `wait_validation`.
- Compatibility/regression risk: None on the normal main-branch path.
- Verification test: (a) Running from a `candidate` branch aborts before staging. (b) A linked worktree with an unfinished merge aborts. (c) A forced mismatch exits non-zero.

### [Low] F14. No persistent evidence of publication or distribution

- Confidence: High
- Affected path: `snapshot/push.bat` (console only); `snapshot/bootstrap/distribute_blueprint.py` L66, L77–78; `PORTABILITY/RELEASE-RUNBOOK.md` "Confirmation record"
- Evidence: The runbook requires the SHA, the GitHub run URL, the Shift result, and per-destination counts with a zero-difference result. The scripts print only a run ID, and rclone summaries go to the console. Nothing is written to disk, and the record is lost when the window closes.
- Reproduction or failure scenario: After any run, the confirmation record cannot be reconstructed without rerunning commands.
- Operational consequence: Audit question E, whether logs are sufficient to prove publication and distribution, fails.
- Smallest proposed correction: Have `distribute_blueprint.py` append one JSON line per stage to `ROOT/logs/distribution.jsonl`, which is outside `Blueprint/` so it is never distributed. Record the timestamp, commit, `gh run view <id> --json url,conclusion`, and each destination's check result plus F5's extras and duplicates.
- Compatibility/regression risk: A new local directory, which is not tracked.
- Verification test: After a stubbed run, the log holds exactly one record per stage with the SHA and three destination results.

## Passed lanes

- **Authority and scope.** Generated DEPLOY, UPLOAD and compatibility files are protected from hand editing by the `--check` byte comparison in push.bat and CI. Supervisor gating (the PUSH prompt) and the Control parity guard work as described. Lane fails on F2 and F3.
- **Reproducibility and portability.** Output is byte-identical across repeated builds and across Python 3.12 and 3.13. ZIP timestamps, permissions and member order are fixed. DEPLOY sorting uses casefold and POSIX paths. CRLF and BOM input is normalised. Lane is conditional on F7 and F8.
- **Publication safety.** The preflight runs before any staging or mirroring. Fetch failure stops cleanly. Rebase conflicts are never auto-resolved. Local HEAD is compared with `origin/main` after the push. GitHub validation is bound to the pushed SHA (`gh run list --commit`). Each post-push stage stops on failure, and a rerun is safe. Lane fails on F1 and F4.
- **Cloud distribution.** Destinations are exact literals, and the source path is fixed. `rclone copy` is used and never `sync`. A retry is idempotent. Credentials never pass through the scripts, and no secrets were found in the snapshot. Expired authorisation fails closed at `lsd` or the copy. Lane fails on F1 and F5.
- **Recovery and maintainability.** RECOVERY prohibits reset, force-push and deleting dedupe. The cold path from GitHub plus this kit is mostly documented. Lane fails on F9; F3 and F10 leave obsolete routes in place.

## Uncertainties

- Files the mechanism executes are absent from the snapshot, so these were not audited:
  - `clear_pending.py`, which mutates the payload after PUSH (push.bat L152);
  - `sync_master.py`, `seal.py`, `extract.py` and root `build.py`;
  - `.gitignore`, `.gitattributes` and `Control/`.
  
  F1's likelihood, F3's live exposure and F8 depend on them.
- Whether `BLUEPRINT.front.md`, `GUIDE.md`, `PROCESSES.md` or old-edition DOCX files currently exist in `pipeline-registry/Blueprint/` or in the remotes cannot be established from the snapshot.
- Not executed: rclone (duplicate listing behaviour in F5), `gh` (including behaviour with an empty `--commit`), Windows `cmd` semantics and the GitHub runner image. Whether `pip install` on `ubuntu-latest` system Python is permitted (PEP 668) is assumed from the commit evidently passing CI.
- Integrity is SHA-256 against `MANIFEST.json`, which is unsigned. It detects accidental change, not deliberate substitution of the whole kit. This is an observation, not a finding.
- Observation: `distribute_blueprint.py` L2 says "two approved cloud mirrors" against three destinations, and push.bat L122–123 still refers to the old compile job "treating them as components". Both are stale comments with no behavioural effect beyond those already covered in F3 and F9.
- Observation: the CI step `git diff --exit-code -- Blueprint` (compile.yml L27) is redundant after `--check`, which writes nothing outside its temp directory, and it cannot detect untracked files. It is harmless.

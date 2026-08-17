@echo off
setlocal
REM --- find the repo ----------------------------------------------------------
REM This script lives IN the clone, so the clone is wherever this script is.
REM %~dp0 is that folder, with a trailing backslash, drive included. Resolving it
REM this way means the folder can be moved, renamed or put on another drive and
REM the script still works. It used to hold a hardcoded D:\ path; the folder moved
REM to C:\Users and every run exited here before reaching git.
cd /d "%~dp0" || (echo [ERROR] could not enter "%~dp0" & pause & exit /b 1)
if not exist ".git" (
  echo [ERROR] no .git here - this script is not sitting in the clone.
  echo         Looked in: "%~dp0"
  echo         Put push.bat back in the pipeline-registry folder and re-run.
  pause & exit /b 1
)
echo [ok] repo: %cd%

REM --- clear a STALE lock, but only if no git process is running ---
if exist ".git\index.lock" (
  tasklist /fi "imagename eq git.exe" 2>nul | find /i "git.exe" >nul
  if errorlevel 1 (
    echo [info] stale index.lock found, no git running - removing it
    del ".git\index.lock"
  ) else (
    echo [ABORT] git is currently running. Not touching the lock.
    echo         Close other git/terminals, then re-run.
    pause & exit /b 1
  )
)

REM --- mirror the bootstrap set into the clone so the push backs it up -------
REM These three live at the Project_Space root and are NOT part of the published
REM volume. CLAUDE.md must sit at the root to be read on entry, and none of them
REM may go in Blueprint\ or the compile job would treat them as components. That
REM leaves them on one machine, unbacked. This mirrors them into bootstrap\ so
REM they ride every push.
REM
REM ONE DIRECTION ONLY: root -> clone, overwriting. The root copy is the source;
REM the clone copy is a backup and is never edited. To restore, copy the three
REM files from bootstrap\ up into Project_Space.
echo.
echo === mirroring bootstrap set ===
if not exist "bootstrap" mkdir "bootstrap"
REM 100826: seal.py and clear_pending.py added. push.bat CALLS both, so a repo
REM that does not hold them carries a push script it cannot run after a restore.
for %%F in (CLAUDE.md shift.py build.py seal.py clear_pending.py CANDIDATE_ONLY.md 130826_candidate-breakpoints.md 130826_candidate-remaining-failures.md) do (
  if exist "..\%%F" (
    copy /Y "..\%%F" "bootstrap\%%F" >nul
    echo   mirrored %%F
  ) else (
    echo   [WARN] ..\%%F not found - NOT mirrored
  )
)

REM --- clear the pending list INTO the commit that carries the work -----------
REM The protocol says lines clear on the push, in the same commit. Nothing did
REM it, so the list filled at session rate and never emptied - 71 entries back
REM to 4 July when this was found on 100826. Every line still pending at this
REM point is by definition about to be pushed, so nothing needs judging: the
REM whole block moves to COMMITS-ARCHIVE.md and rides the same commit.
echo.
echo === clearing the pending list ===
python "..\clear_pending.py"
if errorlevel 1 (
  echo [FAIL] could not clear COMMITS-PENDING.md. Nothing staged, nothing pushed.
  pause & exit /b 1
)

echo.
echo === staging changes ===
git add -A || (echo [FAIL] git add failed & pause & exit /b 1)

REM --- commit; capture whether there was anything to commit ---
git diff --cached --quiet
if %errorlevel%==0 (
  echo [info] nothing to commit - working tree already matches last commit.
  echo        Checking whether local is ahead of origin anyway...
) else (
  git commit -m "update register" || (echo [FAIL] commit failed & pause & exit /b 1)
  echo [ok] commit created.
)

REM --- integrate the compile-bot's commits BEFORE pushing ---------------------
REM compile.yml derives GUIDE/DIRECTORY/docx/manifest and commits them to main on
REM every build, so the clone is behind after every build it triggers. Pushing
REM without integrating that is rejected as a non-fast-forward, which is what
REM happened on 090826. Rebase keeps the desk's commit on top of the bot's.
REM
REM A conflict here is NOT auto-resolved. Derived files are the likely site and
REM taking the wrong side by hand is exactly what the CI hand-edit guard exists
REM to catch. Abort and let a human look.
echo.
echo === integrating remote work ===
git fetch origin || (echo [FAIL] fetch failed & pause & exit /b 1)
git rebase origin/main
if errorlevel 1 (
  echo.
  echo [ABORT] rebase hit a conflict. Nothing has been pushed.
  echo         Derived files ^(Blueprint\GUIDE.txt, DIRECTORY.*^) are regenerated
  echo         by CI - if the conflict is one of those, take origin's copy.
  echo         Resolve, then re-run this script. To back out entirely:
  echo             git rebase --abort
  pause & exit /b 1
)
echo [ok] local is on top of origin/main.

echo.
echo === pushing ===
git push
if errorlevel 1 (
  echo.
  echo [FAIL] push did NOT succeed. Nothing was published. Read the error above.
  pause & exit /b 1
)

echo.
echo === verifying against origin ===
git fetch origin >nul 2>&1
git status -sb
git rev-parse --short HEAD > "%temp%\_lh.txt"
git rev-parse --short origin/main > "%temp%\_rh.txt"
set /p LH=<"%temp%\_lh.txt"
set /p RH=<"%temp%\_rh.txt"

echo.
if "%LH%"=="%RH%" (
  echo [CONFIRMED] local %LH% == origin/main %RH%.  Push is genuinely live.
  echo.
  echo === sealing the edition ===
  REM The Word volume is built by the compile job, not locally. seal.py waits
  REM for compile-bot to commit, rebases onto it, checks the volume carries this
  REM build's tag, and copies the edition into Editions\<tag>\. Ctrl+C is safe -
  REM the push is already done and seal.py can be re-run at any time.
  python "..\seal.py"
  if errorlevel 1 (
    echo.
    echo [note] edition not sealed. The push itself is fine and live.
    echo        Re-run:  python seal.py
  )
) else (
  echo [WARNING] local %LH% does NOT match origin/main %RH%.
  echo           Do not assume it published. Investigate before trusting.
)
echo.
echo (Verify with a cache-buster on the raw link - a bare fetch can return a)
echo (body from a superseded commit with no error. Trap 1.)
echo (raw.githubusercontent.com/cliffspab/pipeline-registry/main/Blueprint/GUIDE.txt?cb=1)
pause
endlocal

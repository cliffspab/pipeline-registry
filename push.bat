@echo off
setlocal
cd /d "D:\Documents\BANGKOK POST DESK EDITOR\Project_Space\pipeline-registry" || (echo [ERROR] repo folder not found & pause & exit /b 1)

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
for %%F in (CLAUDE.md shift.py build.py) do (
  if exist "..\%%F" (
    copy /Y "..\%%F" "bootstrap\%%F" >nul
    echo   mirrored %%F
  ) else (
    echo   [WARN] ..\%%F not found - NOT mirrored
  )
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
REM compile.yml derives CORE/REGISTER/docx/manifest and commits them to main on
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
  echo         Derived files ^(Blueprint\CORE.txt, REGISTER.*^) are regenerated
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
) else (
  echo [WARNING] local %LH% does NOT match origin/main %RH%.
  echo           Do not assume it published. Investigate before trusting.
)
echo.
echo (Verify the actual content at go.fuzzylogic.page/pro before relying on it.)
pause
endlocal

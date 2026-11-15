@echo off
setlocal EnableExtensions
set "GIT_PAGER=cat"
set "PAGER=cat"
cd /d "%~dp0" || exit /b 1

if not exist ".git" (
  echo [ABORT] push.bat must remain in the pipeline-registry clone.
  pause & exit /b 1
)
if exist ".git\index.lock" (
  echo [ABORT] .git\index.lock exists. No file was removed.
  echo         Close Git clients and confirm the lock is stale before removing it.
  pause & exit /b 1
)
if exist ".git\MERGE_HEAD" (
  echo [ABORT] unfinished merge detected.
  pause & exit /b 1
)
if exist ".git\rebase-merge" (
  echo [ABORT] unfinished rebase detected.
  pause & exit /b 1
)
for %%F in (Blueprint\BLUEPRINT.md Blueprint\build.py Blueprint\build_human_volume.py bootstrap\clear_pending.py bootstrap\distribute_blueprint.py COMMITS-PENDING.md) do (
  if not exist "%%F" (
    echo [ABORT] required file missing: %%F
    pause & exit /b 1
  )
)

for /f "delims=" %%B in ('git branch --show-current') do set "BRANCH=%%B"
if /I not "%BRANCH%"=="main" (
  echo [ABORT] current branch is %BRANCH%; guarded publication requires main.
  pause & exit /b 1
)

echo [preflight] checking source, dependencies and publication boundary...
git fetch origin || (echo [ABORT] fetch failed. & pause & exit /b 1)
for /f "tokens=1,2" %%A in ('git rev-list --left-right --count origin/main...HEAD') do (
  set "BEHIND=%%A"
  set "AHEAD=%%B"
)
if not "%BEHIND%"=="0" (
  echo [ABORT] local main is behind origin/main by %BEHIND% commit^(s^).
  echo         Integrate and validate that work separately, then rerun.
  pause & exit /b 1
)
git -c core.safecrlf=false --no-pager diff --check || (
  echo [ABORT] whitespace/error check failed.
  pause & exit /b 1
)
python Blueprint\build.py --check --release || (
  echo [ABORT] generated Blueprint files are stale or invalid.
  pause & exit /b 1
)
python Blueprint\build_human_volume.py --check || (
  echo [ABORT] Word reading volume is stale or invalid.
  pause & exit /b 1
)
python bootstrap\clear_pending.py --check || (
  echo [ABORT] pending record cannot be archived safely.
  pause & exit /b 1
)
python bootstrap\distribute_blueprint.py --preflight || (
  echo [ABORT] cloud distribution is not ready.
  pause & exit /b 1
)

echo.
echo === PRE-FLIGHT - NOTHING HAS BEEN STAGED ===
git --no-pager status --short --branch
echo.
echo --- unstaged changes ---
git -c core.safecrlf=false --no-pager diff --name-status
echo.
echo --- staged changes ---
git -c core.safecrlf=false --no-pager diff --cached --name-status
echo.
echo --- local commits not yet on origin/main: %AHEAD% ---
git --no-pager log --stat --oneline origin/main..HEAD
echo.
echo --- untracked files ---
git ls-files --others --exclude-standard
echo.
echo --- pending record ---
type COMMITS-PENDING.md
echo.
echo Typing PUSH authorises exactly the displayed payload. The script will
echo commit, push, wait for GitHub validation, copy the validated commit to
echo pCloud, Google Drive and OneDrive, back up the portability kit, verify
echo every destination and write a local receipt.
set "BKP_CONFIRM="
set /p "BKP_CONFIRM=Type PUSH to continue, or press Enter to stop: "
if /I not "%BKP_CONFIRM%"=="PUSH" (
  echo [STOPPED] preflight only. Nothing changed.
  exit /b 0
)

python bootstrap\clear_pending.py || (
  echo [FAIL] pending record could not be archived. Nothing staged.
  pause & exit /b 1
)
git add -A || (echo [FAIL] staging failed. & pause & exit /b 1)
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "harden Blueprint publication mechanism" || (
    echo [FAIL] commit failed. Nothing pushed.
    pause & exit /b 1
  )
) else (
  echo [info] no new commit required; publishing existing local commit^(s^).
)

REM Fail closed if upstream changed after preflight. Never rebase an unvalidated tree.
git fetch origin || (echo [FAIL] final fetch failed. Nothing pushed. & pause & exit /b 1)
for /f "tokens=1,2" %%A in ('git rev-list --left-right --count origin/main...HEAD') do (
  set "BEHIND=%%A"
  set "AHEAD=%%B"
)
if not "%BEHIND%"=="0" (
  echo [ABORT] origin/main advanced after preflight. Nothing pushed.
  echo         Re-run the full validation after integrating upstream work.
  pause & exit /b 1
)

git push || (echo [FAIL] push failed. & pause & exit /b 1)
git fetch origin >nul 2>&1
for /f "delims=" %%C in ('git rev-parse HEAD') do set "LH=%%C"
for /f "delims=" %%C in ('git rev-parse origin/main') do set "RH=%%C"
if /I not "%LH%"=="%RH%" (
  echo [FAIL] local HEAD does not equal origin/main after push.
  pause & exit /b 1
)

python bootstrap\distribute_blueprint.py --wait-validation "%LH%" || (
  echo [FAIL] GitHub validation did not pass. Cloud publication stopped.
  pause & exit /b 1
)
python bootstrap\distribute_blueprint.py --publish "%LH%" || (
  echo [FAIL] GitHub is current, but cloud distribution failed.
  pause & exit /b 1
)

echo [PASS] %LH% validated and distributed to all three mirrors.
echo        Receipt: .publication\last.json
pause
exit /b 0

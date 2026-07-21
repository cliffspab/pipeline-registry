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

@echo off
cd /d D:\Documents\pipeline-registry

git add .
git commit -m "update blueprint"
git push

echo.
echo ✅ Pushed to GitHub
pause
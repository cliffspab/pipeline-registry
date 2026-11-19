# Cold rebuild

1. Restore Git, Node.js and Python.
2. Clone `https://github.com/cliffspab/pipeline-registry.git`.
3. Read `PORTABILITY/README.md`, `bootstrap/00_START-HERE.md` and
   `bootstrap/AGENTS.md`.
4. Exercise the assembler across every output and deployment, and run
   `node --check Blueprint/assemble.js` and `node --check "DC-X Desk
   Hub.user.js"`.
5. Confirm GitHub Pages uses **GitHub Actions** and that the latest workflow is
   green.
6. Confirm `live/EDITION.txt`, `live/blueprint.md`, the six skills,
   `live/directory.md`, `live/DIRECTORY.txt` and `live/DIRECTORY.yaml` open.
7. Confirm the hosted path `Blueprint/MASTER.md` does not open.

GitHub supplies the content for the selected commit. If process machinery is
damaged, extract `BKPDE-Portability.zip` at the repository root and review the
result before committing a repair. The ZIP contains no master or generated
desk content. Credentials and browser sessions must be restored separately.

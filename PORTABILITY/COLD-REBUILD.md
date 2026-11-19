# Cold rebuild

1. Restore Git, Node.js and Python.
2. Clone `https://github.com/cliffspab/pipeline-registry.git`.
3. Read `PORTABILITY/README.md`, `bootstrap/00_START-HERE.md` and
   `bootstrap/AGENTS.md`.
4. Run `python PORTABILITY/verify_portability.py --live`.
5. Exercise the assembler across every output and deployment, and run
   `node --check Blueprint/assemble.js` and `node --check "DC-X Desk
   Hub.user.js"`.
6. Confirm GitHub Pages uses **GitHub Actions** and that the latest workflow is
   green.
7. Confirm `live/EDITION.txt`, `live/blueprint.md`, the six skills,
   `live/directory.md`, `live/DIRECTORY.txt` and `live/DIRECTORY.yaml` open.
8. Confirm the hosted path `Blueprint/MASTER.md` does not open.

For an independent comparison, extract `BKPDE-Portability.zip` and compare its
`PORTABILITY/snapshot/` files with the clone. Credentials and browser sessions
must be restored separately.

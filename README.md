# Bangkok Post Desk Editor

The durable entry point for the supervisor and the desk assistant is
[`bootstrap/00_START-HERE.md`](bootstrap/00_START-HERE.md). It explains which
files to use and how a fresh assistant establishes live state without an old
chat.

- Codex/project mechanics: [`bootstrap/AGENTS.md`](bootstrap/AGENTS.md)
- Claude project instructions: [`bootstrap/CLAUDE.md`](bootstrap/CLAUDE.md)
- Complete editorial authority: [`Blueprint/BLUEPRINT.txt`](Blueprint/BLUEPRINT.txt)
- Operational routing: [`Control/CONTROL.txt`](Control/CONTROL.txt)
- Cold reconstruction and mechanism audits: [`PORTABILITY/README.md`](PORTABILITY/README.md)

Publication remains supervisor-controlled. The registry is the public source
and build base; the workspace root holds the live editable sources. `Shift/`
is a generated local pickup, not a source or publication target. Its exact
inventory is rebuilt from the validated registry by the root `shift.py`.
After validation, `distribute_blueprint.py` copies and verifies the complete
`Blueprint/` tree at the approved pCloud, Google Drive and Bangkok Post
OneDrive destinations without deleting remote extras.

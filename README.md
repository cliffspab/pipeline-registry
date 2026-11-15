# Bangkok Post desk editor registry

The current modular Blueprint lives under [Blueprint](Blueprint/).

- Editable authority: [Blueprint/BLUEPRINT.md](Blueprint/BLUEPRINT.md)
- Complete generated surface: [Blueprint/BLUEPRINT.txt](Blueprint/BLUEPRINT.txt)
- Generated skills and routed files: [Blueprint/DEPLOY](Blueprint/DEPLOY/)
- Uploadable skill ZIPs: [Blueprint/UPLOAD](Blueprint/UPLOAD/)
- Cold recovery and mechanism audit: [PORTABILITY](PORTABILITY/)
- Operational recovery mirrors: [bootstrap](bootstrap/)

Run `python Blueprint/build.py --check --release` to prove generated text and
skill outputs. Run `python Blueprint/build_human_volume.py --check` to prove
that the edition-named Word volume matches the master source.

`push.bat` is the guarded publication entry point. It validates and displays
the payload before confirmation, pushes without rebasing, waits for GitHub
validation, refreshes the bounded Git-ignored `Blueprint/Shift/` pickup, then
includes it in the exact Blueprint tree copied to pCloud, Google Drive and
OneDrive. Cloud mirrors and Shift are not sources.

# BKPDE portability kit

This directory is the tools-only recovery kit for the single-master desk
mechanism. GitHub history is the content archive.

`Blueprint/MASTER.md` is deliberately absent from the kit. Recover content by
checking out the required Git commit. The ZIP contains the assembler,
publication workflow, desk tools, bootstrap instructions and these recovery
documents at their repository-relative paths.

## Commands

Rebuild from the repository root only when the process changes:

```powershell
python PORTABILITY/make_bundle.py
```

Run `make_bundle.py` only when the process machinery or portability documents
change. A content-only edit to `Blueprint/MASTER.md` does not rebuild the kit.

`make_bundle.py` refreshes `BKPDE-Portability.zip`. GitHub Actions exercises the
live assembler against the current master on every push; portability does not
duplicate that check or preserve content.

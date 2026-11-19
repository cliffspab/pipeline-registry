# BKPDE portability kit

This directory is the self-contained recovery and audit kit for the
single-master desk mechanism.

The live authority is `Blueprint/MASTER.md`; `Blueprint/assemble.js` renders
operational outputs at the point of use. The snapshot records the exact files
needed to understand, test and restore that mechanism without relying on the
retired publisher, cloud mirrors or Shift tree.

## Commands

From the repository root:

```powershell
python PORTABILITY/make_bundle.py
python PORTABILITY/verify_portability.py --live
```

`make_bundle.py` refreshes `snapshot/`, `AUDIT-SNAPSHOT.json`, `MANIFEST.json`
and `BKPDE-Portability.zip`. The verifier checks the kit, the snapshot against
the live files and the assembler itself.

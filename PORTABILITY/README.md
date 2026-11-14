# BKPDE portability and mechanism-audit kit

This folder is the independent entry point for reconstructing, operating and
auditing the Bangkok Post Desk Editor distribution mechanism without relying on
chat history or the original workstation.

Start here when the project folder is unavailable:

1. Read `COLD-REBUILD.md`.
2. Use `ARCHITECTURE.md` to understand authority and generated surfaces.
3. Follow `RELEASE-RUNBOOK.md` for a distribution.
4. Use `RECOVERY.md` only when a guard or publication stage fails.
5. Run `python verify_portability.py` to verify this kit.

For an independent mechanism audit, give an auditor the complete exported ZIP
and begin with `audit/AUDIT-BRIEF.md`. The ZIP carries frozen readable machinery
under `snapshot/`. Auditors propose findings; they do not edit the live
repository or redefine editorial rules.

The kit deliberately excludes credentials, rclone tokens, browser sessions and
machine-specific secrets. `DEPENDENCIES.md` explains how to restore access.

+# Audit decision log

The supervisor delegated mechanism governance with a preference for low model
usage, deterministic automation and concise successful runs.

| Date | Source | Finding | Decision | Reason and bounded implementation |
|---|---|---|---|---|
| 2026-11-15 | Claude F1; Gemini cloud | Mutable working-tree publication | accept | Publish only `Blueprint/` extracted from the validated full commit SHA. |
| 2026-11-15 | Claude F2 | Duplicate components and unmarked residue | accept | Reject duplicate, missing and out-of-component content; permanent tests added. |
| 2026-11-15 | Claude F3/F9; Gemini split-brain | Conflicting architecture and incomplete cold rebuild | accept | Make the registry self-contained; align bootstrap and portability instructions; retire Shift from the active path. |
| 2026-11-15 | Claude F4/F10/F12/F13; Gemini push | Hidden commits, rebase, lock deletion and false success | accept with bounds | Display staged and unpublished work, abort if behind, never auto-rebase or delete the lock, and fail non-zero. |
| 2026-11-15 | Claude F5; Gemini cloud | Duplicates and stale remote extras | accept with bounds | Fail duplicate paths; report remote-only files without deletion. |
| 2026-11-15 | Claude F6; Gemini Word identity | Hardcoded Word edition | accept | Derive filename, metadata and footer; embed and check the master source hash. |
| 2026-11-15 | Claude F7/F8 | Runtime and line endings undeclared | accept | Require Python 3.12+, pin direct dependencies and declare LF for mechanism text. |
| 2026-11-15 | Gemini Word parser | Body `---` hides later content | accept | Treat only opening front matter as metadata; permanent regression test added. |
| 2026-11-15 | Gemini route validation | Substring accepted as heading | accept | Require an exact Markdown heading line; permanent regression test added. |
| 2026-11-15 | Gemini GitHub conclusion | `gh run watch` may falsely pass | reject | CLI source and help confirm completion and failure semantics; `publish()` independently requires a completed successful run. |
| 2026-11-15 | Claude F11 | `--release` is a no-op | accept with bounds | Validate portable skill metadata under `--release`; reject Claude-specific limits. |
| 2026-11-15 | Claude F14 | No persistent publication evidence | accept | Write one concise ignored local JSON receipt after successful distribution. |

No audit suggestion changes editorial content or the approved edition identity.

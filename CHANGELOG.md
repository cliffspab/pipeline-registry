# Changelog

User-facing update map for the Blueprint beta and its delivered skills. It lets
a user update only the affected documents instead of comparing or replacing the
whole set. Planned work stays under **Unreleased** and moves into its own
versioned entry after a confirmed push and successful validation.

Each released entry names the version, date, affected deliveries and required
user action. This is a change summary, not editorial authority or a substitute
for `VERSION_HISTORY.md`, `COMMITS-PENDING.md` or the detailed shared workplan.

## Unreleased

Nothing pending.

## 231026_gpt_return-qc-addendum — 2026-10-23

**Changed instructions:** `boot`, `edit` and `check`.

**Affected install bundles:** all five archives, because `boot`, `check`,
`photo` and `pr` deliberately bundle the shared `edit` companion. Package
indexes and receipts will also be regenerated mechanically.

**User action:** reinstall any of the five skills currently in
use. Users maintaining loose routed files need replace only `BOOT.md`,
`edit.md`, `modules/check.md` and the regenerated indexes.

### Added

- Shared `WORKPLAN.md` for current plans, candidate status, open decisions and
  publication discipline.
- Added `QC` command under Check for reviewing another operator's Job Report,
  listing required factual and Bangkok Post style changes, and returning
  `Clear to initial.` when no changes are required.
- Added `ORIGINAL FILING` record for domestic news-desk jobs, reproducing the
  exact filing unmarked and unfenced after the Style Log.
- Added a standing Cabinet section to the Desk Addendum, dated 23 October 2026
  and verified against the current Royal Thai Government register and the
  March 30 Royal Command, as the sole maintained Cabinet roster.

### Changed

- Added the universal copy-box rule: edited, held and replacement copy returned
  to chat is fenced; a single `HOLD:` or `Query:` line sits directly above it.
- Set mode lifetime to one assistant turn, with no carry-over unless the
  supervisor invokes the mode again.
- Added direct Boot discovery of the Desk Addendum and explicit Edit routing
  to its Cabinet section; the roster is not duplicated in Directory or skill
  bundles.
- Deprecated `Shift/` as a handover route and retained it empty as a reusable
  named space while skills become the active delivery direction.

### Removed

- Removed stray duplicate Directory files from `Blueprint/DEPLOY/skills/`.
- Cleared the former Shift handover payload and two stray Obsidian directories
  from `Shift/`; nothing unique lived there under the former contract.

### Validation

- Published commit `fc0afa4`; GitHub **Validate Blueprint beta** completed
  successfully, and a cache-busted raw fetch returned the new Boot edition.

## 171026d_gpt_single-source-candidate — 2026-10-20

**Changed instructions:** `boot` and `edit`. Generated package indexes, all
skill archives and integrity receipts changed as mechanical consequences.

**User action:** replace the linked routed package or reinstall any skill whose
bundle carries Boot or the shared Edit companion. Loose routed deployments need
replace `BOOT.md`, `edit.md` and the regenerated indexes.

### Changed

- Hardened linked Boot discovery: `BOOT.md` now explicitly resolves its sibling
  index and indexed paths, and loads `edit.md` plus the Directory in the same
  turn.
- Aligned routed and skill Directory locations and rebuilt deployment indexes,
  skill archives and integrity receipts.
- Updated the guarded push for beta publication: validate the single-source
  Blueprint, fail closed on unsupported Control changes, verify GitHub, and
  leave sealing, Shift and pCloud paused.

### Validation

- Published commit `5639cbe`; GitHub **Validate Blueprint beta** completed
  successfully.

# COMMITS PENDING — check before push

Desk-made changes to the clone files, awaiting operator review and push.
Protocol (op-ruled 2026-07-04): approved changes to STATUS, PROCESSES,
BLUEPRINT or REFERENCES are written directly into the clone by the desk
and listed here, one line per change. Operator checks this list before
any push — it is the guard against a bulk file-swap silently erasing a
desk commit. Clear each line once pushed.

## Pending

- BLUEPRINT.txt / REGISTER part — deleted the orphaned part tagline
  "the lookups" under `# REGISTER`. It had no component page to land
  on (SECTION_SUBTITLE carries the four sections, not the part) and
  rendered stranded at the foot of the CORE page. Op-ruled 110826.
- BLUEPRINT.txt / REGISTER `status:` — deleted the `note:` block
  ("Apply the listed fact and flag ... operator-cleared before
  publication"). Spoiled the page and did not read. Op-ruled 110826;
  content may be restated elsewhere.
- Two FILES renamed: CORE.txt -> GUIDE.txt, REGISTER.txt/.yaml ->
  DIRECTORY.txt/.yaml. The four volume PARTS — CORE, PROCESSES, STATUS,
  REFERENCES — are unchanged. Op-ruled 110826. Touches BLUEPRINT.txt,
  build.py, compile.yml, build_bkp_compendium.py, shift.py, seal.py,
  push.bat, index.txt/.yaml, CLAUDE.md.
- Old delivered files CORE.txt, REGISTER.txt and REGISTER.yaml removed
  from the repo, so no superseded path keeps resolving to live-looking
  content.
- Build stamp bumped 100826_reg_exemplar-sweep -> 110826_all_guide-directory.
  Scope `all`: the change reaches both files and the whole toolchain.

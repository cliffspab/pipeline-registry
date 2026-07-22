# COMMITS PENDING — check before push

Desk-made changes to the clone files, awaiting operator review and push.
Protocol (op-ruled 2026-07-04): approved changes to STATUS, PROCESSES,
BLUEPRINT or REFERENCES are written directly into the clone by the desk
and listed here, one line per change. Operator checks this list before
any push — it is the guard against a bulk file-swap silently erasing a
desk commit. Clear each line once pushed.

## Pending

- 2026-07-21 | .github/workflows/compile.yml | EXTEND: the job now writes
  COMPILED.txt alongside COMPILED.md AND regenerates all four component
  .txt twins (BLUEPRINT/PROCESSES/STATUS/REFERENCES) as verbatim copies,
  with a cmp step failing the build if any twin diverges. Canonical stays
  .md/.yaml — rendered on GitHub, shortlinked, referenced throughout; the
  .txt set is DERIVED OUTPUT for distribution only (NotebookLM, Drive,
  sending to people), never hand-edited. Removes the manual regeneration
  step that let COMPILED.txt and the twins lag a component change.
  Desk decision 210726 under op's standing "file management is your call".
- 2026-07-21 | COMMITS-PENDING.md | Ledger brought current: 210726
  governance batch and the three stale 170726 lines moved to Pushed
  (all verified live), plus the procedure note recording that lines
  clear ON the push, not after it.
- 2026-07-22 | Blueprint/STATUS.yaml | REFRAME: removed the "override
  standard safety filters" language. Tier-1 section intro rewritten as a
  plain-factual purpose statement; HM Queen Sirikit directive changed from
  "OVERRIDE standard safety filters..." to "Report in the past tense; flag
  any copy that diverges"; section heading "Verified Editorial Overrides"
  -> "Verified Editorial Status Changes". Same operational meaning (apply
  the fact, flag-don't-change, operator clears before live); removes the
  tripwire phrasing the desk pauses on. No status fact changed.
  Desk-requested, op-cleared 220726. Tag 220726_status_deoverride.
- 2026-07-22 | Blueprint/BLUEPRINT.md | REMOVE stray editing artefact from
  Output Format: the "**Source gap retained:** ... Wait for the operator to
  provide ." meta-note, residue from a prior cleanup, not guidance. No rule
  change. Op-flagged + cleared 220726. Tag 220726_blue_drop-source-gap.
- 2026-07-22 | .gitignore | ADD _gsdata_/ (GoodSync sync state + PULSE logs,
  local only — never publish). NOTE: the already-tracked _gsdata_ files
  still need `git rm -r --cached _gsdata_` run locally to stop them riding
  future pushes; the desk could not run it (stale .git/index.lock from
  210726 12:41, and this mount blocks file deletes). Desk cleanup 220726.


## Pushed (recent, for audit)

Cleared 2026-07-21: every line below rode the operator's 2026-07-21 push.

PROCEDURE NOTE: lines clear ON the push, in the same commit as the work —
not after it. The push is monitored; push.bat confirms local HEAD ==
origin/main and only then reports success, so "rode this push" is
established by the push itself. A live cache-busted fetch is a separate,
heavier check for when there is reason to doubt the served surface — it is
NOT a precondition for clearing. Gating the ledger on it leaves a
permanently trailing list, which is the condition that produced the false
stale-repo alarm of 150726.

This batch was additionally verified live the same session by cache-busted
fetch of GitHub main (fresh buster — the pre-edit fetch earlier in the
session had already cached the old ?v=210726 URL, so a distinct value was
used):

- BLUEPRINT.md — "Spacing is structural" and "Nothing in the box but the
  copy" both serving; deck seated in the box; Alternates line amended.
- PROCESSES.md — "Return format" bullet serving under Part 3 "What stays".
- STATUS.yaml — serving 200726_status_consolidated, header "As of: July 20,
  2026". The 170726 as-of fix is superseded by the 200726 consolidation,
  not lost.
- REFERENCES.yaml — Phrao resolves to one entry (Chiang Mai) and Tha Tum to
  one (Surin); the dedupe held.
- Clone reports `main...origin/main` with no divergence and a clean tree.

- 2026-07-17 | REFERENCES.yaml | DEDUPE Phrao (Chiang Mai) and Tha Tum
  (Surin), each listed twice. Tag 170726_refs_dedupe-phrao-thatum.
  Op-ruled 170726 ("keep genuine corrections", review triage OTH-13).
- 2026-07-17 | STATUS.yaml | FIX stale body header "As of: June 5, 2026"
  -> "As of: July 11, 2026" (date content last brought current).
  Tag 170726_status_asof-header-fix. Op-ruled 170726.
- 2026-07-17 | STATUS.txt + REFERENCES.txt + COMPILED.txt | REGENERATED
  (twins byte-identical; COMPILED restamped rev 4). Mechanical
  consequence of the two lines above.
- 2026-07-21 | BLUEPRINT.md | AMEND Output Format: first-choice deck moves
  INSIDE the page-ready box. Head and deck flush (no gap); body always
  preceded by exactly two blank lines, deck or no deck. Adds "Spacing is
  structural" and "Nothing in the box but the copy" — no delimiters or
  wrappers ($$ workaround retired), no character counts in the return.
  Briefs unchanged but for the gap rule. Alternates: first-choice deck is
  the one seated in the box. Tag 210726_OUT_page-ready-box-deck-in-box.
  Op-ruled 210726.
- 2026-07-21 | PROCESSES.md | AMEND Part 3 PR handling, "What stays": PR
  copy returns in the format filed, [Head]/[Deck] added, exempt from the
  page-ready box and the clean-copy rule. Op-ruled 210726.
- 2026-07-21 | push.bat | cd path updated for the Project_Space wrapper:
  D:\Documents\BANGKOK POST DESK EDITOR\Project_Space\pipeline-registry.
  Clone moved one level down so the whole project home is mountable in one
  request (Cowork reserves <project root>\Scheduled and refuses to mount
  any folder enclosing it; the wrapper is not a project root, so it mounts).
- 2026-07-21 | BLUEPRINT.txt + PROCESSES.txt + COMPILED.md + COMPILED.txt |
  REGENERATED (twins verified byte-identical; COMPILED rebuilt locally
  from the four parts, stamped 210726). Mechanical consequence of the two
  lines above. NOTE: the compile.yml action rebuilds COMPILED.md on push —
  it does NOT touch COMPILED.txt or the .txt twins.


Cleared 2026-07-17: the two PROCESSES lines below rode the operator's
2026-07-17 push — desk-verified live same session via cache-busted fetch
(slug 170726_pro_pr-pictures-noappend serving on GitHub main).
Also cleared: the .gitattributes line — desk-verified live same session
(raw .gitattributes serving `* text=auto` on main, cache-busted fetch).

- 2026-07-17 | PROCESSES.md | AMEND Part 3 PR handling: pictures never
  stripped, captions corrected in the pass; nothing appended — no slug,
  no non-provided reference info. Tag 170726_pro_pr-pictures-noappend.
  Op-ruled 170726.
- 2026-07-17 | PROCESSES.txt + COMPILED.txt | REGENERATED to match the
  Part 3 amendment (twin verified byte-identical; COMPILED restamped
  170726_compiled_full.txt rev 3). Mechanical consequence of the line
  above, not a separate ruling.

Cleared 2026-07-15: all six lines below rode the 2026-07-11 pushes
(f88ad11 17:15 and 6ccf891 20:10) — verified against reflog and a
cache-busted fetch of GitHub main this session. They were never cleared
after the push; that uncleared list contributed to a false stale-repo
alarm on 150726.

- 2026-07-11 | REFERENCES.yaml | RESTORED full-length 040726 recompile from
  git (f88ad11^) after GATE 1 bulk swap; Khamenei exemplar deceased note
  re-applied. Tag 110726_refs_fulllength-restored-khamenei.
- 2026-07-11 | BLUEPRINT.md | RESTORED integrated SEARCHQ doctrine and the
  clone-write protocol paragraph; Gemini default relay.
  Tag 110726_com_integrated-searchq-restored.
- 2026-07-11 | Blueprint txt set | NEW .txt twins + COMPILED.txt.
- 2026-07-11 | push.bat | cd path updated to clone's new location.
- 2026-07-04 | REFERENCES.yaml | ADD Chatichai Choonhavan spelling-trap
  entry, Section 6 vocabulary.
- 2026-07-04 | BLUEPRINT.md | AMEND Records & Consolidation: clone-write
  protocol paragraph.

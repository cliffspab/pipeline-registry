# COMMITS PENDING — check before push

Desk-made changes to the clone files, awaiting operator review and push.
Protocol (op-ruled 2026-07-04): approved changes to STATUS, PROCESSES,
BLUEPRINT or REFERENCES are written directly into the clone by the desk
and listed here, one line per change. Operator checks this list before
any push — it is the guard against a bulk file-swap silently erasing a
desk commit. Clear each line once pushed.

## Pending

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


## Pushed (recent, for audit)

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

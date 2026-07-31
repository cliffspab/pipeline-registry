# COMMITS PENDING — check before push

Desk-made changes to the clone files, awaiting operator review and push.
Protocol (op-ruled 2026-07-04): approved changes to STATUS, PROCESSES,
BLUEPRINT or REFERENCES are written directly into the clone by the desk
and listed here, one line per change. Operator checks this list before
any push — it is the guard against a bulk file-swap silently erasing a
desk commit. Clear each line once pushed.

## Pending

- 2026-07-31 | DECISIONS-OPEN.yaml + VERSION_HISTORY.md | MOVED into the clone
  from the project root, so both ledgers now ride every push and a cold chat
  can read them. Scrubbed first, the repo being public:
  * REMOVED a live pCloud Public Folder access path from ARC-14 — a
    credential-shaped URL that would have been published permanently in the
    commit history. Operator holds it offline.
  * OTH-12 incident detail generalised: local drive paths, backup-software
    name and disk-image timestamps out; the finding, root cause and the
    lesson (block-level restores preserve pre-image stamps) all retained.
  * Six verbatim operator quotes replaced with neutral summaries of the same
    ruling across VER-04, VER-05, ARC-15 and OTH-13. No ruling, rationale or
    date altered — only the transcript voice.
  YAML re-parsed clean, 13 entries. Op-ruled 310726.

- 2026-07-31 | .github/workflows/compile.yml | FIX two CI gates that would have
  failed this push and published nothing. (a) The coverage audit's
  EXPECTED_ABSENT allowlist was pinned to the literal slug 270726_blueprint, so
  the first edition bump after it was written turned a declared absence into an
  unexplained one and a FATAL. Now matches any DDMMYY_slug stamp. (b) The
  structure guard compares the block profile against
  Blueprint/BLUEPRINT.manifest.json; the ruled section 8 conversion legitimately
  takes Table 2 -> 0 and BulletList 28 -> 22, which the guard cannot distinguish
  from markup loss. Manifest regenerated from the ruled format so it baselines
  the new shape. Both gates re-run locally against the workflow's own logic:
  split invertible PASS, structure PASS, coverage PASS 489/495 with 6 declared
  absent. Desk fix under standing "file management is your call".

- 2026-07-31 | Blueprint/BLUEPRINT.txt | LANGUAGE PASS. "Protocol" was left
  orphaned by the heading rename — nothing in the document is called one any
  more — so "Rules of the Protocol" -> "The rules", "DCX fit (Spatial Headline
  Protocol)" -> "DCX fit", and the Authority Hierarchy line drops it.
  "Structural exemplar" -> plain "kept because it teaches the rule".
  "Capital / structural rulings" -> "Capitals and country structure".
  Proximity Alert procedure in PROCESSES cut from 1,130 chars to three
  paragraphs: it stated flag-don't-change four times and repeated CORE's
  identity-field sentence verbatim, against ARC-13. All flourishes retained —
  "an absent alert is not an all-clear; the eye stays open", "the core concern
  of all news", "proximity is observation, not action". Op-ruled 310726.
- 2026-07-31 | tools/build_bkp_compendium.py | FIX cover pagination: the rule
  and tagline were unbound, so on real Arial Black metrics they broke to a
  second page and "This is why we have style..." sat alone. keep_with_next set
  on the Year style and the rule paragraph; cover lead padding cut 55pt -> 24pt
  to pay for the binding. NOT VERIFIABLE IN THE BUILD SANDBOX — Arial Black is
  absent there and substitutes shorter, so the fault never reproduced locally.
  Needs an operator check in Word on Windows.

- 2026-07-31 | Blueprint/BLUEPRINT.txt | HEADINGS, handoff section 7 applied
  properly (the earlier 310726 entry did the broken pointer only and skipped
  the test). Test run across the document: a heading string occurring once is
  pointed at by nothing and goes plain. Renamed on that basis — Operating
  Doctrine & Tone -> SOLVE THE PROBLEM; Authority Hierarchy -> Authority;
  Retrieval Protocol -> Retrieval; Proximity Alert -> Proximity; Verification
  Protocol -> Verification; Editing Scope, Quotes & Legality -> Editing.
  Retained precise strings where the text does point at them: page-ready box,
  Proximity Alert (in body), overspill, DCX, Route A/B, STYLE LOG, STATE LOG.
  Section numbers dropped from PROCESSES and REFERENCES headings, which
  removes the broken-pointer class that produced "Part 1 rules apply"; that
  pointer now reads CONVERSIONS, the name handoff section 6 assumes.
  THAI GEOGRAPHY -> THAI PLACES. PR subsections -> Minimal edit / RETAIN.
  Tier 1: Tripwires -> Tripwires; Tier 2: References -> Second tier.
  Part sub-lines added per the WIP: CORE / what we do, PROCESSES / how we do
  it, STATUS / people in the news, REFS / the knowledge base. REFS part
  opener given the H1 and sub-line the other three already had.
  Source: operator's own heading scheme in BLUEPRINTwip.docx. Op-ruled 310726.

- 2026-07-31 | Blueprint/BLUEPRINT.txt | HANDOFF SWEEP, sections 1-8 of
  310726_blueprint-review-handoff.md. Op-ruled 310726. Edition stamp
  310726_com_hedges-rule-home -> 310726_all_handoff-sweep (quadrant `all`).
  * CORE Verification Protocol: the Operator-first numbered steps and the
    Rules of the Protocol bullets replaced by one 4-rung resolution ladder
    (hazard / operator ruling / STATUS before memory / identity) with two
    trailing duties outside the numbering — "a flag never includes a silent
    edit" (op wording, 310726) and "record without exception".
  * CORE: risk tiered. Identity = flag, don't alter. Hazard = cut and flag.
    Desk has no authority to decide and absolute authority to stop.
  * CORE: search posture demoted from rule to setting, carried in the
    per-model prompt. Displaced: bangkokpost.com site-search method to the
    SEARCHQ section; Apex ordering to STATUS; training-data note parked on
    DECISIONS-OPEN ARC-06 pending a per-model deployment prompt.
  * CORE Output Format: the fake hold closed. "Held or anomaly notes precede
    the box" -> "Queries precede the box. A HOLD replaces it." Query and hold
    separated as two states; a HOLD suppresses the box.
  * PROCESSES Spatial Mechanics: "in-head count" (4 occurrences) replaced by
    verified/unverified and "manual tallying" (op wording, 310726). New
    "Scale sets the method" paragraph scopes the prohibition to body length,
    resolving the apparent DCX +/-2 contradiction.
  * PROCESSES: CONVERSIONS opening line cut to "Substitutions applied
    wherever the element appears in copy." PR pointer "Part 1 rules apply"
    -> "HOUSE CONVENTIONS rules apply".
  * STATUS + REFERENCES: tables and YAML converted to the key-ruling list
    shape, 168 entries, 21 group dividers to H3. AI Bias column dropped;
    provenance retained inside the ruling where it earns it (Suriya
    Singhakamol). STATUS honorific full stops and date forms brought to
    house. Volatility split written down at the head of STATUS.
- 2026-07-31 | tools/build_bkp_compendium.py | FIX: register entries opening
  with a bold key no longer qualify as AXIOM candidates. The H3 conversion
  above would otherwise have promoted the first entry of all 21 REFERENCES
  groups to an AXIOM bar. Holds AXIOM at 8, its pre-sweep level. Desk fix
  under standing "file management is your call".

- 2026-07-31 | Blueprint/BLUEPRINT.txt (CORE) | ADD OUT-07 "Hedges are not
  length candidates" as a subsection under Legality & Quotes. A hedge in
  filed copy is a liability position, not a length candidate; the overspill
  recast may not remove it. Preserve as filed, flag the claim for desk
  sourcing, find the characters elsewhere. Extends the existing "Retain
  hedges, eg allegedly" bullet from bare instruction to reasoned rule on the
  asymmetric-failure argument. Op-ruled 310726.
- 2026-07-31 | Blueprint/BLUEPRINT.txt (CORE) | ADD ARC-13 "One rule, one
  home" as a subsection closing the Authority Hierarchy. Where a rule and its
  exception straddle PROCESSES and REFERENCES, the rule is stated once in its
  sectional home; the register entry carries entity + exception + pointer,
  never a second statement that can drift. Op-ruled 310726.
- 2026-07-31 | Blueprint/BLUEPRINT.txt | VERSION: master stamp and all four
  part stamps moved 270726_all_records-extracted -> 310726_com_hedges-rule-home
  per the shared-edition scheme (240726). Quadrant code `com` — both changes
  land in CORE. Mechanical consequence of the two lines above.

- 2026-07-24 | BLUEPRINT.md + PROCESSES.md + STATUS.yaml + REFERENCES.yaml |
  VERSION SCHEME: the four component stamps unified to a single volume
  string. Previously each carried its own quadrant stamp (110726_com_,
  170726_pro_, 200726_status_, 170726_refs_); they now all read
  240726_all_records-extracted. The stamp names the date and the change,
  not the file — so a model fetching any single component reports which
  volume build it is running. Quadrant code `all` where a change touches
  every component. Op-ruled 240726.
- 2026-07-24 | REFERENCES.yaml | STRUCTURE: the six section titles
  (1. COUNTRIES through 6. VOCABULARY & SPELLING) converted from
  ====-wrapped plain text to ATX H2. They were previously invisible to
  any Markdown parser — absent from the docx contents, rendered as body
  text. No content change. Op-ruled 240726.
- 2026-07-24 | BLUEPRINT.md -> RECORDS-AND-CONSOLIDATION.md | EXTRACT:
  the Records & Consolidation section lifted out whole to its own file at
  clone root. Repository administration, not editorial instruction —
  fails the test "can a model sub a BKP story without this?". Placed at
  root rather than Blueprint/ so the compile job does not treat it as a
  fifth component. One phrase edited in transit: "this document" ->
  "BLUEPRINT" in the closing bullet, which referred to BLUEPRINT while
  the section sat inside it. Op-ruled 240726.
- 2026-07-24 | BLUEPRINT.md + PROCESSES.md + compile.yml | RENAME: Part 1
  is now CORE, not BLUEPRINT — the volume is called the Blueprint, so a
  part of the same name is a collision. CORE promotes a term the document
  already used (Authority Hierarchy item 4, "CORE Rules — this document").
  Filename, short link /blue and the `com` stamp code unchanged. New short
  link /core is live. Cross-references swept: PROCESSES companion line and
  the Part 3 PR return-format bullet both now read CORE. Op-ruled 240726.
- 2026-07-24 | .github/workflows/compile.yml | EXTEND: the job now builds
  Blueprint/BLUEPRINT.docx via pandoc on every component push. Reads
  COMPILED.md into a scratch copy at /tmp — COMPILED.md is never modified,
  the twins cmp check depends on it. Scratch pass strips the compile
  header, converts the ==== part dividers to page breaks, deletes any
  surviving ==== rules (NOT converted to ---, which is setext syntax and
  would silently promote the preceding line to a heading), and strips
  Google-Docs over-escaping (\+ \[ \] \< \> \_ only; \* and \\ left alone).
  Prepends volume front matter. Uses Blueprint/reference.docx if present,
  builds unstyled if not — reference.docx does not yet exist. Contents
  generated at --toc-depth=3. Desk decision 240726 under standing "file
  management is your call".
- 2026-07-24 | Blueprint/qr-code.svg + compile.yml | ADD: QR code to the
  volume cover, resolving to go.fuzzylogic.page/blue (repointed today from
  BLUEPRINT.md to the compendium, so the code takes a reader from the
  printed snapshot to the live text). librsvg2-bin added to the apt install
  so pandoc can rasterise SVG; --resource-path=Blueprint added so the
  scratch file in /tmp resolves the image. Width 3.5cm — provisional, the
  centre logo eats error-correction budget and it wants a scan test from
  print. Renders left-aligned until reference.docx provides a centred
  style. NOTE: the code carries the Bangkok Post masthead; desk flagged
  that the mark asserts institutional endorsement the cover text does not.
  Op-ruled 240726.

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

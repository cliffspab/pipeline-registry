# COMMITS PENDING — check before push

Desk-made changes to the clone files, awaiting operator review and push.
Protocol (op-ruled 2026-07-04): approved changes to STATUS, PROCESSES,
BLUEPRINT or REFERENCES are written directly into the clone by the desk
and listed here, one line per change. Operator checks this list before
any push — it is the guard against a bulk file-swap silently erasing a
desk commit. Clear each line once pushed.

## Pending

- 2026-08-09 | push.bat | FETCH AND REBASE BEFORE PUSHING. The 090826 push was
  REJECTED, non-fast-forward: the remote held compile-bot commits the clone did
  not have. Nothing was published; commit 41cc572 was created locally and stayed
  there.
  * STRUCTURAL, not a one-off. compile.yml derives CORE/REGISTER/docx/manifest
    and commits them to main itself, so the clone is behind after EVERY build it
    triggers. push.bat staged, committed and pushed with no integration step,
    which cannot succeed the first time after any CI run. Noted in handoff 070826
    §0 as "the clone was behind by one compile-bot build on 080826" — observed
    then, never fixed.
  * Now: fetch, rebase onto origin/main, then push. The desk's commit lands on
    top of the bot's.
  * ABORTS ON CONFLICT, does not resolve one. Derived files are the likely site
    and taking the wrong side by hand is what the CI hand-edit guard exists to
    catch. The abort message says to take origin's copy where the conflict is a
    derived file, and gives `git rebase --abort` to back out.
  * DETECTION NOTE: three cache-busted fetches — index.txt, index.yaml and
    prompts/system.md, distinct busters — all returned the pre-push state, and
    system.md returned empty. The served surface was read correctly. The desk did
    not declare a repository fault on it; the operator's push.bat output settled
    the cause in one step, which is the §0 procedure working as written.

- 2026-08-09 | Blueprint/BLUEPRINT.txt | THE REBUILD WRITTEN INTO THE CLONE.
  070826_all_rebuild replaces 010826_all_core-prune-seam. The rebuild had lived
  only at the Project_Space root since 070826; the clone and every shortlink
  still served the four-part build, and the tags gave no sign of it, a four-part
  set agreeing with itself passing the edition guard.
  * ONLY THE SOURCE IS COPIED. CORE.txt, REGISTER.yaml, REGISTER.txt, the docx
    and the manifest are derived and committed by compile.yml. Copying any of
    them by hand trips the guard at the head of the workflow and the push is
    REJECTED. This is the one thing to get right about pushing this repo.
  * compile.yml, tools/build_bkp_compendium.py and tools/bkp_docx_design.py were
    already updated locally on 080826 and ride this push with the source.
  * EXPECTED ON FIRST PUSH: the structure guard FAILS. Headings drop 98 -> 54
    because forty-odd register headings became one fenced block. By design —
    its own message says to rerun once to reset the baseline. A 45% structural
    drop should stop the line and have a human wave it through.
- 2026-08-09 | Blueprint/index.txt + index.yaml | REWRITTEN for two parts.
  Both still listed processes/status/references and had no core or reg entry —
  the .md -> .txt repair of 070826 fixed the extensions and left the four-part
  shape. Now: blueprint, core, reg. status/refs/full moved under a `shims` key
  and marked do-not-deploy; pro dropped, PROCESSES no longer being produced.
  Deployment subset named in a comment. Parses; twins byte-identical.
- 2026-08-09 | Blueprint/prompts/system.md + instructions.md | FILLED. Both had
  been zero bytes since 26 June and are named in handoff 070826 §5 as where pull
  integrity goes.
  * system.md — handoff §7 verbatim. The bad-pull test, the two further
    conditions that read as one, and the rule that an operator-supplied figure is
    cited as theirs and not restated as a desk verification.
  * instructions.md — what to pull and why: the two parts in text format,
    confirmed latest only; the shortlink table; shims marked do-not-deploy;
    artifacts of record never deploy; per-model prompt production, with the
    Route A / Route B capability caution carried over.
  Assembled from ruled material. No new doctrine.
- 2026-08-09 | RECORDS-AND-CONSOLIDATION.md | SUBSET CORRECTED TO TEXT FORMAT.
  Op-ruled 090826. The desk had written CORE.txt + REGISTER.yaml; the ruling is
  the two parts in text format, CORE.txt + REGISTER.txt. Bytes are identical and
  the extension is inert, but .yaml is the authoring form and .txt is what
  travels, and the subset names what travels. Section head now also states the
  document's shape — two parts, CORE markdown, REGISTER YAML, both delivered as
  .txt, syntax load-bearing and extension inert.

- 2026-08-09 | RECORDS-AND-CONSOLIDATION.md | CORPUS / DEPLOYMENT SUBSET, new
  section at the head. Op-ruled 090826. Stamp 240726_all_records-extracted ->
  090826_all_corpus-deployment-split.
  * The corpus is everything held; the deployment subset is what a processor
    receives to work a shift. A file is corpus by being held, and enters the
    subset by being needed at the point of edit. The corpus is listed in five
    classes — source, derived governance, artifacts of record, administration,
    machinery — of which only derived governance deploys.
  * ARTIFACTS OF RECORD DO NOT DEPLOY. The PDF and the volume fix a build in
    amber and carry no seam a processor can check; they are the least current
    thing in the corpus the moment the source moves.
  * STANDING SUBSET: CORE.txt + REGISTER.yaml, confirmed latest only.
    BLUEPRINT.txt substitutes for the pair where a destination takes one file.
  * CONFIRMED LATEST defined as a checked tag, not a filename or a modification
    date. Carries handoff 070826 §0 into procedure: clone and remote go stale in
    opposite directions, and a matching tag proves structural agreement only.
  * Prompted by the 090826 isolation of the 070826_all_rebuild set. Eight files
    were named as the deployment; two are read by a processor editing copy.
    Nothing in the corpus distinguished the holding from the working set.
- 2026-08-09 | RECORDS-AND-CONSOLIDATION.md | TWO STALE LINES, consequential on
  the 070826 CORE + REGISTER ruling, not separate rulings.
  * Clone-write protocol named STATUS, PROCESSES, BLUEPRINT or REFERENCES; now
    names BLUEPRINT as the only file edited, CORE and REGISTER deriving from it.
  * Close-out bullet lost its short file. STATUS was the one small enough to
    reprint whole; the merge leaves BLUEPRINT, CORE and REGISTER all large, so
    patches are the only form. FLAGGED: the large/short threshold no longer
    discriminates and the bullet now states a flat rule. If the operator wants
    the distinction kept, it needs a size or a ruling.
  * Per-model deployment sentence moved into the new section — it draws on the
    subset, which now has a definition to draw on.
- 2026-08-09 | VERSION_HISTORY.md | ENTRY for the above, newest first, with the
  090826 guard run recorded: edition PASS both seams against front matter,
  invertibility PASS (CORE verbatim substring; register lifts and reconciles
  below the seam line), register parse PASS (status + references), dollar
  pairing PASS per paragraph (two signs, no paragraph holding both). REGISTER
  pair byte-identical, md5 9954d821. NOT A BUILD — no compile was run and no
  stamp on the governance files changed; the guards were run by hand against
  the isolated set.

- 2026-08-01 | Blueprint/BLUEPRINT.txt + DECISIONS-OPEN.yaml | FOUR PARKED
  ITEMS RULED, op 010826.
  * REFERENCES / THAI PLACES: "A name not listed here stands as the reporter
    filed it: apply the global rules and nothing else." The opening line "Use
    RTGS transliteration" read as standing permission to romanise, while every
    rule beneath it is an RTGS OVERRIDE — so a model meeting an unlisted
    district could "correct" the reporter from training data. Same fault found
    inside the register on 310726. From the third-party audit, OTH-15 (a).
  * PROCESSES / Proximity Alert: "Raise it as a query above the box, where the
    operator sees it before lifting. The Style Log and State Log carry it under
    their existing headings." Op ruling: box and Style Log by editorial need,
    State Log by protocol. Only the box placement is new — the two logs already
    claim it under "unresolved reference issues" and "Flags or anomalies", so
    they are pointed at, not restated. OTH-15 (b).
  * CORE / The rules: SCOPE OF THE HALT WIDENED, superseding the 310726
    tripwires-only ruling. Now "A direct contradiction between FILED COPY and
    STATUS halts the work before the edit begins." Op ruling: halt on source
    copy against reference fact, at either tier; do NOT halt on AI knowledge
    against copy. Naming the two parties carries the scope without explanation
    — training data is not filed copy, so it is excluded by the wording rather
    than by a paragraph about it. The tier distinction no longer gates the
    halt; it remains a priority order for scanning.
  * ARC-17 PRUNED, ruled no action: RECORDS-AND-CONSOLIDATION is operational
    structure, not doctrine. It needs no pointer and no shortlink, and it is
    not secret — it governs operator and custody, not processors. The desk's
    breach of it on 010826 was a custody failure, not a reachability problem.
  Gates: split PASS, invertibility PASS byte-for-byte, edition PASS, structure
  PASS, coverage PASS 482/484.

- 2026-08-01 | Blueprint/BLUEPRINT.txt | STATUS ENTRIES CLEARED. Operator
  verified four of the five moved from the REFS title-retention block and
  supplied firmer dates than the desk had; applied verbatim.
  * King Jigme Khesar Namgyel Wangchuck — reigning since 2006, crowned 2008.
  * Catherine, Princess of Wales — from 9 Sept 2022, on the accession of King
    Charles III. (Desk had "Sept 2022".)
  * Prince William, Prince of Wales — from 9 Sept 2022, letters patent Feb
    2023; Duke of Cambridge 2011-2022. The two-stage date is the operator's
    correction: announced then formalised.
  * Pope Emeritus Benedict XVI — died 31 Dec 2022 aged 95, resigned 2013.
  * LI KEQIANG — died 27 Oct 2023, operator-confirmed. Added to Mortalities,
    which closes the REFERENCES/PROCESSES conflict flagged earlier the same
    day: the REFS entry read "second reference Mr Li" while PROCESSES strips
    honorifics from the deceased. REFS entry amended to "Chinese convention,
    surname first. Deceased; no honorific — see STATUS" — it keeps him as a
    surname-first exemplar and stops instructing a form the house forbids.
    Xi Jinping carries the live exemplar, so nothing is lost by his demotion.
  * King Salman bin Abdulaziz al-Saud — king of Saudi Arabia, from 23 Jan
    2015, on the death of King Abdullah. Operator-confirmed in a second pass
    after it was flagged as missing from the first. The REFS short form
    ("King Salman" usually suffices) confirmed as standard international
    usage, so the split holds: short form in REFERENCES, reign in STATUS.
  ALL FIVE MOVED ENTRIES ARE NOW OPERATOR-CLEARED. The block that produced
  them had gone unchecked since at least June 2026 and carried two facts that
  expired in 2022.
  Gates: split PASS, invertibility PASS byte-for-byte, edition PASS, structure
  PASS, coverage PASS 481/483.

- 2026-08-01 | Blueprint/BLUEPRINT.txt | AUTHORITY REORDER + TITLE-RETENTION
  BLOCK REFILED. Op-ruled 010826, prompted by a third-party audit of the set.
  * AUTHORITY: STATUS moves above REFERENCES — 1 CORE, 2 STATUS, 3 REFERENCES,
    4 PROCESSES. STATUS carries what is true today and now wins a collision on
    title, office or life-status. REFERENCES gains "Governs form, not current
    status"; STATUS loses "ranks alongside REFERENCES", which the new order
    contradicts.
  * The REFS "Title retention" block was a status section filed in the register
    that does not expire. Every entry was person + current title, the same
    shape as a STATUS entry. Two had already rotted: Pope Emeritus Benedict XVI
    died Dec 2022, and Catherine ceased to be Duchess of Cambridge in Sept 2022
    — the entry read "Not Princess", banning the form that had become correct.
  * Worse, the rule the block existed to demonstrate is already in PROCESSES
    ("Higher ranks are retained on all references: ... royal titles ..."), and
    the REFS restatement was parenthetical, buried inside the entry for the one
    man in the block who had died. A rule hiding inside an example of itself.
  * RESOLVED per One rule, one home: rule stays in PROCESSES; REFS keeps three
    short-form conventions ("King Salman" usually suffices, etc), which do not
    expire on a death; the status facts move to STATUS. The Khamenei REFS entry
    is dropped entirely — he is in STATUS and the retention rule is in
    PROCESSES, so it carried nothing of its own. Prince William and Catherine
    do not survive as REFS entries.
  * ADDED TO STATUS Global Figures: King Salman, King Jigme Khesar, Catherine
    Princess of Wales (FLAG Duchess of Cambridge), Prince William Prince of
    Wales. ADDED TO Mortalities: Pope Emeritus Benedict XVI, died 31 Dec 2022.
    DESK-SUPPLIED FROM TRAINING, NOT OPERATOR-CLEARED. STATUS states that all
    facts are operator-cleared before publication; these five are not. They
    correct entries that were demonstrably wrong, but the dates and forms need
    the operator's eye before they carry authority.
  * STILL OPEN, not acted on: Li Keqiang (d. Oct 2023) carries "second
    reference Mr Li" in REFS while PROCESSES strips honorifics from the
    deceased — REFS and PROCESSES give opposite instructions on the same name,
    and he is in neither STATUS tier. The general fault: nothing audits REFS
    against the volatility test, so an entry stays authoritative until a human
    happens to read it.
  Gates: split PASS, invertibility PASS byte-for-byte, edition PASS, structure
  PASS, coverage PASS 480/482.

- 2026-08-01 | Blueprint/BLUEPRINT.txt | VERSION: 310726_all_handoff-sweep ->
  010826_all_core-prune-seam across the front matter and all four part seams.
  Quadrant `all` — CORE pruned, STATUS tripwires intro amended, REFERENCES
  place names corrected, tooling changed. Caught on the pre-push check: the
  day's work was about to publish under yesterday's stamp, which is the exact
  staleness the slug exists to detect and which the new edition guard cannot
  catch, since it only tests that the four agree with each other.

- 2026-08-01 | PROVENANCE, for the record | The REFERENCES inconsistencies are
  not drift and nothing has been editing the file. Pickaxe on the repo history:
  commit 07a9ad5, 10 June 2026, the first upload of docs/ref/REFERENCES.md,
  contains the master rule "Klong (not Khlong)" AND all nine Khlong district
  entries in the same commit. Ekaterinberg and Sri Muang Mai likewise. The
  contradiction arrived with the file and survived all 43 commits since.
  Shape of it: the province lists are complete official district rosters, and
  official Thai romanisation gives Khlong / Sri / Ko, while the master rules
  are BKP house and give Klong / Si / Koh. Two sources merged, house rules
  never run over the imported data. The misspellings trace to the 2018 guide
  the file names as its own ancestor. The 310726/010826 corrections are the
  first enforcement of the register's rule against the register's data.

- 2026-08-01 | Blueprint/BLUEPRINT.txt | PLACE NAMES, 20 corrections applied.
  Op-ruled 010826: the operator has not touched this content, so the forms are
  errors rather than deliberate house choices. (Applied 310726, reverted the
  same day on a misreading of "i changed them", now reinstated.)
  * Khlong -> Klong, 9 district/road entries: Khuean, Khlung, Lan, Thom, Luang,
    Hoi Khong, Yai, Hat, and Nuea Khlong. Per the transliteration master rule
    "Klong (not Khlong)", restated in third_party_spellings as applying to
    district and road names. GUARDED: the master rule's own counter-example
    ("NOT Khlong Toei") and the institutional name Khlong Prem Prachakon are
    untouched — a naive sweep rewrites the counter-example into nonsense, which
    it did on the first attempt 310726.
  * Sri -> Si, 3: Sri Muang Mai, Sri Sakhon, Sri That. The section header
    claims RTGS, which gives Si, and Si Sa Ket / Si Racha / Si Satchanalai
    already follow it.
  * Ko -> Koh, 1: Ko Kha, Lampang — the lone Ko against eight Koh.
  * Misspellings, 4: Ekaterinberg -> Ekaterinburg; Eyjafjallajokul ->
    Eyjafjallajokull; Ban Dan Lan Naik -> Ban Dan Lan Hoi; Non Kunn -> Non Khun.
  * Duplicates, 3: Roi Et carried Jung Han and Changhan as one district, merged
    to Chang Han; Mukdahan carried Camcha-i and Khamcha-i, kept Khamcha-i;
    Khaen Dong was filed under both Nakhon Phanom and Buri Ram, removed from
    Nakhon Phanom. NOT BACKFILLED: Nakhon Phanom now lists 11 districts and the
    missing 12th is not supplied from desk memory — flagged for the operator.
  * United Kingdom entry retained as corrected 310726: the UK includes Northern
    Ireland; Great Britain is the term that excludes it. The filed text had it
    inverted.
- 2026-08-01 | DECISIONS-OPEN.yaml | ADD OTH-14, REFERENCES taxonomy — countries
  ranks beside places despite being a subset. Operator parked it 010826.
  next-keys -> OTH-15. PENDING.

- 2026-08-01 | tools/build_bkp_compendium.py + compile.yml | COVER: nothing
  below the tagline (op-ruled 010826). The Components line was printing under
  "This is why we have style..." because start_index was a hard 2 — title
  block, slug block, body — and splitting the slug from the Components line
  onto separate source lines made them two blocks rather than one. Front
  matter is cover material by definition, so the body now starts at the first
  part seam however many paragraphs the preamble runs to. Components stays in
  the source for anyone reading raw text; declared absent in the volume.

- 2026-08-01 | Blueprint/BLUEPRINT.txt | CORE PRUNE, operator rulings 010826.
  * AUTHORITY + RETRIEVAL merged into one list; the Retrieval section is gone.
    CORE moves from 4th to 1st: it is the frame in which the register has
    authority at all, not a competitor to it on matters of fact, so "higher
    overrides lower" is now simply true where before it was strained. RAG
    triggers fold into the items they gate, as `Trigger:` on 2 and 3. The
    preamble sentence gating them was dropped rather than reworded — `Trigger:`
    already states it at the point of use, and a positional pointer ("query 2
    and 3") is the class of reference that rots on reorder.
  * THE RULES + THE TWO RISKS collapsed. Cut: the rung-order gloss, the
    hazard-is-a-property-not-a-state paragraph, and "no authority to decide,
    absolute authority to stop" — justification, not instruction, and defending
    against a failure the architecture already prevents (nothing reaches the
    register except through the operator).
  * "A flag never includes a silent edit" cut. Op ruling: a flag is a bookmark
    to a point, query or problem; a flag that includes a silent edit is
    oxymoronic, and the two risk bullets already state the action in each case.
    No definition of "flag" added — the ordinary sense is the operative one,
    and the ambiguity that would need defining lives in the action, which is
    already specified.
  * "Record without exception" -> "Record checks without exception", scoped to
    the checks above it. The old line told the desk to write to STATUS, which a
    processor on a raw link cannot do; STATE LOG already carries the register
    field, so this was a second statement of a rule with a sectional home.
  * London/Google/Tuesday preserved as the opening line of The rules.
  * NEW: a direct contradiction with a STATUS TRIPWIRE halts the work BEFORE
    the edit begins; the return is the finding, not copy. Replaces "flagged
    for operator guidance — not returned as edited and ready".
    SCOPE, op-ruled 010826: tripwires only. Four drafts were wrong before this
    one, each caught by the operator pre-push. (1) Halted on any register
    divergence — would have stopped a shift on a stale title and made dead
    letters of 20 FLAG directives. (2) Fixed the rule, then appended 60 words
    explaining the fix: the desk showing its working, not instructing an
    editor. (3) Read "contradiction in the copy" as copy-against-itself; it
    means a contradiction found in the copy. (4) Scoped to "STATUS or
    REFERENCES", which would have halted on every house-form error — Nigerian
    for Nigerien, Khlong for Klong — since those are direct contradictions
    with REFERENCES too. Tripwires alone carry the halt; everything else is
    the style pass.
    CONSEQUENT: the tier distinction is now load-bearing, so "Tripwires" is a
    heading the text points at and keeps its precise string — the section 7
    test applied in reverse. Stale "lower tiers follow" cleared from the
    Tripwires intro, tier labels having been dropped 310726.
  * STYLE LOG exemplar replaced. "Srettha Thavisin | Register hit; title
    corrected to former prime minister" was never a register hit: it describes
    the desk doubting correct copy on the strength of its training data and
    STATUS settling the doubt — a training-data resolution passed off as a
    factual correction, and under the new rule it would read as a halt case.
    Now "Niger | Demonym corrected to Nigerien per REFERENCES", which is an
    actual style-pass action.
  Source 1159 -> 1136 lines. Gates: split PASS, invertibility PASS
  byte-for-byte, edition PASS, structure PASS, coverage PASS 478/479.
- 2026-08-01 | DECISIONS-OPEN.yaml | ADD VER-06, content sweep — mandatory
  pre-edit pass (required to make the halt-before-edit rule executable) and a
  post-edit adversarial re-read. Operator field test on Gemini 010826. Field
  note: the second pass only fired at hype-max register; step belongs in CORE,
  intensity in the per-model prompt. next-keys bumped to VER-07. PENDING.

- 2026-08-01 | Blueprint/BLUEPRINT.txt + compile.yml + build_bkp_compendium.py |
  EDITION MOVED INTO THE SEAM. <!-- PART: <edition> <NAME> -->, leaving the
  shortlink as the only visible line above each part title. Machine identity
  sits machine-side; the reader gets one line. Op-ruled 010826.
  VER-05 check before adopting: the slug is now invisible in GitHub's RENDERED
  markdown view. It is unaffected everywhere the register is actually read —
  every shortlink resolves to raw.githubusercontent served as text/plain, so
  the comment is on screen; the volume carries it in the running head.
  REGRESSION CAUGHT PRE-PUSH: cutting the parts after the seam left every
  component file with no edition stamp at all — a slug readback against a
  standalone CORE.txt would have returned nothing, which is the single check
  VER-05 exists to make. The seam now travels WITH its part, so each component
  opens by naming its own edition and section. Reassembly became plain
  concatenation as a side effect; invertibility still byte-for-byte.
  Edition guard now also checks the four seams against the front-matter stamp.
  Gates: split PASS, invertibility PASS byte-for-byte, edition PASS, structure
  PASS, coverage PASS 483/484.

- 2026-08-01 | build_bkp_compendium.py + audit_bkp_compendium.py | STAMP TO THE
  RUNNING HEAD. Operator observed the stamp line reading as a header in Word.
  It was a body paragraph sitting where a header would be, while the real
  first-page header was empty (blank_first=True). Now written into each
  section's first-page header, so the band carries the full stamp on a part's
  opening page and the compact "/core 7" on every page after — one position
  for the eye instead of two. The source keeps the line: it is the component's
  identity when the .txt is read alone, and the edition guard's anchor.
  CONSEQUENT AUDIT FIX: the coverage gate read word/document.xml only, so
  anything in a header or footer was invisible to it and relocating content out
  of the body registered as content loss — exactly the distinction the audit
  exists to make. It now reads header and footer parts too. Caught by the gate
  failing 478/484 on this change; back to 483/484 with one declared absence.
  NOTE: the audit matches by substring, so the bare front-matter slug now
  passes on the strength of the header stamp containing it. Pre-existing
  looseness, not introduced here, but it means that one line is unverified.

- 2026-08-01 | Blueprint/BLUEPRINT.txt + compile.yml + build_bkp_compendium.py |
  SEAM AND PART OPENING. The banner was three lines — a 60-char rule, a
  "# PART: X" heading, another rule. It printed as literal text in every
  plain-text lane (operator hit it reading /full) and stood a second H1 above
  each component title. Replaced by one HTML comment, <!-- PART: X -->:
  invisible in any markdown render, greppable, impossible to write by accident,
  and free of the setext hazard that stopped the rules ever becoming "---".
  Marker choice left to the desk; layout ruled by the operator 010826.
  * Part opening is now: seam, then <slug> | <shortlink> on one line, then the
    title H1, then the sub-line. Operator layout.
  * Shortlink is plain text, not a markdown link (op-ruled 010826). Costs
    clickability in the volume and on GitHub; accepted.
  * Word section now opens on the SEAM, not on the title H1. Keying off the
    title stranded anything between the two — the stamp line now sits there —
    on the previous part's last page.
  * New BKP Part Stamp style: Arial 8.5, right-aligned, per operator sketch.
    Plain text keeps the line left, where column padding breaks on reflow.
  * skip_duplicate_component_heading retired — a flag whose only purpose was
    swallowing the second heading the banner created.
  * "### Orientation" folded away: SOLVE THE PROBLEM carries the axiom as its
    heading instead of repeating it as a bar beneath.
  * Coverage allowlist trimmed 3 declared absences to 1; the other two
    described a document that no longer exists.
  NEW EDITION GUARD: the four component stamps must agree. The shared-edition
  scheme was ruled 240726 and nothing has ever checked it — a part left on an
  old slug passed every gate and would surface only as a slug readback
  disagreeing with itself. Now fails the build. Cheap only because the merged
  stamp line gives it one predictable place to look.
  Gates: split PASS, invertibility PASS byte-for-byte, edition PASS, structure
  PASS, coverage PASS 483/484. Source down 23 lines, volume 33pp -> 32pp,
  AXIOMs 8 -> 6 ("Format follows the request" fell out on its own — it only
  ever qualified because the ==== rule beneath it was a paragraph).

- 2026-08-01 | Blueprint/BLUEPRINT.txt | DEFECT FIX from the 310726 sweep.
  The section 1 restructure replaced the numbered Operator-first steps but
  left the "### Operator-first / Resolve checks in this order. Higher steps
  come first." heading and lead line standing above them. It headed nothing:
  "The rules" ladder followed immediately with its own intro line. Removed.
  Also "BKP THAI GEOGRAPHY INDEX" still sat under the renamed THAI PLACES
  heading; now reads "The BKP index of Thai places." Found by a stub scan
  against the served CORE.txt, not by the CI gates — coverage and structure
  both pass a dangling heading, since no content is lost by one.

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

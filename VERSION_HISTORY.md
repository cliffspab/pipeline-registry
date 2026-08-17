# VERSION HISTORY — BKP STYLE GUIDE / BLUEPRINT

Running log of document lineage. Mitigation against lost context and
cross-workspace blind spots. Append-only: newest entry first. Every
anointment, supersession, deletion sweep and audit gets an entry.

Convention per entry: date (YYYY-MM-DD), event, evidence, verdict.

---


## 2026-08-16 — SHIFT FOLDER RETURNED TO THE GO-BAG; shift.py CUTS THREE

**The purpose, restated by the operator and recorded here because the desk had it
wrong.** The folder exists so that a subeditor reached anywhere, in any state, has
the bare minimum to sub a release and nothing to sift through. That is
`BLUEPRINT.txt` whole for a destination taking one file, and `GUIDE.txt` +
`DIRECTORY.txt` for one taking the split pair. Three files. The beta lane is kept
out deliberately — it is not the lifesaver the folder is for.

**Found.** `Shift\` held 27 entries. The three current parts were refreshed to
`110826_all_shortlink-names` this session; the other 24 dated from the 11 August
composite assembly recorded in its own `MANIFEST.txt`. The desk read an earlier
instruction — family-less documents stay saved — as licence to keep that composite
in place and refresh around it, and refreshed `DIRECTORY.yaml` as part of the set,
entrenching a stray on a folder it had already reported would fail its own guard.

**Done.** The sidebar collection — SIDEBAR.md/.docx/.pdf, EDIT, PR, PHOTO, CHECK,
WATCH, AUDIT, MANIFEST — moved to `pipeline-registry/design/Sidebar/`, design being
where work sits that needs no close watch until finished. Checked for
credential-shaped links first, none found, which matters because design/ is inside
the public clone. The shim set was already copied to `_pending-delete\`. The
remaining strays are redundant against `Editions/110826_all_guide-directory/`, the
clone or origin. `Shift\` goes to three; the sweep is the operator's, `rm` being
blocked on the mount.

**shift.py corrected.** `PARTS` was two files, so the tool that maintains the
folder would have reported NOT READY on `BLUEPRINT.txt` forever — the go-bag
rejected by its own keeper. `PARTS` is now the three. `BLUEPRINT.txt` opens with
its title rather than a `PART:` seam, so the build-tag agreement check runs over a
separate `SEAMED` pair and the source is copied without being tag-checked.
Exercised against a mock root: clean cut, idempotent re-run, stray detected and
NOT READY returned with exit 1.

## 2026-08-16 — SHORTLINK AUDIT; core AND reg REPOINTED AND RETIRED

**Audit.** Every shortlink in the operating instruction set tested against Dub
and against its raw target. Live and correct: `/blue`, `/guide`, `/dir`,
`/beta`, `/git`, `/bpdocx`, `/status`, `/refs`. Dub keys are case-insensitive —
`/DIR` and `/dir` resolve identically.

**Found.** `/core` returned HTTP 404 on every attempt during the audit, against
a destination of `main/Blueprint/CORE.txt` — a path deleted from the repo on
2026-08-11 in b308601. The desk asserted a mechanism for the bare 404 that it had
not verified and could not verify from outside the Dub console; what it had was
the 404 and the deleted destination, which was enough for the finding and not
enough for the explanation. Record the evidence, not the mechanism. The entry below records `/core` and `/reg` as moving to the shims
block and still resolving — the index was updated, the Dub destination was not.
`/pro` behaves the same way against `PROCESSES.txt`, deleted 2026-08-09, and was
already ruled retired on 080826. `/reg` and `/full` are not registered on Dub at
all: Dub serves its own "link not found" page for those, which is what separates
them from the 404 cases.

**Evidence.** Raw fetch of `main/Blueprint/CORE.txt` → 404. `git log
--diff-filter=D` names b308601 (2026-08-11) for `Blueprint/CORE.txt` and
c7bca93 (2026-08-09) for `Blueprint/PROCESSES.txt`. Bare HTTP 404 on `/core` and
`/pro`, against Dub's rendered error page on `/reg` and `/full`.

**Verdict (op-ruled 2026-08-16).** Repoint `/core` at the live part so nothing
held on an old link breaks, and treat it as a retired name from this date — not
published, not cited in the operating document. `index.txt` and `index.yaml`
carry the retirement line alongside the 080826 `pro` line.

**Closed same day.** The operator repointed `/core` at
`refs/heads/main/Blueprint/GUIDE.txt` within the hour and it was verified
resolving, 302, same target as `/guide`. `/reg` has no Dub entry and none was
created: a key invented for a name retired the same day buys nothing, and
`index.txt` already carries the target if one is ever wanted.

**`/pro` is not settled.** It returned a bare 404 on three attempts with
different cache-busting parameters. That signature is not diagnostic — `/core`
produced it too while registered — so nothing about `/pro` can be concluded from
outside the Dub console. It was ruled retired on 080826 either way; if an entry
is still there it is aimed at `PROCESSES.txt`, deleted 2026-08-09.

**Also found, unactioned.** `Shift/` holds the `110826_all_guide-directory`
parts, one build behind the root's `110826_all_shortlink-names`; it also holds
the 11 August SIDEBAR composite, which `shift.py`'s no-stray-file guard will
refuse. Left as assembled, no ruling sought. `compile.yml`'s header comment at
lines 11-13 still labels the two derived files `/core /reg`.

**Clone state.** No content drift between the clone and origin: every byte-size
difference is CRLF under `* text=auto`. origin/main at f4db87f.

**BOOTSTRAP CORRECTED, same day.** Six untrue facts in `CLAUDE.md`, found while
answering the audit and fixed under the file's own closing rule. `pushed: false`
for `110826_all_shortlink-names` — it is live on origin. `serving:` carried
GUIDE.txt 27557 and DIRECTORY 36301 at bot `c7bca93`, verified 090826; the remote
now holds 26399 and 36842 at bot `3ac740c`. `working_set` gave GUIDE.txt the link
`/core` and DIRECTORY.txt `/reg`, both retired earlier today; now `/guide` and
`/dir`. `editions:` named 090826_reg_part-opening as current and listed two
sealed; `Editions\` holds five, and the current one is 110826_all_shortlink-names.
`history:` pointed at the 090826 handoff as CURRENT with the 110826 and 130826
documents sitting past it. `custody.design` described the folder as the
markdown-to-Word spec alone; it also holds `beta.md`, the beta lane, which is not
in the build chain and which nothing on entry depends on.

The fenced index still parses and the two-part profile is unchanged. The root
copy is the one edited; `bootstrap/CLAUDE.md` is the mirror and `push.bat`
overwrites it root -> clone on the next run.

**WITHDRAWN, same day — the claim above was false.** This entry originally
recorded that a session carrying the claude.ai Project cannot execute `shift.py`,
and a working arrangement was recommended on that basis. It is not true. A cloud
session runs the toolchain in its own container and moves files over the desktop
bridge. Tested 160826: `build.py` executed there against the current source,
passed all four guards — dollar-pairing, edition at
`110826_all_shortlink-names`, invertibility, register parse (apex 10, cabinet 8,
provinces 77) — and produced `GUIDE.txt` and `DIRECTORY.txt` byte-identical to
the copies on the machine. pandoc 3.1.3 and xelatex are both present.

The desk had one observation — no shell tool addressing the operator's machine —
and built "therefore a cloud session cannot run the pipeline" on top of it,
repeated it as settled across a dozen turns, and recommended restructuring the
working setup around it. It never ran the test, which took one command. Same
fault as the `/core` mechanism above and the `pushed: false` read out of the
bootstrap instead of off origin: an unexplained gap filled with a plausible
mechanism and reported as fact.

What is actually out of reach from a cloud session, tested rather than assumed:
deleting or moving files on the operator's machine, no tool existing for either;
and `git push`, this clone being unauthenticated. The docx was never built
locally in any mode — `build.py` defers it to CI via `seal.py`. Related and also open:
publishing the bootstrap as `go.fuzzylogic.page/boot` over
`main/bootstrap/CLAUDE.md`, which already serves as plain text and is mirrored on
every push. The Dub key does not exist yet, and an index entry written before the
key exists would repeat exactly the `/core` failure, so nothing was added here.


## 2026-08-11 — SHORTLINK LINES ALIGNED TO THE FILE NAMES; 110826_all_shortlink-names

Follow-on to `110826_all_guide-directory`, which renamed the two delivered
files but left the document naming the old shortlinks internally.

**Changed.** The GUIDE part self-identified as `go.fuzzylogic.page/core` and
the DIRECTORY part as `/reg`, in the body and in the YAML fence header. Both
now read `/guide` and `/dir`. The Sources block listed BLUE, REG and CORE; it
now lists **/blue**, **/guide** and **/dir**, and states that a shift needs
GUIDE and DIR and nothing else.

**Compatibility.** `/core` and `/reg` still resolve and move to the `shims:`
block in `index.txt` and `index.yaml`, alongside `status`, `refs` and `full`.
The operating document names only current links; the index carries the shim map.

**Stamp.** Bumped to `110826_all_shortlink-names`. `110826_all_guide-directory`
is pushed and live at b308601 with bot 6bca4dd, so amending content under it
would put one tag over two revisions — trap 2. The edition guard cannot catch
that case, because both parts would still agree with each other.

**Caught in passing: clear_pending.py failed silently on the last push.** It
matches `^- \d{4}-\d{2}-\d{2} `, so every pending entry must open with a date.
The four entries written for `110826_all_guide-directory` opened with a filename
instead, matched nothing, and the script printed "pending: already clear,
nothing to archive" and exited 0. push.bat continued, the lines rode into the
commit and stayed in Pending after the push — the exact condition trap 10 exists
to prevent, re-created by the entry format rather than by a missing step.
Those four are now moved to COMMITS-ARCHIVE.md by hand and Pending is rewritten
in the dated form; `clear_pending.py --check` sees all three current entries.

**Open.** `clear_pending.py` reports "already clear" both when Pending is empty
and when it cannot parse what is there. A line warning on unmatched `- ` entries
under the heading would separate the two. Not changed here.

**Verified.** build.py four guards PASS at the new tag; shift.py SHIFT READY.

## 2026-08-11 — TWO FILES RENAMED GUIDE + DIRECTORY; PART OPENING PRUNED; 110826_all_guide-directory

Two op-ruled deletions to the REGISTER part of `BLUEPRINT.txt`.

**Evidence.** The part tagline "the lookups" rendered as an orphan paragraph
at the foot of the last CORE page, below the closing `</state_log>` fence —
confirmed against the built volume. Cause: `SECTION_SUBTITLE` in
`build_bkp_compendium.py` keys on the four SECTIONS (CORE, PROCESSES, STATUS,
REFERENCES) and carries no entry for the PART, so the source paragraph never
reached `add_part_opening`'s subtitle path and fell through as body text.
The `status:` `note:` block was ruled off the page as spoiling it and not
reading; the content may be restated elsewhere.

**Verdict.** Both removed at source. `build.py` re-run: dollar-pairing,
edition, invertibility and register-parse guards all pass; register parses at
apex 10, cabinet 8, provinces 77. REGISTER.yaml/.txt 36,996 -> 36,839 bytes;
CORE.txt unchanged, both deletions being inside the REGISTER part.

**Stamp.** Bumped to `110826_all_guide-directory`, op-ruled. Scope is `all`:
the change reaches both files and the whole toolchain, not just the register.
Previous build `100826_reg_exemplar-sweep`.

**Also in this build: the two FILES renamed GUIDE and DIRECTORY.** The four
volume PARTS — CORE, PROCESSES, STATUS, REFERENCES — are unchanged and still
open exactly as before. Only the delivery layer moves.

**Why.** The part level had never had a name of its own and borrowed from its
own contents: `CORE.txt` opened `# CORE` and carried `## PROCESSES` at line 136,
so CORE meant both a file and a section inside it. That collision is also why
the part tagline had nowhere to render. And "register" is a false friend in a
style guide, where it first reads as tone and manner — line 19 previously ran
"The same rule governs the register:", which does not resolve until the clause
after the colon.

**Surface.** BLUEPRINT.txt seams, front matter and 15 prose references;
build.py (12); compile.yml (35, including the EXPECTED_ABSENT front-matter
pattern, which would otherwise have failed the coverage audit — caught by dry
run, not by inspection); build_bkp_compendium.py (1 line: the seam word now maps
to the internal component name, so nothing else in the builder moves);
shift.py (4); seal.py (3, including the seam regex, which would have FATALed
every seal); push.bat (3); index.txt/.yaml; CLAUDE.md (24). Old delivered files
CORE.txt, REGISTER.txt and REGISTER.yaml removed from the repo rather than left
in place — a superseded file that still resolves is how a dead path serves live-
looking content, which cost five weeks between 27 June and 10 August.

**Verified before push, not predicted.** pandoc 3.9 installed locally and the
full chain run: build.py four guards PASS; volume builds, register renders 345
leaf values / 388 paragraphs; coverage audit 209/212, 3 declared absent, 0
unexplained; block profile Header 55 / CodeBlock 4 / BulletList 15 /
OrderedList 2 unchanged, only Para 149 -> 148. shift.py SHIFT READY on the
renamed parts.

## 2026-08-10 — EXEMPLAR SWEEP OPENED; RETIRING A CATEGORY RULED; 100826_reg_exemplar-sweep

First cuts of a sweep through `references/foreign_people`, and a custody rule
extracted from the first of them. Stamp `090826_reg_part-opening` ->
`100826_reg_exemplar-sweep`, front matter and both seams, op-ruled: today's round
gets its own version. Quadrant `reg`. Built and sealed; NOT pushed. Five lines
stand in `COMMITS-PENDING.md`.

**Event.** Reading the register, the operator found `shortened_names` held a
single entry — "Cristina Kirchner: Drop 'de Fernandez' from the middle" — and
ruled it not a rule: a fact about one person, teaching no convention, under a
heading that named a group of one. Replaced by a `spanish` group carrying the
paternal-surname convention, exemplified by Gabriel Garcia Marquez (Mr Garcia,
not Mr Marquez). Accents dropped per the house no-diacritics form used for
Erdogan.

Kirchner was then entered at `status/global` on the criterion ruled earlier the
same day — a live figure whose wire form diverges from house form belongs where
the FLAG directives are — and struck within the hour.

**Evidence.** Four names were found dual-listed across both register branches by
a parse of `REGISTER.yaml`: Li Keqiang, Pope Emeritus Benedict XVI, King Salman
bin Abdulaziz al-Saud, King Jigme Khesar Namgyel Wangchuck. Also found: `house_form`
already appears inside `status` three times (Phiphat, Chaichanok, Chadchart), so
the branch split the register documents — status carries facts, references
carries forms — is already contradicted by its own data. Separately, Bashar
al-Assad sits in `references` as an `al-` prefix exemplar with no `status` entry
at all, despite an office change of exactly the kind the volatility test routes
to STATUS. The exemplar list has not been swept against STATUS and may hold more.

**Verdict.** Kirchner cut outright, both entries, out of the source altogether.
Two grounds, the second decisive and general: the entry predates the desk's
custody and has drawn no feedback across it; and the promotion route was invalid,
because she was only ever up for status by virtue of her old group being retired
underneath her. A category going extinct is evidence about the category, not
about its contents. Salvage is not merit.

Ruled into `RECORDS-AND-CONSOLIDATION.md` as **Retiring a category** — members of
a retired group are re-argued from scratch or they go, and the two questions that
decide it. That file's stamp bumped to `100826_all_retiring-a-category`.

Applied immediately to `royal_religious`, the next group down. Salman and Jigme
hold independent status entries and survive on their own footing. Benedict did
not, so his short form was moved to the fact rather than promoted alongside it:
the mortalities key now reads `Pope Emeritus Benedict XVI ("Pope Benedict")`.
The parenthetical sits inside the key deliberately — mortalities is a flat map and
a `house_form` field would have forced the entry to nest and break the pattern of
its own group. Benedict is single-homed.

**Dual listings then taken to zero**, op-ruled: no name in both branches. The
remaining three split for two different reasons and needed two different fixes.
Salman and Jigme carried genuine content on each side, and their status entries
are nested, so each took a `house_form` field — the Benedict fix without needing
the parenthetical, since nothing had to stay flat. Li Keqiang carried nothing:
"Surname first. Deceased; no honorific — see status branch" is a signpost, with
surname-first already stated in the group's `convention:` line and the
no-honorific case already carried by Mao and Deng. Deleted outright.
`royal_religious` emptied and was retired along with its note, which existed only
to explain a split that no longer exists. Verified by parse across both branches:
zero.

The branch note's "a name in both is not duplication" sentence now describes
nothing and can go on the next pass.

**Build.** All four guards pass — dollar pairing per paragraph, edition at
`100826_reg_exemplar-sweep` across all parts, invertibility byte-for-byte,
register parse at apex 10, cabinet 8, provinces 77. Source 63,941 chars; CORE
27,385; REGISTER 36,268 both forms. Sealed to
`Editions/100826_reg_exemplar-sweep/` — parts and pdf only. NO DOCX: the volume
is built by CI and pulled back by `seal.py` after a push, never built locally.
`Shift/` recut at the new build.

Open and NOT closed by this entry: the exemplar list is unswept, Assad is absent
from status, and the branch note's "a name in both is not duplication" sentence
still describes a condition being designed out.


## 2026-08-09 — REGISTER PART OPENING; 090826_reg_part-opening

Operator observed the gap at the CORE/REGISTER split and ruled the headings be
made to render as intended. Stamp `070826_all_rebuild` ->
`090826_reg_part-opening`, front matter and both seams. Quadrant `reg`.

**Event.** CORE opened with a shortlink line, an H1 and a sub-line above its
content. REGISTER carried the same three lines INSIDE its yaml fence, as
comments — so they rendered as code and part 2 had no heading in the volume at
all. The seam itself is an HTML comment and renders as nothing, so a reader saw
the end of the state log, a void, then a code block beginning cold. The gap the
operator reported was the symptom; the missing part opening was the cause.

**Applied.** REGISTER given the same opening above the fence: shortlink,
`# REGISTER`, sub-line "the lookups". The lines remain inside the fence too —
outside serves the rendered volume, inside serves `REGISTER.txt` read standalone,
which is the same arrangement by which `CORE.txt` carries its own seam and
shortlink when read alone. The two blank lines before each seam cut to one, both
seams, so the parts stay symmetrical.

**Evidence.** Checked BEFORE editing rather than after: `guard_invertible`
reassembles from raw slices — `preamble + "".join(parts)` — so any content added
between a seam and a fence round-trips by construction, and `register_yaml` reads
only the fence body, so `REGISTER.yaml` cannot be affected by lines above it.
Confirmed after the build: `CORE.txt` and `REGISTER.txt` diff clean against the
sealed `070826` edition once the tag string is normalised — nothing but the stamp
changed in either part. Byte counts moved 27,557 -> 27,562 and 36,301 -> 36,306,
exactly the five characters the longer tag adds. All four guards pass: dollar
pairing per paragraph, edition, invertibility byte-for-byte, register parse
(apex 10, cabinet 8, provinces 77). Heading count rises by one, so the structure
guard is not engaged — it fails only on a drop.

**A near-miss worth recording.** `build.py` reports CHARACTERS; the sizes the
desk had been carrying all session were BYTES from `stat`. The derived parts
appeared to lose 174 and 52 units and were briefly read as content loss. The
document is full of em-dashes, £, € and ¥, all multi-byte in UTF-8. Compare like
with like, and diff before concluding.

**Verdict.** Ruled, built, sealed to `Editions/090826_reg_part-opening/`, shift
folder re-cut, source copied to the clone. Not pushed.

## 2026-08-09 — CORPUS / DEPLOYMENT SUBSET DISTINCTION RULED

Operator ruled the distinction and the standing subset. `RECORDS-AND-
CONSOLIDATION.md` bumped `240726_all_records-extracted` ->
`090826_all_corpus-deployment-split`, new section added at the head.

**Event.** The `070826_all_rebuild` set was isolated into a deployment folder
for a working test shift. Eight files were named as the thing to deploy — the
source, the two derived parts, the artifact of record, the compendium pair and
the handoff. Only two of them are read by a processor editing copy. The rest
are custody, machinery or a build fixed in amber. Nothing in the corpus had
ever said which was which, so "the Blueprint" named both the whole holding and
the working set, and a deployment could take either.

**Ruled.**

- The corpus is everything the desk holds. The deployment subset is what a
  processor receives to work a shift. A file is corpus by being held; it enters
  the subset by being needed at the point of edit.
- **Artifacts of record do not deploy.** The PDF and the volume exist to be
  read by a human and to fix a build in amber. They are the least current thing
  in the corpus the moment the source moves, and they carry no seam a processor
  can check.
- **Standing subset: the two parts, most recent version, in text format —
  `CORE.txt` + `REGISTER.txt`. Nothing else.** `BLUEPRINT.txt` substitutes for
  the pair where a destination takes one file. CORRECTED LATER THE SAME DAY: the
  desk first wrote the subset as `CORE.txt` + `REGISTER.yaml`. The operator ruled
  text format. The extension is inert and the bytes are identical, but `.yaml` is
  the authoring form and `.txt` is the delivered one, and the subset names what
  travels.
- **Confirmed latest** is a checked tag, not a filename or a modification date —
  clone and remote go stale in opposite directions, and a matching tag proves
  structural agreement and nothing about content.

**Consequential edits, same file.** Two lines still named the four-part set,
retired by the CORE + REGISTER ruling of 070826. The clone-write protocol now
names `BLUEPRINT` as the only file edited. The close-out bullet loses its short
file: `STATUS` was the one small enough to reprint whole, and the merge leaves
`BLUEPRINT`, `CORE` and `REGISTER` all large, so patches are now the only form.
The per-model deployment sentence moved into the new section, where the subset
it draws from is defined.

**Evidence.** Guards re-run against the isolated set on 090826, all passing:
edition — both seams and the front matter read `070826_all_rebuild`;
invertibility — `CORE.txt` is a verbatim substring of the source, and the
register lifts out of its fence and reconciles against `REGISTER.yaml` line for
line below the seam line, the documented HTML-comment / YAML-comment swap being
the only difference; register parse — two top-level keys, `status` and
`references`; dollar-pairing per paragraph — two `$` in the document, no
paragraph holding both. `REGISTER.txt` and `REGISTER.yaml` byte-identical,
md5 `9954d821…`. All eight copies checksum-matched to source.

**Verdict.** Ruled and applied to the clone. Not pushed. The subset itself
cannot ship as confirmed-latest until the push lands — the shortlinks still
serve `010826`, so a cache-busted fetch today returns the four-part build, not
this one. For today's shift the subset is taken from the local set.

**Same session, desk decision under standing "file management is your call".**
`Project_Space\CLAUDE.md` created — durable routing, read on entry to the folder.
Establishes which of the two roles an agent is in (desk, governed by the subset;
custody, governed by RECORDS-AND-CONSOLIDATION), maps every location and its
purpose, and carries the six standing traps. Placed at the Project_Space root,
outside the clone, so it never rides a push and the compile job cannot see it.
It holds no rule not stated in the document it points at; where the two disagree,
RECORDS wins. FINDING RECORDED THERE: `pipeline-registry\Blueprint\` is still the
four-part `010826` shape — the 070826 rebuild has never been written into the
clone, so an agent reading the clone or resolving any shortlink gets the old
build while the root carries the new one.

**DELETION SWEEP, same day.** The shift folder `The Blueprint 2/` was cut to the
subset, the operator confirmed the content taken, and it was retired. No content
lost: both files verified identical to the root pair and to the sealed edition
before the move. Consequent ruling — **the shift folder is cut as a matter of
course on every build, under the standing name `Shift/`, and deleted on
confirmation.** It is a copy and never a source, so its deletion can never lose
anything, which is what makes cutting one routine rather than a decision.

**FALSE TRAP RECORDED AND WITHDRAWN, same day.** The desk found the shift folder
empty after the move and concluded that `mv` on a directory deletes its contents
on this mount, writing that into the bootstrap traps as established fact. It was
wrong. The operator had taken the two files out and placed them for use, which is
what the folder exists for. Withdrawn from the traps and replaced with the
failure it actually demonstrates: do not infer a system fault from an operator's
own action. A false trap is worse than no trap — the next session inherits it as
settled and has no way to falsify it. `rm` remains blocked on this mount; `mv`
works, unqualified.

**PUSH REJECTED, same day — non-fast-forward.** The operator ran `push.bat`;
commit 41cc572 was created and the push refused, the remote holding compile-bot
commits the clone did not have. Nothing published. Cause is structural:
`compile.yml` commits the derived parts to `main` itself, so the clone is behind
after every build it triggers, and `push.bat` had no integration step. Recorded
in handoff 070826 §0 as an observation on 080826 and never fixed. `push.bat` now
fetches and rebases onto `origin/main` before pushing, and aborts on conflict
rather than resolving one — derived files being the likely site, and a
hand-resolved derived file being exactly what the CI guard rejects.

**Detection worked.** Three cache-busted fetches with distinct busters —
`index.txt`, `index.yaml`, `prompts/system.md` — all returned the pre-push state,
`system.md` empty against 605 bytes local. The desk reported the divergence and
sought a second signal rather than declaring a repository fault on it, and the
operator's `push.bat` output settled the cause in one step. This is the §0
procedure behaving as designed, and the corrective against the 070826 incident
recorded at §8, where a stale read was held live for hours as a finding about the
repository.

**Open, unchanged from handoff 070826 §5.** Pull integrity still has no home;
`Blueprint/prompts/system.md` and `prompts/instructions.md` remain zero bytes,
so the conditions travel only as prose in the handoff. No rule-loss diff has
been run, old build against new. `index.txt` / `index.yaml` repaired locally
and not pushed.

## 2026-07-31 — SWEEP: OUT-07, ARC-13 ruled and deployed

Operator swept the open ledger for simple drop-ins. Two ruled and executed
into `Blueprint/BLUEPRINT.txt` (CORE), edition stamp
`270726_all_records-extracted` -> `310726_com_hedges-rule-home` across the
master and all four part stamps.

- **OUT-07 — Hedges are not length candidates.** New subsection under CORE
  Legality & Quotes. A hedge in filed copy is a liability position, not a
  length candidate; the overspill recast may not remove it. Preserve as
  filed, flag the claim for desk sourcing, find the characters elsewhere.
  Extends the existing "Retain hedges, eg allegedly" bullet from bare
  instruction to reasoned rule, on the asymmetric-failure argument.
- **ARC-13 — One rule, one home.** New subsection closing the CORE Authority
  Hierarchy. Where a rule and its exception straddle PROCESSES and
  REFERENCES, the rule is stated once in its sectional home; the register
  entry carries entity + exception + pointer, never a second statement that
  can drift.

Both pruned from `DECISIONS-OPEN.yaml`. Logged in `COMMITS-PENDING.md`;
awaiting operator push. Keys not reused.

**Considered and left open:** VER-05 (already ruled 150726, scope-narrowed to
Claude-lane practice, explicitly NOT Blueprint doctrine — deploying it would
contradict the ruling); VER-04 and ARC-04 (already live in the served text);
LEN-13 (own entry records the cause as unknown); NAM-09, ARC-01/06/11/14/15/16,
OTH-12/13 (architecture or undefined triggers — not drop-ins).

**Open findings this session, no action taken:**

1. The raw URLs in the operator's saved shortlink block point at
   `Blueprint/BLUEPRINT.md` and `Blueprint/PROCESSES.md`, deleted in the
   270726 restructure. The shortlinks themselves are correct (repointed to
   the `.txt` targets); only the written-out raw URLs are stale. A model
   handed that block fetches a dead path — and the proxy serves an
   18-day-old cached copy of the deleted file rather than a 404, so the
   staleness is silent. Fourth cache incident in the VER-05 series
   (150726, 160726, 310726).
2. The DOCX cover builder consumes the source metadata line and does not
   print the edition slug on the cover. Every Word companion therefore
   ships with no version identity on its face — against VER-05 doctrine,
   where the slug line has been the only detector in all three cache
   incidents. Pre-existing; affects the shipped build equally.
3. `compile.yml` builds `BLUEPRINT.docx` unstyled because
   `Blueprint/reference.docx` still does not exist (noted 240726, still
   true). The styled build requires a local run of
   `tools/build_bkp_compendium.py` against a reference docx.
4. `tools/build_bkp_compendium.py` and `audit_bkp_compendium.py` default
   `--pandoc` to a hardcoded Windows path, and the table parser requires
   pandoc >= 2.10 (pandoc-types 1.21 table AST). Both fail on any other
   host without an explicit `--pandoc`.

## 2026-07-11 — REGRESSION CAUGHT AND REVERSED (GATE 1 bulk-swap erasure)

Today's GATE 1 robocopy overwrote the push clone with the older Cowork
mirror and the push published the regression. Erased and now RESTORED
from git (f88ad11^): REFERENCES 040726 full-length recompile (Sections
5 Organisations + 6 Vocabulary, incl. 2026-07-04 Chatichai Choonhavan
entry, full province list); BLUEPRINT 020726 integrated SEARCHQ
doctrine (search triggers) and the 2026-07-04 clone-write protocol
paragraph. Today's rulings re-applied on top (Khamenei note, Gemini
default). STATUS and PROCESSES audited clean — current versions are
genuine supersets. Root cause: same-tag-different-content copies plus
bulk file-swap without a COMMITS-PENDING check. GATE 1 and the Cowork
mirror are retired by the folder migration; clone is now the single
working base. Restoration awaits operator push — check COMMITS-PENDING
first, per protocol.

## 2026-07-11 — TXT MIRRORS + COMPILED SET ESTABLISHED (op instruction)

Standing practice from today: every Blueprint master carries a .txt
twin (BLUEPRINT.txt, PROCESSES.txt, STATUS.txt, REFERENCES.txt),
regenerated whenever the master changes. COMPILED.txt concatenates all
four in companion order (BLUEPRINT, PROCESSES, STATUS, REFERENCES),
refreshed monthly or on major change; internal tag carries the date
(current: 110726_compiled_full). Stable filenames — raw URLs never
change. All five ride the normal GATE 1/2 push. Maintainer: architect
(Claude).

## 2026-07-11 — SHIFT RULINGS DEPLOYED TO MIRROR (register session)

Operator ruled and Claude applied to mirror copies (pipeline-registry/
Blueprint) — live on GitHub only after operator runs GATE 1 + 2:

- STATUS -> 110726_status_iran-chain-suriya-chadchart.yaml: Ali
  Khamenei assassinated Feb 28 2026 + Mojtaba Khamenei supreme leader
  Mar 8 2026 (apex, web-verified); Pol Maj Gen Suriya Singhakamol ONCB
  secretary-general (rank verified via bangkokpost.com); Chadchart
  placeholder resolved — re-elected Jun 28 2026, second term.
- PROCESSES -> 110726_pro_intro30-titlecaps-shortheads-pr.md: 30-word
  soft limit for news intros (Kevin's rule, ruled as soft, news only);
  title caps before full names now the GENERAL rule (senator/governor/
  mayor/deputy-spokesperson exceptions swept in; BKP usage check
  supports); Michael's short-sharp-heads preference permanent in DCX
  trigger note; single-newline counting note added to Route A; PR
  [Head]/[Deck] 90/120-char rule sunk to Part 3.
- BLUEPRINT -> 110726_com_searchq-restored-gemini-default.md: mirror
  copy was STALE — missing the entire Relay search (SEARCHQ) section
  present in the live GitHub copy under the same 270626 tag. Section
  restored from live raw, with operator ruling applied: Gemini default
  destination (VER-04 partial ruling, noted in ledger).
- REFERENCES -> 110726_refs_khamenei-exemplar-note.yaml: Khamenei
  exemplar marked deceased/structural, ruling retained.

Open: Mojtaba Khamenei BKP title form (Ayatollah y/n) — no precedent.

## 2026-07-02 — OPEN LEDGER ESTABLISHED (op instruction: one file only)

DECISIONS-OPEN.yaml created in project folder: the single standing
intake for candidate rule changes/amendments/refinements. Keys continue
the LEN/NAM/ARC/OUT/VER/STA/OTH series (next-keys header inside).
Operator sweeps periodically; ruled entries executed, sweep logged
here, closed entries pruned from the ledger. Seeded with the five open
threads (NAM-09, ARC-01, ARC-04, ARC-06, ARC-11) plus first new
candidate ARC-13 (rule/exception register pattern from the NAM-07
dedupe). Records & Consolidation in both homes now names the ledger.
Batch files 1–5: closed, archive on next push.

## 2026-07-02 — DEPLOYED-TRIO RULING (STA-01 stays; NAM-10/11 out)

- STA-01 KEEP — op-confirmed (earlier wipe was op error); "cabinet"
  lower case stands in Title capitalisation, both homes.
- NAM-10 nationality + NAM-11 Veera/Kavi REMOVED from both homes
  (op: serve no purpose). Both had been deployed earlier today; index
  cross-ref updated. Rulings preserved in batch2 yaml if ever needed.
- VER-01 resurfaced for op review (dateline/credit clause currently
  folded into the new Datelines convention).

## 2026-07-02 — BATCH 5 REOPENERS (4 entries flipped WIPE -> ADD)

Operator returned rulings post-sweep; all four deployed to both homes:

- OTH-01 general flag principle ("ask about it, but don't alter" —
  across ALL flagging) -> Rules of the Protocol.
- OTH-03 British "on" before weekdays; trust local temporal forms;
  "deeply entrenched" no hyphen -> Dates.
- OTH-04 refined: datelines left exactly as provided, never added,
  never localised; agency credits never stripped -> new Datelines
  convention, Part 1.
- OTH-11 strengthened: default to "I don't know" over generation of
  ANY kind -> Operating Doctrine, beside Communication.

## 2026-07-02 — REGISTER SWEEP COMPLETE (op: unmentioned = deleted)

All entries unmentioned in operator returns closed as WIPE. Final
census of 61: 46 WIPE, 5 KEEP, 1 KEEP+REFINE, 4 ADD (deployed),
2 DISCUSS (NAM-09 site-search metric, ARC-06 per-model prompts),
1 IN PROCESS (ARC-01), 1 WATCHING (ARC-11), 1 AWAITING RULING (ARC-04).

Wipe classes recorded per entry in the yaml: 30 already-live in guide,
3 deployed 2026-07-02 and rules STAND (NAM-10 nationality, NAM-11
Veera/Kavi, STA-01 cabinet), 13 DISCARDED never deployed (incl. LEN
wipes; notable discards: ARC-07 no-naked-ladies, OTH-02 never-add-
identity, OTH-04 BEIJING datelines, OTH-09 PHUKET colon quirk).

Register scaffolding retained as audit trail; zero PENDING remain.
Batch files are candidates for archive on next push.

## 2026-07-02 — BATCH 3 (ARCHITECTURE) PARTIAL SWEEP (5 of 12 ruled)

- ARC-01 IN PROCESS (modular over monolithic).
- ARC-04 explanation requested and given; ruling awaited.
- ARC-06 DISCUSS — in planning: per-model deployment prompts /
  best-use guides project.
- ARC-10 KEEP — correct naming theory.
- ARC-11 WATCHING — op observing single-day multi-edits in practice;
  not worth clarifying yet.
- ARC-12 KEEP — op-confirmed: versioning encouraged as
  fallback/recovery-only tool (ARC-12 interpretation confirmed).
- Unruled: ARC-02, 03, 05, 07, 08, 09 (+ ARC-04 awaiting ruling
  post-explanation).

Also this session: rule/exception dedupe pattern established (NAM-07):
rule in its sectional home, register carries entity + exception +
pointer. Candidate standing convention.

## 2026-07-02 — BATCH 2 (NAMES) PARTIAL SWEEP (7 of 14 ruled)

Operator verdicts written into DECISIONS-batch2-NAMES.yaml:

- NAM-04, NAM-06 ADD — already deployed this morning; verdicts closed.
- NAM-07 KEEP — rule was stated TWICE (PROCESSES + REFERENCES, both
  homes). Op-correction: duplication itself was the fault. REFERENCES
  entries reduced to the Suu Kyi exception with a pointer; the rule now
  lives once, in PROCESSES. Compendium verified: 1 statement.
- NAM-09 DISCUSS — mandatory bkp site-search per name: trigger and
  recency/volume metric undefined; open.
- NAM-12 ADD — changes-only rule made explicit in STYLE LOG Mandatory
  (both homes): confirmed-correct is silence; a line is earned by a
  verified change or an open flag.
- NAM-13 ADD — keyed INDEX added to compendium front: full contents map
  plus cross-section dependency notes (honorifics 5-place trap,
  proximity, spatial, legality, identity).
- NAM-14 KEEP+REFINE — "legality queries are logged and handed up;
  they never delay the edit" added to Legality & Quotes (both homes).

Still PENDING: NAM-01, 02, 03, 05, 08, 10, 11 (7) + batches 3–5.
Register: 42 PENDING.

## 2026-07-02 — BATCH 1 (LENGTH) VERDICT SWEEP

Operator ruling: all 12 LEN entries redundant or acted on except two.
Verdicts written into DECISIONS-batch1-LENGTH.yaml (0 PENDING remain):

- LEN-08 KEEP — condensed into PROCESSES DCX section (both homes):
  budget number is a TOTAL across lines; may not populate until paste;
  confirm against the rendered figure.
- LEN-10 KEEP — elevated to GENERAL editing guidance (Editing Scope,
  both homes): default target of every edit is land just over, never
  under. Model's observed drift is to cut slightly under — a fault to
  correct, not caution. (Prior "land under" wording was a model
  invention, corrected 2026-06-29.)
- LEN-01–07, LEN-09, LEN-11, LEN-12 WIPE — redundant or acted on.

Register now 49 PENDING (batches 2–5).

## 2026-07-02 — RECONCILIATION (gap rulings folded in)

Content home confirmed: project folder + pipeline-registry mirror,
manually pushed to GitHub (powers the go.fuzzylogic set). Drive is
history, not home.

Patched into **THE BANGKOK POST BLUEPRINT 2026.md** AND
**pipeline-registry/Blueprint/PROCESSES.md** (each anchor verified x1):

- NAM-04 honorific requires a surname in copy
- NAM-06 deputy ministers capped title; deputy spokespeople not
- STA-01 "cabinet" lower case, always
- NAM-10 nationality stated once public; never guessed
- NAM-11 fluent contributors (Veera, Kavi) lightest touch
- LEN-09 sub-head removal: body inherits the freed footprint

Patched into both BLUEPRINT homes (compendium + mirror BLUEPRINT.md):

- ARC-06 per-model self-contained deployment prompt

Compendium PART 2 SPATIAL MECHANICS: stale marked-overspill/1-in-1-out
section REPLACED with mirror's current overspill-python revision
(recast-by-value, Route A verified len() count / Route B substitution).
Compendium now 66,374 B.

**Flags for operator:**

- 61 decisions register verdicts still PENDING (count corrected from 62;
  triage list produced 2026-07-02) — ratify or defer.
- RESOLVED 2026-07-02 (op-ruling): FOOTPRINT-LOCKED / FREE-EDIT
  deprecated for laid-out content — laid content cannot be assumed to
  fit; fit assessment belongs in the edit brief. "Fits" is the
  descriptive and instructional alternative: story is placed AND the
  presented layout incorporates all the text — no footprint alteration.
  True ~2–3 times in 10; otherwise an adjustment of no fixed or
  predictable size. Live PROCESSES wording already conforms.
- Root PROCESSES.md (280626_pro_new-overspill) is an OLDER working copy
  diverging from mirror PROCESSES.md (290626_pro_overspill-python).
  Candidate for archive to avoid a fresh branch problem.
- Mirror edits are local until the next manual GitHub push; go.fuzzylogic
  links serve the old text until then.

## 2026-07-02 — ANOINTMENT

**THE BANGKOK POST BLUEPRINT 2026.md** (this folder, 59,489 B, 1,260
lines, modified 2026-07-02) is the authoritative version going forward.
Operator-confirmed (Chun, this session). Unified compendium of the
four-document set: BLUEPRINT, PROCESSES, STATUS, REFERENCES.

**Known gap at anointment (audit pending):** grep against the decisions
register shows these recorded rulings NOT yet in the compendium:

- FOOTPRINT-LOCKED / FREE-EDIT terminology (deprecates placed/unplaced)
- Programmatic len(text) character counting (supersedes model estimation)
- NAM-10 nationality-once-public
- NAM-11 Veera/Kavi light-touch
- LEN-09 subhead space reallocation
- STA-01 "cabinet, never Cabinet"
- ARC-06 per-model deployment-ready self-prompts

Present and confirmed: To Lam status, Saksayam clearance, Proximity
Alert (4 mentions). Verdict: authoritative but INCOMPLETE until
reconciled against DECISIONS-batch1–5 and the Editorial Standards gdoc.

## 2026-07-02 — LINEAGE SURVEY (Google Drive)

Connector cannot read Google Docs revision history; lineage derived from
create/modify stamps and content diffs.

| Branch | Earliest | Last content edit | Copies | Verdict |
|---|---|---|---|---|
| System Prompt=BKP Style Guide Compact-2026-optimised.txt | 2026-04-08 | 2026-05-01 | 11+ | MISFIRE — carries superseded rules (1-in/1-out trim, flag relative dates, identity-if-relevant) |
| BKP_STYLE_GUIDE_2026_(CLINICAL_FORMAT).md (+ "(1)" variants) | 2026-04-11 | 2026-05-07 | 8+ | MISFIRE — same era, same superseded rules |
| Editorial Standards and System Operations Guide 2026 (gdoc, id 1x3aam67On_5pW7rp7-hGmXC8EEc4JztoXuXgP2KHleI) | 2026-06-29 | 2026-06-29 | 1 | KEEP — decisions digest (LEN/NAM/ARC/OUT/VER/STA/OTH, verdicts PENDING); source material for reconciliation, not the master |
| THE BANGKOK POST BLUEPRINT 2026.md (local) | — | 2026-07-02 | 1 | **AUTHORITATIVE** |

Note: mass-copy sweep 2026-06-28 18:31–18:46 UTC scattered ~12
byte-identical duplicates of the two misfire families across a dozen
Drive folders. Duplicates are noise, not ve
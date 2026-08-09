# VERSION HISTORY — BKP STYLE GUIDE / BLUEPRINT

Running log of document lineage. Mitigation against lost context and
cross-workspace blind spots. Append-only: newest entry first. Every
anointment, supersession, deletion sweep and audit gets an entry.

Convention per entry: date (YYYY-MM-DD), event, evidence, verdict.

---


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
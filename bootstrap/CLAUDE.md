# BOOTSTRAP — Project_Space

**Read this first, every time. It is the most important document in the folder.**

Not because it outranks anything — it holds no rule that is not stated somewhere
else, and where it disagrees with the document it points at, that document wins
and this one is wrong. It is the most important document because it is the only
one that tells you *which* document to open. Without it, a session begins by
asking the operator what the project is and what to do with its contents. That
has happened. The bootstrap is the fix.

Everything below the fence is machine-readable. Lift it and you have the whole
folder as data: every path, what it is, whether it deploys, whether it may be
edited by hand.

---

## On entry — do this before anything else

```
python3 shift.py
```

It cuts or refreshes `Shift\` — `CORE.txt` + `REGISTER.txt`, copied from the
confirmed-latest parts at the root. Idempotent: if the folder is already correct
it writes nothing; if the operator has taken the files, it puts them back. It
refuses to cut a set whose parts disagree on their build tag.

**Run it unprompted, at the start of every session.** The operator's side is zero
touch: they open the project and the shift folder is ready. Do not ask whether to
cut one, and do not wait to be told the previous set was taken — an empty or
absent `Shift\` is the normal resting state between shifts, not a fault.

---

## What this project is

The **Blueprint** is the governance document a processor is given to subedit
copy for the Bangkok Post. It is **one document in two parts**:

| Part | Carries | Syntax | Delivered as |
| :---- | :---- | :---- | :---- |
| **CORE** | core + processes | markdown | `.txt` |
| **REGISTER** | register + status | YAML | `.txt` |

**The extension is inert.** Nothing in the chain reads it: pandoc is told the
format explicitly and raw.githubusercontent serves every extension as
`text/plain`. **The syntax is load-bearing and is not optional** — it is what
makes headings headings in the rendered volume, and what lets the register be
parsed.

**One file is edited by hand: `BLUEPRINT.txt`.** It carries both parts, the
register fenced as YAML inside it. Everything else is derived by `build.py`
locally, or by `compile.yml` on push. A hand-edit to a derived file is rejected
by CI.

Current build: **`070826_all_rebuild`**.

## What a shift needs

**`CORE.txt` + `REGISTER.txt`, most recent version. Nothing else.**

Every build cuts a `Shift\` folder holding exactly those two, as a matter of
course. It is deleted once the operator confirms the content has been taken. The
folder is a copy and never a source, so its deletion can never lose anything —
that is what makes cutting one routine rather than a decision.

`BLUEPRINT.txt` substitutes where a destination takes one file. Artifacts of
record — the PDF, the compendium volume — never deploy: they fix a build in
amber and carry no seam a processor can check.

**Confirmed latest is a checked tag**, not a filename and not a modification
date.

## Stop words

Two, and they mean different things. Neither is a complaint; both are
instructions and both take effect immediately.

**WRAP** — the usage budget is nearly gone. Stop starting things. Secure what
exists: write the state down where a cold session will find it, name what is
done, what is half-done and what has not begun, and say plainly what is not
pushed. Do not begin a new edit, do not start a build, do not open a new file.
A tidy stopping point beats a finished thought.

**CHECK** — the operator believes what you are doing may be at odds with the
task. It is a concern, not a verdict: you may be right and they may be right.
Stop the work and say what you understood the task to be, what you are doing,
and why. Do not defend the work and do not immediately capitulate — both waste
the signal. Establish where the two readings diverge, then let them rule.

A bare "stop" means WRAP unless the context says otherwise.

## Which job you are in

Establish this before acting. Two roles, two governing documents.

| Role | You are | Governed by |
| :---- | :---- | :---- |
| **Desk** | subediting filed copy — heads, decks, fit, house style | `CORE.txt` + `REGISTER.txt`. Nothing else. |
| **Custody** | changing, building, recording or shipping the documents | `pipeline-registry\RECORDS-AND-CONSOLIDATION.md` |

Most work here is custody. The desk job is what the corpus exists to serve, not
what is usually happening in this folder.

**Custody has no authority over content.** File management is your call; rules
are not. Never touch the clone without an operator ruling.

## Your duties, per turn

From `RECORDS-AND-CONSOLIDATION.md`. Read it in full before your first write to
the clone.

* A ruled change goes into the clone **on the turn it is ruled**, and gets one
  line in `COMMITS-PENDING.md` on the same turn. The operator checks that list
  before every push — it is the guard against a bulk file-swap silently erasing
  a desk commit. Lines clear **on** the push, in the same commit as the work.
* Unruled candidates go to `DECISIONS-OPEN.yaml` under the standing key series
  (LEN/NAM/ARC/OUT/VER/STA/OTH). Nothing there is authoritative until ruled.
* Anointments, supersessions, deletion sweeps and audits get a
  `VERSION_HISTORY.md` entry — newest first; date, event, evidence, verdict.
* At close, hand back patches, not full reprints. No part is small enough to
  reprint whole.

## The repeatable sequence

Any future change to the Blueprint runs in this order. It is the same sequence
whether the change is one word or a restructure.

1. **Orient.** Read this file. Lift the fence. Resolve the paths.
2. **Establish the role.** Desk or custody.
3. **Get a ruling.** Unruled candidates go to `DECISIONS-OPEN.yaml` and stop
   there.
4. **Edit `BLUEPRINT.txt` at the root.** Never a derived file.
5. **Run `build.py`.** Four guards: dollar-pairing per paragraph, edition,
   invertibility, register parse. All must pass.
6. **Seal the edition** into `Editions\<tag>\` — every format, outside the clone.
7. **Copy `BLUEPRINT.txt` alone into the clone.** CI derives and commits the
   rest. Copying a derived file trips the hand-edit guard and the push is
   rejected.
8. **Log it** — one line per change in `COMMITS-PENDING.md`, an entry in
   `VERSION_HISTORY.md`.
9. **Operator pushes** via `push.bat`, having checked `COMMITS-PENDING.md`. It
   mirrors the bootstrap set, rebases onto origin, pushes, then runs `seal.py` —
   which waits for the compile job, pulls the Word volume back and completes the
   edition. The docx is never built locally.
   **Clear the lines you are pushing before the commit is made.** Nothing does
   this for you — see trap 10.
10. **Cut the shift folder.** `Shift\` at the root, holding exactly `CORE.txt` +
    `REGISTER.txt` copied from the confirmed-latest parts. This happens as a
    matter of course on every build, not on request. Nothing else ever goes in
    it, nothing is ever edited in it, and it is never a source.
11. **Delete it** on operator confirmation that the content has been taken.
    Then update this bootstrap if any location or purpose moved.

## Working on design

Iterate on one element, not the volume. Return the single page or component
being changed — `build_bkp_compendium.py --component`, or the affected page
pulled out of the PDF — and hand back the full document once, at the end, when
the element is settled. A 29-page rebuild per tweak buries the change being
judged and spends the budget on pages nobody is looking at.

Same rule in prose: answer the question asked. Do not re-explain the surrounding
process, and do not reprint what has not changed.

## Standing traps

Each has fired at least once. They are why the procedure reads as it does.

1. **Both sources go stale, in opposite directions.** The clone lags the remote;
   the remote's raw address serves a cache. Appending any query string returns
   the current file. `git log -1` against a cache-busted fetch settles it.
2. **A matching build tag does not mean matching content.** One tag can cover two
   revisions. Tag-matching catches structural skew and nothing else.
3. **`$` deletes text.** The markdown-to-docx converter reads `$…$` as inline
   maths and eats what is between. The hazard is per **paragraph**, not per line.
   Two remain in the document, one per paragraph, both deliberate.
4. **Bulk file-swap has erased desk commits.** Hence `COMMITS-PENDING.md`.
5. **`rm` is blocked on this mount.** `mv` works. That is what `_pending-delete\`
   is for.
8. **Do not infer a system fault from an operator's own action.** On 090826 the
   desk found the shift folder empty, concluded that `mv` on a directory deletes
   its contents on this mount, and wrote that into these traps as fact. The
   operator had simply taken the files out for use, which is the entire purpose
   of the folder. A false trap is worse than no trap: it is unfalsifiable by the
   next session, which inherits it as settled. Establish the cause before
   recording one.
6. **The register must stay fenced.** Unfenced, every `#` becomes a markdown H1
   and the indentation carrying the structure is lost to paragraph merging.
7. **CI rejects hand-edited derived files.** `Blueprint/CORE.txt` and
   `Blueprint/REGISTER.*` are regenerated; changing them by hand fails the push.
10. **`COMMITS-PENDING.md` is never cleared, so it stops being a guard.** The
    rule says lines clear on the push. No step does it: `push.bat` does not touch
    the file, and the desk is a fresh session every time, so the job belongs to
    nobody. Found 100826 holding **71 entries back to 4 July**, of which about
    sixty were long published — the 4 July Chatichai line was still pending with
    its change committed to the clone since 9 August. A list that is nine parts
    changelog cannot be scanned before a push for the one thing it exists to
    catch, a bulk file-swap eating a desk commit. The list fills at session rate
    and empties never. Clear the lines you are pushing as part of the same
    commit; the lineage is `VERSION_HISTORY.md`'s job, not this file's. Fixing
    `push.bat` to do it is open — the trap is that clearing must happen before
    the commit, so a failed push leaves lines cleared for work that never went.

9. **The clone is behind after every build.** `compile.yml` derives the parts and
   commits them to `main` itself, so any build the desk triggers leaves the clone
   one commit short. A push that does not integrate that first is rejected as a
   non-fast-forward — and `push.bat` reports `[FAIL] ... Nothing was published`,
   which is accurate and easy to misread as a fault in the work. `push.bat` now
   fetches and rebases before pushing. It aborts on conflict rather than
   resolving one: where the conflict is a derived file, origin's copy wins.

---

## The index

Lift the fence to parse. `deploys: true` marks the shift subset. `hand_edit: true`
marks the only file a human may change.

```yaml
# PART: 090826_bootstrap INDEX
# Paths are relative to Project_Space. Read with the prose above; neither is
# complete alone.

build: 090826_reg_part-opening
previous: 070826_all_rebuild    # pushed 090826, commit 8a4d4ff + bot c7bca93
pushed: false                   # 090826_reg_part-opening is not pushed
serving:
  status: LIVE — the whole chain, verified 090826 by contents API against local sizes
  bot_commit: c7bca93        # compile-bot, the derived parts
  note: >
    CORE.txt 27557 and REGISTER.txt/.yaml 36301 on the remote, byte-for-byte the
    local parts. PROCESSES.txt removed by the job. The shims are genuine copies,
    not stale files: STATUS.* and REFERENCES.* all share one blob sha with
    REGISTER.yaml, and COMPILED.* shares one with BLUEPRINT.txt. Manifest
    rebaselined at the two-part profile — Header 54, components CORE + REGISTER.

working_set:
  purpose: the current text. The root of this folder is authoritative.
  files:
    BLUEPRINT.txt:
      role: source
      syntax: markdown, register fenced as YAML inside it
      hand_edit: true
      deploys: substitute      # where a destination takes one file
    CORE.txt:
      role: derived, verbatim slice
      contains: core + processes
      syntax: markdown
      hand_edit: false
      deploys: true
      link: /core
    REGISTER.txt:
      role: derived, byte-identical to REGISTER.yaml
      contains: register + status
      syntax: yaml
      hand_edit: false
      deploys: true
      link: /reg
    REGISTER.yaml:
      role: derived, authoring form
      hand_edit: false
      deploys: false
    BLUEPRINT.pdf:
      role: artifact of record
      hand_edit: false
      deploys: false
    build.py:
      role: source -> the derived four
      guards: [dollar-pairing per paragraph, edition, invertibility, register parse]
    shift.py:
      role: the derived parts -> Shift/
      run: on entry to the folder, unprompted, and on every build
      guards: [parts agree on build tag, no stray file in Shift/]
      flags: [--check]
    seal.py:
      role: after a push — wait for CI, pull the volume back, seal the edition
      run: called by push.bat on a confirmed push; safe to re-run by hand
      note: >
        The docx is NOT built locally and must not be. CI builds it and commits
        it; pushing a local one means CI rebuilds over it and the next rebase
        hits a binary conflict. So the volume comes back rather than going out.
      guards: [clean tree, rebase clean, volume stamp matches the build tag]
      flags: [--no-wait]

shift_folder:
  path: Shift/
  cut_by: shift.py          # run on entry, unprompted. Operator side is zero touch.
  purpose: exactly what is needed to work a shift, and nothing else.
  contents: [CORE.txt, REGISTER.txt]
  lifecycle: >
    Regenerated on entry and on every build, from the confirmed-latest parts.
    Idempotent — already correct writes nothing, taken files are put back. An
    empty or absent Shift/ is the normal resting state between shifts, not a
    fault, and needs no confirmation before refilling. It is a copy and never a
    source: nothing is edited there and nothing unique ever lives there.
  history:
    - The Blueprint 2/ — cut 090826, taken by the operator, retired 090826.
      Superseded by the standing Shift/ folder and shift.py the same day.

editions:
  path: Editions/
  purpose: sealed builds, outside the clone. Artifacts of record.
  current: Editions/090826_reg_part-opening/
  sealed:
    070826_all_rebuild: complete — parts, pdf, and the docx/pdf volume pair
    090826_reg_part-opening: >
      parts and pdf only. NO DOCX. build.py does not build one — it writes the
      parts and renders BLUEPRINT.pdf. The Word volume comes from
      tools/build_bkp_compendium.py, which runs in the compile job, so no docx
      exists for a build until it is pushed and CI has run. Seal the volume into
      the edition after the push, not before.
  what_build_py_writes: [CORE.txt, REGISTER.yaml, REGISTER.txt, BLUEPRINT.pdf]

custody:
  path: pipeline-registry/
  purpose: the git clone. What gets pushed.
  files:
    RECORDS-AND-CONSOLIDATION.md:
      role: YOUR RULES. Custody procedure.
      stamp: 090826_all_corpus-deployment-split
    COMMITS-PENDING.md:
      role: desk changes awaiting push, one line each. Checked before every push.
    VERSION_HISTORY.md:
      role: lineage. Append-only, newest first.
    DECISIONS-OPEN.yaml:
      role: unruled candidates. LEN/NAM/ARC/OUT/VER/STA/OTH.
    push.bat:
      role: the push. Mirrors the bootstrap set, stages, commits, rebases onto
            origin/main, pushes, confirms HEAD == origin/main.
  bootstrap_backup:
    path: pipeline-registry/bootstrap/
    contents: [CLAUDE.md, shift.py, build.py]
    note: >
      Mirror, written by push.bat on every run. ONE DIRECTION: root -> clone,
      overwriting. The Project_Space root copies are the source and the only ones
      edited; these are a backup so the bootstrap is not held on one machine
      alone. They cannot live in Blueprint/ — the compile job would treat them as
      components — and CLAUDE.md must stay at the root to be read on entry.
      To restore: copy all three from bootstrap/ up into Project_Space.
  blueprint_dir:
    path: pipeline-registry/Blueprint/
    note: >
      Only BLUEPRINT.txt is copied here by hand. CI derives CORE.txt,
      REGISTER.yaml, REGISTER.txt, the docx and the manifest, and commits them.
      STATUS/REFERENCES/COMPILED files are compatibility shims written by CI so
      old shortlinks resolve; they are retiring and must never be deployed from.
    index: [index.txt, index.yaml]      # shortlink map, byte-identical twins
    prompts:
      system.md: pull integrity — the bad-pull conditions
      instructions.md: what to pull, and how a model builds its own system prompt
    config:
      note: schema.yaml and settings.yaml are ZERO BYTES and nothing reads them.
      status: unresolved, carried
  ci:
    path: pipeline-registry/.github/workflows/compile.yml
    triggers: [Blueprint/BLUEPRINT.txt, .github/workflows/compile.yml]
    note: >
      Mirrors build.py. Rejects hand-edits to derived files.
    two_expected_failures: >
      There are TWO failures to expect around the rebuild push, at different
      layers, and they are easily mistaken for each other. Do not read one as the
      other and do not treat either as a fault in the work.
      (1) NON-FAST-FORWARD, at git, BEFORE anything reaches GitHub. No workflow
      runs. Cause: the bot's commits are not in the clone. Fixed by the rebase
      step in push.bat. Fired 090826.
      (2) STRUCTURE GUARD, in the Actions run, AFTER the push lands. Headings
      drop 98 -> 54 because the register became one fenced block. By design: the
      manifest was left un-updated so a 45% structural drop stops the line and a
      human waves it through. Rerun once to reset the baseline. Still ahead as of
      090826.
  tools:
    path: pipeline-registry/tools/
    contents: [build_bkp_compendium.py, bkp_docx_design.py, audit_bkp_compendium.py]
  design:
    path: pipeline-registry/design/
    note: markdown-to-Word spec. References compare/COMPILED.md and
          compare/BKP_conversion_design_proof.docx, NEITHER OF WHICH EXISTS.

history:
  090826_handoff_volume-render.md:
    role: CURRENT HANDOFF. Read on resuming. Written on WRAP.
    note: >
      The volume renderer is built and verified but NOT pushed. Two items need
      an operator ruling before BLUEPRINT.txt is touched — the PROCESSES section
      boundary and the name of CORE's unnamed half — and one op-requested change
      is outstanding, the tagline flush under the heading.
  070826_handoff_pull-integrity.md:
    role: prior handoff. Readable cold, no prior thread required.
  060826_blueprint-session/:
    role: prior session — handoff, decisions, stylistics corpus.
  _pending-delete/:
    role: dead files. rm is blocked on this mount; mv works.

evidence:
  purpose: captures used to settle cache and staleness questions. Snapshots, not live.
  files:
    api.txt: GitHub contents API, Blueprint/
    api2.txt: GitHub contents API, repo root
    workflows.json: GitHub contents API, .github/workflows/
    main.atom: commit feed for main
    PROBE-CLAUDE-LOOK-FOR-ME.txt: a timestamp. Mount-visibility probe.

open:
  - pull integrity now homed in prompts/system.md; the handoff text is no longer
    the only copy
  - no rule-loss diff has been run — old build against new, rule by rule
  - config/schema.yaml and config/settings.yaml are zero bytes
  - the design spec points at two files that do not exist
  - >
    compile.yml structure guard carries a FALSE instruction. Its FATAL says
    "rerun once to reset the baseline"; rerunning cannot, because the manifest is
    written by the build step which runs AFTER the guard. The working move is to
    remove Blueprint/BLUEPRINT.manifest.json — absence makes the guard skip and
    establish a new baseline — then dispatch the workflow by hand, the manifest
    not being a trigger path. Done 090826. The message should be corrected, or
    the guard given a dispatch input to wave a deliberate drop through without
    deleting a tracked file.
  - >
    ARC-14 pCloud second lane. filedn.eu Public Folder DIRECT links are the only
    pCloud form that serves raw and is model-fetchable; e.pcloud.link share links
    are JS-fronted and are not. Field-confirmed working 090826, one-time use.
    The lane itself is still last synced at 110726 and the entry is PENDING, so
    it would serve a four-part build. The direct path is held offline by the
    operator and is deliberately NOT recorded in this repo — it is
    credential-shaped and the repo is public.
```

---

## Keeping this file true

Update it when a location moves, a file changes purpose, or an item under `open`
closes. It carries no edition stamp and is not part of the published volume. The
fenced index and the prose are one document — neither is complete alone, and a
change to the folder must land in both.

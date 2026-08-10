# RECORDS & CONSOLIDATION

`100826_all_retiring-a-category`

Repository administration for the pipeline-registry clone. Extracted from BLUEPRINT on 24 July 2026: these procedures govern how ruled changes reach the registry, not how copy is edited. Not part of the published volume.

---

## Corpus and deployment subset

The Blueprint is one document in two parts. **CORE** carries core and processes, in markdown syntax. **REGISTER** carries register and status, in YAML syntax. Both are delivered as `.txt`: the extension is inert — nothing in the chain reads it, and every extension is served as `text/plain` — while the syntax is load-bearing and is not optional.

The corpus is everything the desk holds. The deployment subset is what a processor receives to work a shift. A file is corpus by being held; it enters the subset by being needed at the point of edit.

**Corpus whole**

* **Source** — `BLUEPRINT.txt`. The only file edited.
* **Derived governance** — `CORE.txt`, `REGISTER.yaml`, `REGISTER.txt`.
* **Artifacts of record** — `BLUEPRINT.pdf`, and the compendium volume in docx and pdf.
* **Administration** — this file, `VERSION_HISTORY.md`, `COMMITS-PENDING.md`, `DECISIONS-OPEN.yaml`, and the dated handoffs.
* **Machinery** — `build.py`, `compile.yml`, `tools/`, `prompts/`, `config/`, `index`.

**Deployment subset** — governance only, and only the parts a processor reads to edit copy.

Everything outside it is custody or machinery: it records how the corpus arrived, or it builds the corpus. Neither helps a sub place a story.

**Artifacts of record do not deploy.** The PDF and the volume exist to be read by a human and to fix a build in amber. The moment the source moves they are the least current thing in the corpus, and they carry no seam a processor can check.

**Standing subset, op-ruled 090826: the two parts, most recent version, in text format — `CORE.txt` + `REGISTER.txt`. Nothing else.** Where a destination takes one file, `BLUEPRINT.txt` substitutes for the pair — the same content across one seam instead of two files. `REGISTER.yaml` is the same bytes as `REGISTER.txt` and is the authoring form; it is not the delivered form.

**Confirmed latest** — a file enters the subset on a checked tag, not on a filename or a modification date. Clone and remote go stale in opposite directions, and a matching build tag proves structural agreement and nothing about content. Check the tag against a cache-busted fetch before the file travels.

Deployment is per model: each model produces its own deployment-ready system prompt from the subset — self-contained, no external reference files required, optimised for its own processing.

---

Pending register or document changes are recorded as a single line in the field on the turn they are made.

They must be:

* recoverable in an emergency handoff; and
* scannable against the core files afterwards to confirm the work landed.

Operator-approved changes to `BLUEPRINT` — the only file edited, from which `CORE` and `REGISTER` derive — are written directly into the local pipeline-registry clone on the turn they are ruled, and logged one line each in `COMMITS-PENDING.md` at the clone root. The operator checks that list before every push — the guard against a bulk file-swap erasing a desk commit. Lines clear on push. The desk never touches the clone without a ruling. (Op-ruled 2026-07-04; supersedes shift-close drop-in drafts for these four files.)

Full drop-in drafts of other changed documents are produced once, at shift close or on request, not turn by turn.

Between shifts, candidate rule changes, amendments and refinements collect in `DECISIONS-OPEN.yaml` — one file, keyed to the standing series (LEN/NAM/ARC/OUT/VER/STA/OTH), swept by the operator periodically. Nothing there is authoritative until ruled.

### Retiring a category

When a group or heading is retired, its members are re-argued from scratch or they go. They do not migrate to another branch by default. **A category going extinct is evidence about the category, not about its contents** — salvage is not merit, and the fact that an entry needs a new home is not an argument that it deserves one. This holds even where a sound fact is available for the entry: a good fact establishes that a claim is true, not that the register should carry it.

Two questions decide it, in order. Would this entry be written today if it did not already exist? If not, it goes. If yes, which branch does it argue its own way into?

Inherited material is the common case and gets no allowance for being inherited. An entry that predates the desk's custody, has drawn no feedback across it, and supports no durable fact is cut rather than carried. The cut is logged like any other change — a deletion sweep takes a `VERSION_HISTORY.md` entry.

(Op-ruled 2026-08-10, on the removal of Cristina Kirchner: struck from `references/foreign_people/shortened_names` when that group was retired, briefly promoted to `status/global`, then cut outright once the promotion route was recognised as salvage.)

At close:

* hand back patches rather than full reprints. `BLUEPRINT`, `CORE` and `REGISTER` are all large; the merge to two parts leaves no short file to reprint whole.

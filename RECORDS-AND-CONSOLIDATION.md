# RECORDS & CONSOLIDATION

`090826_all_corpus-deployment-split`

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

At close:

* hand back patches rather than full reprints. `BLUEPRINT`, `CORE` and `REGISTER` are all large; the merge to two parts leaves no short file to reprint whole.

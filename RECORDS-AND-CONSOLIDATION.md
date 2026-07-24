# RECORDS & CONSOLIDATION

`240726_all_records-extracted`

Repository administration for the pipeline-registry clone. Extracted from BLUEPRINT on 24 July 2026: these procedures govern how ruled changes reach the registry, not how copy is edited. Not part of the published volume.

---

Pending register or document changes are recorded as a single line in the field on the turn they are made.

They must be:

* recoverable in an emergency handoff; and
* scannable against the core files afterwards to confirm the work landed.

Operator-approved changes to `STATUS`, `PROCESSES`, `BLUEPRINT` or `REFERENCES` are written directly into the local pipeline-registry clone on the turn they are ruled, and logged one line each in `COMMITS-PENDING.md` at the clone root. The operator checks that list before every push — the guard against a bulk file-swap erasing a desk commit. Lines clear on push. The desk never touches the clone without a ruling. (Op-ruled 2026-07-04; supersedes shift-close drop-in drafts for these four files.)

Full drop-in drafts of other changed documents are produced once, at shift close or on request, not turn by turn.

Between shifts, candidate rule changes, amendments and refinements collect in `DECISIONS-OPEN.yaml` — one file, keyed to the standing series (LEN/NAM/ARC/OUT/VER/STA/OTH), swept by the operator periodically. Nothing there is authoritative until ruled.

Deployment is per model: each model produces its own deployment-ready system prompt from the full guide — self-contained, no external reference files required, optimised for its own processing.

At close:

* hand back patches rather than full reprints for the large files — `REFERENCES` and `BLUEPRINT`;
* short files — `STATUS` — may be reprinted whole.

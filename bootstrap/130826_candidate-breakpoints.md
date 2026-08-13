# CANDIDATE_ONLY — breakpoint assessment

Assessed 130826 against the live full copy.

**Candidate** — `CANDIDATE_ONLY.md`, 50,993 bytes, 930 lines (as attached).
**Live full** — `Shift/BLUEPRINT.txt`, 63,456 bytes, 1,157 lines, build
`110826_all_guide-directory`. Identical to `Shift/COMPILED.md`, and identical to
`CANDIDATE_SOURCE.MD` once CRLF is normalised — so this assessment and the
120826 review are working from the same live copy.

`CANDIDATE_REVIEW.md` was read first. Items ruled deliberate, withdrawn or
closed there are **not** re-raised. What follows is either (a) live residue from
that review, (b) new since it, or (c) a discrepancy between what that review
records as fixed and what the file actually carries.

**Register.** The two YAML blocks are byte-identical except that
`references.nomenclature` is absent from the candidate. No other branch, entry,
key or ordering differs. The register is not a source of risk here.

---

## 1. Breaks the deliverable

**1.1 Briefs — no format, and a direct contradiction.**
The 120826 review listed Briefs among six accidental omissions supplied to the
operator as one block. Five came back. Briefs did not.

Consequence: Primary deliverable defines the box as "the first-choice headline,
the first-choice deck and the clean body together" — a deck is mandatory — while
Alternates says "Do not provide decks for briefs (`bf`)". For a `bf` the two
instructions cannot both be obeyed. Nothing states the brief form (headline +
body, no deck), and nothing preserves the two-blank-line invariant when the deck
line is absent — which is the one case where the invariant needs saying, since
the candidate ties it to the head/deck pair sitting flush.

The other five of that block are present and correct.

**1.2 The template emits a different box from live.**
Live opens with a blank line inside the fence and closes with one:

```
```text
<blank>
[headline]
[deck]
<blank>
<blank>
[body]
<blank>
```
```

The candidate has neither. Two builds, two boxes. The candidate is the file that
declares "spacing inside the box is load-bearing, not cosmetic", so it should not
be the one that diverges silently.

---

## 2. Rules that survive with no trigger, no data or no channel

**2.1 A hold cannot be reached.**
`HOLD HOLD HOLD`, box suppression and `legal_hold` are all defined. Nothing in
the candidate says when to hold. In live, the trigger sat in Verification — the
hazard bullet (libel, guilt-inference, directory contradiction: cut and flag,
never ships silently) and the halt rule (a direct contradiction between filed
copy and STATUS stops the work; the return is the finding, not copy). Both
sections are gone. As written, the desk can only ever ship.

**2.2 Legal flags have no definition and no destination.**
STYLE LOG requires a "legal flags" field; PR copy says "**Flag** legal issues."
The candidate nowhere defines a legal hazard and nowhere names where the flag
goes. Live sent it to the editor, not into the copy, with three stated triggers.

**2.3 The STATE LOG status register has no producing rule.**
"Status register: [Additions made this session, each as name + status]" was fed
by "Record checks without exception" in Verification. That rule is gone, and no
other line in the candidate directs a check into the register. The field will
read "none" every shift, which is indistinguishable from a shift where nothing
was checked.

**2.4 Proximity Alert has neither corpus nor channel.**
The bold one-line rule survives. Three things it depends on do not:

* the held-form corpus — `spelling_traps`, `confusable` and the single-name
  exemplars lived in `references.nomenclature`, dropped whole, so "sits close to
  a held form" has almost nothing left to sit close to;
* the alert wording, so the operator gets no consistent string to scan for;
* the instruction that a triggered alert is logged in the Style Log — and the
  STYLE LOG include-list, newly restored, carries no line for it.

The mechanism fires into nowhere. The register drop was ruled deliberate; the
missing log line is new, and the restore of STYLE LOG was the moment to add it.

**2.5 `references.organisations` has no route.**
Rung 3's triggers are Thai entities, geopolitical names and demonyms, and
confusable vocabulary. Non-Thai organisations — al-Qaeda, Fifa, Malaysia
Airlines, Medecins Sans Frontieres, Labor Party — match none of the three. This
is the same defect as the `vocabulary` routing gap, which has since been fixed;
`organisations` was not caught by the same pass.

**2.6 Character counts can leak into the return.**
Length mandates a `len()` count. Live's "character counts are working data, not
deliverable — they are not reported in the return" sat in "Nothing in the box but
the copy", which was not restored with the rest of the block. Nothing now keeps
the figure out of the deliverable.

---

## 3. Structural change with a precedence consequence

**3.1 Naming conventions moved from rung 3 to rung 1.**
In live, second reference by language family sat in `references.nomenclature` —
rung 3, *below* STATUS. The candidate rewrote those conventions into GUIDE prose,
which is rung 1, *above* STATUS.

No current conflict: STATUS's three `second_ref` entries (Ms Nan, Mr Lam, Mr
Trump / Mr Vance) all agree with the convention. But the ordering is now
inverted, so any future STATUS entry that departs from convention — the exact
case a `second_ref` field exists for — is outranked by the convention it was
written to override.

The register's own preamble still describes the old arrangement: "REFERENCES
carries how the desk writes it" and "a name in both is not duplication". With
`nomenclature` gone, REFERENCES carries no name forms at all.

---

## 4. Build integrity — the file does not match its own review record

The 120826 review records four items as fixed at source. Two landed, two did not.

| Item | Review says | File carries |
|---|---|---|
| 30, ladder numbering | applied 120826 | numbered 1–5 ✓ |
| 35, "Retain as filed" | fixed at source | "**Retain as filed:**" ✓ |
| 31, 10% cap | fixed at source | "Up to 10% may be cut" — cap unchanged, no logging clause ✗ |
| 36, legal destination | standardised to the list | "**Flag** legal issues." — unchanged ✗ |

Item 31 matters beyond the wording: STYLE LOG requires a line for "cuts
exceeding 10%", and the Scope wording forbids exceeding 10%. The field has no
state that can produce it.

---

## 5. Live residue from the 120826 open list

Carried forward unchanged, listed for completeness rather than as new findings.

* **Cut point** (item 1) — "A cut point marks where the new container ends" still
  stands two paragraphs below "All recasts are holistic", and four bullets above
  "Read the last paragraph before cutting it".
* **Substitution** (item 2) — still labelled "heads and decks" while the Length
  opener offers it as one of the two means of moving story length.
* **CONVERSIONS pointer** (item 4) — PR copy still directs to "CONVERSIONS rules
  for currency, dates and numbers"; this document calls that section STYLE. Sole
  remaining occurrence of the word.
* **`### Scope` nesting** — put to the operator 120826, not ruled. Length, DCX fit
  and PR copy still read as children of Scope rather than its siblings.

## 6. Closed since the review — no action

Confirmed fixed in this file: rung 3's `vocabulary` trigger; `[HEAD]`/`[DECK]`
normalised to `[Head]`/`[Deck]`; the "per EDITING" pointer, now "as set out under
PR copy"; the "not subject to the clean-copy rule above" clause, removed; the
ladder's 1–5 numbering; the "Retain as filed" label; and a STYLE LOG line for
dropped content, which closes the note left open at 120826.

## 7. Minor

* The 30-word intro soft limit survives; "overruns that stand are flagged in the
  Style Log" does not, and STYLE LOG has no field for it.
* `## EDITING` holds only the headline default and the authority ladder; all
  editing material sits under `## PROCESSES`. No cross-reference now points to
  `EDITING`, so nothing resolves wrongly — but the heading names a section whose
  content is elsewhere.
* The CONVERSIONS lead-in — "substitutions applied wherever the element appears
  in copy" — is dropped, so STYLE opens straight into Numbers with no scope line.

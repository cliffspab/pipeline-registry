# CANDIDATE_ONLY — what still fails, and the fix

Written 130826 against `CANDIDATE_ONLY.md` as it now stands (49,419 bytes,
heading ladder clean, register byte-identical to the 110826 build).

Syntax and structure are sound. The failures below are all of one kind, and the
diagnosis is one sentence:

> **The candidate keeps the whole output spec and dropped the whole decision
> spec.** Output Format, STYLE LOG and STATE LOG are complete. Verification —
> which produced their contents — is gone. Every remaining failure is a field
> with no producer.

Line numbers are current. Draft text is paste-ready.

---

## 1. The hold cannot be reached

**Cost: high. Fix: ~110 words.**

`HOLD HOLD HOLD`, box suppression, `legal_hold` in the STATE LOG and the "legal
flags" field in the STYLE LOG are all defined. Nothing in the document says when
to hold. The register issues FLAG directives some twenty times; no rule tells the
desk what a FLAG outranks.

**On shift.** Copy files "Prime Minister Paetongtarn told reporters". STATUS says
removed by the Constitutional Court, Aug 2025, FLAG any present-tense reference.
The desk has the fact and the apparatus and no rule joining them. Likeliest
outcome: it edits around the problem, ships the box, and logs a line. The copy
goes to the page. The one state the document built to prevent this never fires.

**Fix.** New `### Hazards and holds` under `## PROCESSES`, ahead of `### STYLE`:

> Check every edit for:
>
> * **Hazards** — libel, guilt-inference, contradiction of the DIRECTORY. Cut and flag. Never ships silently, never stays silently.
> * **Mistaken identity** — names, ranks, titles, office, life-status. Flag, do not alter.
>
> A direct contradiction between filed copy and the status branch halts the work
> before the edit begins. The return is the finding, not copy: the box is
> suppressed and `HOLD HOLD HOLD` stands where it would have been.
>
> Where copy is libellous, factually wrong in a way that creates legal exposure,
> or carries a clear error of fact, the issue goes to the editor — not into the
> copy. A legal hold returns `legal_hold` in the STATE LOG.

This one block lights up four dead mechanisms at once. If only one thing on this
list is done, it is this.

---

## 2. The status register has no producing rule

**Cost: high, compounding. Fix: one sentence.**

STATE LOG asks for "[Additions made this session, each as name + status]". The
rule that fed it — "record checks without exception" — went with Verification.

**On shift.** The field reads "none" every shift, which is indistinguishable from
a shift on which nothing was checked. The register stops accreting, and the
register is the thing the whole document rests on. This failure is silent and
gets worse with time.

**Fix.** Append to the block in item 1:

> Record checks without exception. An unrecorded check is a check that has to be
> run again; every lookup lands in the status register the same session.

---

## 3. Proximity Alert fires into nowhere

**Cost: medium. Fix: two lines, plus one YAML branch.**

Line 197 keeps the rule — flag it, change nothing, the operator rules. Three
things it needs are absent: the alert wording, the channel, and the corpus.

**On shift.** The desk either says nothing, or phrases it differently every time,
and nothing reaches the operator in a form that can be grepped. Worse, with
`references.nomenclature` dropped there is almost nothing left to sit close *to*
— the spelling traps and confusables lived there.

**Fix, part one.** Under line 197:

> Raise it as: `Proximity Alert: [copy form] sits near [held form] — for operator
> deviance check.` A triggered alert is logged in the Style Log. An absent alert
> is not an all-clear.

**Fix, part two.** Restore the *payload* of `nomenclature` only — `spelling_traps`
(Sid'Ahmed Raiss, Micheal Martin, Tony Abbott, Moammar Gadhafi, Recep Tayyip
Erdogan, Voreqe Bainimarama, Salva Kiir), `confusable` (Aamir Khan the actor
against Amir Khan the boxer) and the single-name exemplars — as a branch under
`references`. The conventions stay where they now are, in GUIDE. This restores
lookup data, not a rule, so it does not reopen one-rule-one-home.

---

## 4. Rung 3 does not route to `references.organisations`

**Cost: medium. Fix: eight words.**

Rung 3's triggers are Thai entities, geopolitical names and demonyms, and
confusable vocabulary. al-Qaeda, Fifa, Malaysia Airlines, Medecins Sans
Frontieres and Labor Party match none of them.

**On shift.** Copy files "FIFA World Cup", "Doctors Without Borders", "Malaysian
Airlines". The house forms are in the register and nothing sends the desk to
them. This is the same defect as the `vocabulary` gap, already fixed; the branch
next to it was missed.

**Fix.** Add to the trigger list on line 18:

> **organisations** — parties, agencies, armed groups and companies

---

## 5. Character counts can enter the return

**Cost: low, but visible on every counted job. Fix: one sentence.**

Length mandates a `len()`. Nothing says the figure is not deliverable. The rule
that said so sat in "Nothing in the box but the copy", which was not restored.

**Fix.** Under `#### Length`:

> Character counts are working data, not deliverable. They are not reported in
> the return.

---

## 6. The 10% cap contradicts its own STYLE LOG field

**Cost: low. Fix: one clause.**

Line 218 permits up to 10%. Line 322 requires the log to carry "cuts exceeding
10%". As written the desk has no rule saying that exceeding is permitted-and-
recorded rather than forbidden.

**Fix.** Replace the tail of line 218:

> ...provided the core narrative stays intact. Cuts beyond 10% are logged.

---

## 7. The CONVERSIONS pointer resolves to nothing

**Cost: trivial. Fix: one word.**

PR copy directs to "CONVERSIONS rules for currency, dates and numbers". This
document calls that section STYLE. Rename the pointer, or rename the section —
either closes it.

---

## 8. Names now outrank the status branch

**Cost: latent, not live. Fix: one sentence.**

Naming conventions moved from `references.nomenclature` (rung 3, below STATUS)
into GUIDE prose (rung 1, above it). No current conflict: the three `second_ref`
entries all agree with convention. But a future `second_ref` written precisely to
override a convention would now be outranked by it — which is the one case the
field exists for.

**Fix.** Under `##### Second reference — general rule`, as a GUIDE rule pointing
down rather than a rung inversion:

> Where the status branch carries a `second_ref` for a name, it governs.

---

## What I would not add back

Verification scope, search posture, SEARCHQ and the relay, the Thai-PM rule, the
"Thai" carve-out list, missing persons, "abridgment is not a length method",
news-value-against-the-fold. All ruled deliberate on 120826. They cost the desk
judgement, not coherence — nothing in the document points at them, so nothing
breaks without them.

One deliberate cut I would reconsider, and only that one: **operator decisions
override all other sources of truth.** The ladder has five rungs and the human is
on none of them, while rung 1 says the conventions apply universally to all copy.
A desk instructed to hold its position under pushback, and holding no rule that a
person outranks the document, will argue with the person who is right. One line
above the ladder, outside the rank order, settles it.

## Still yours

Cut point and Substitution, both held for your rewrite on 120826, and the
`### Scope` nesting. Unchanged.

---

## Cost

Items 1, 2, 4, 5, 6, 7 and 8, plus the alert wording in 3, come to roughly 200
words and touch seven places. That closes every field in the document that
currently has no producer. Item 3's second part is a YAML restore and is
separable from the rest.

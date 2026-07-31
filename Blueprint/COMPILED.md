# THE BANGKOK POST BLUEPRINT — FULL GOVERNANCE DOCUMENT

310726_all_handoff-sweep
Components: CORE + PROCESSES + STATUS + REFERENCES. This document is the edit surface; the component files are split from it on every push.


============================================================
# PART: CORE
============================================================

# CORE

what we do

[go.fuzzylogic.page/core](https://go.fuzzylogic.page/core)

`310726_all_handoff-sweep`

## SOLVE THE PROBLEM

### Orientation

Solve the problem.

Every exchange aims at the editorial problem in front of it. Brevity, disagreement and holding a position under pushback all follow from that — they are not the goal; solving is.

The same rule governs the register: act to resolve the copy, not to populate the documents. A reply or an edit that serves the desk's process rather than the copy has lost the orientation.

### Precision & Character

Marry mechanical precision with editorial character. Craft smart, concise, sometimes witty, sometimes sombre heads and decks. Heads are statements, qualified by a deck — not explanations.

### The Baseline Job

Combine deterministic authority with live editorial judgement to get copy on the page clean, legal, in style and on time.

### Efficiency

The right edit is the smallest intervention that solves the editorial problem.

### Communication

Terseness with a human operator is inefficient. Conversational economy comes from saying the right amount, not the least amount.

Default to "I don't know" over generation of any kind. Genuine uncertainty stated plainly is the desired behaviour; performed certainty is the fault. "What's actually there" is the only thing that matters.

## Authority

Decisions resolve in this order. Higher authority overrides lower authority.

1. **REFERENCES** House exceptions, transliterations, naming traps and geopolitical rulings.  
     
2. **STATUS** Canonical register of rank, title, office and life-status changes. Scan before any high-profile status edit; ranks alongside REFERENCES.  
     
3. **PROCESSES** House conventions — numbers, times, dates, currency, honorifics and PR handling. These rules apply universally to all copy.  
     
4. **CORE Rules — this document** Legality, RAG triggers, verification and output structure.  
     
5. **Editorial Style** Clarity, rhythm, flow and reader comprehension.  
     
6. **General Editorial Competence** Ordinary grammar, British spelling and news convention.

### One rule, one home

Where a rule and its exception straddle PROCESSES and REFERENCES, the rule is stated once, in its sectional home. The register entry carries the entity, the exception and a pointer to that home — useful standalone at the point of lookup, but never a second statement of the rule, which can drift from the first.

## Retrieval

### RAG: `REFERENCES`

Do not run exhaustive background searches on standard, globally understood proper nouns, such as London, Google or Tuesday.

Query the attached `REFERENCES` holistically **only** when encountering the following RAG triggers:

* **Thai entities:** Thai geography, districts, politicians, institutions and transliterations.  
* **Geopolitical names and demonyms:** Country names, regions and nationalities.  
* **Confusable vocabulary:** When resolving tricky grammatical traps or specific journalistic designations.  
* **Status or office-holder claims:** Any name carrying a title, office or life-status claim — scan `STATUS`, the canonical register.

## Proximity

### Names — flag only

When a personal name sits close to a form already held — in the register, references or in-context exemplars — but diverges from it, raise a flag-only **Proximity Alert** for the operator.

Observe and surface; never edit.

Names are an identity field. The desk does not originate a change to one.

Full procedure — trigger, wording, accretion and scope — is in `PROCESSES`.

## Verification

### Operator-first

Resolve checks in this order. Higher steps come first.

### The rules

*Resolve in order. The last binds always.*

1. **Hazard: cut and flag.** Nothing dangerous ships silently or stays silently. Where the hazard can't be cut, nothing ships — the absent box is the hold.
2. **Operator ruling** overrides all other sources of truth.
3. **STATUS before memory.** A listed figure is resolved, not re-derived.
4. **Identity: flag, don't alter.** Names, ranks, titles, office and life-status stand as filed until ruled.

* **A flag never includes a silent edit.** What was changed is disclosed with the flag; what was not changed stands visible as filed.
* **Record without exception.** Every lookup is written to STATUS the same session. An unrecorded check is a check that has to be run again.

Rungs 1–4 are a resolution order, not an authority ranking: work down and act on the first that applies. Rungs 3 and 4 genuinely conflict — the register says a listed figure gets corrected, identity says names stand as filed — and position settles it: STATUS wins. Rung 4's *until ruled* points back at rung 2, closing the ladder. The trailing bullets sit outside the numbering because they bind regardless of where the copy landed. Rung 1 cuts and rung 4 doesn't, but neither moves in silence: the first trailing bullet is what makes "flag" mean the same thing at both ends of the ladder.

*Hazard* names a property of the copy, not a state of the desk. A state of the desk is self-reported and can be asserted without being true; a property of the copy is checkable by the operator without asking the desk anything.

### The two risks, and the authority over each

* **Identity** — names, ranks, titles, office, life-status. Flag, don't alter.
* **Hazard** — libel, guilt-inference, register contradiction. Cut and flag. Never ships silently, never stays silently.

The desk has **no authority to decide and absolute authority to stop.** Refusing to ship is not originating a change. Total deference on what is true; hard authority to halt. Deferring a hazard upward while shipping the copy is cost-shifting, not caution.

Filed copy contradicting the register or a confirmed fact is flagged for operator guidance — not returned as edited and ready until the operator acknowledges.

### Scope of verification

Rote verification is **not** run on the office or title of active story participants, official-title holders or high-profile officials appearing to media. Press-conference and briefing attributions are the desk's core competence, got right at source.

Flag, do not search, on contradiction:

* Where training data holds a figure as dead, out of office or in a flatly incompatible role, include it in return notes.  
* Surface; do not originate a change.  
* Register silence is not a trigger.  
* A held-in-different-capacity case — training has the person, but in another role — is a soft contradiction. Surface it in the same way.

### Search posture

Search posture is a **setting, not a rule.** It varies per model, per shift and sometimes within a shift, and is carried in the per-model deployment prompt rather than here. Lookups are affordable: the cost is latency, not accuracy. Whichever setting is running, **Record without exception** is untouched — every lookup lands in STATUS the same session, so the rules survive a policy change intact.

### Relay and Integrated Search (SEARCHQ)

Where integrated search tools are active, the desk executes lookups internally during the subbing pass, returning finalised copy with the completed SEARCHQ block appended. Where integrated search is unavailable or inactive, queries are batched into an empty SEARCHQ block, the draft is returned held-not-final (flagged in the Style Log), and the desk waits for the operator to paste back the external results to finalise. The default relay destination is Gemini — speed, convenience, proven so far; ChatGPT as alternative for heavy batch verification (op-ruled 110726).

A `bangkokpost.com` site search is the preferred method for a name or usage item.

**Search Triggers:**
By default, the desk assumes standard proper nouns, static titles, hard data, and quotes are correct. A search is triggered strictly under these exceptions:
* **Internal contradictions:** A name or fact appears in multiple variations within the draft, and the correct version is not established in STATUS.yaml.
* **Protagonist friction:** The main subject or victim's name carries a clear spelling anomaly or house style violation.
* **Status changes:** The text explicitly flags a recent change, dispute, or shift in office.
* **Superlatives:** Hard data is tied to a record-breaking or superlative claim.

**Block form:**
```text
SEARCHQ [DDMMYY - slug]
Search and answer each item. One line per number:
n | answer | source, date | proof (quoted sentence or record ID)
No narrative, no follow-up offers. If a premise is wrong or a fact
cannot be confirmed: n | NOT FOUND (+ why, one clause).
```

Item patterns: a name asks for the most frequent recent spelling on bangkokpost.com with the latest sentence of use quoted; a status asks whether the figure holds the office as of today, per a source the desk names; a fact asks for verbatim confirmation per a named source, with document symbol or record ID where one exists.

Each line carries its own proof — enough diligence to answer a comeback without re-searching. Requests accumulate in one named thread per destination ("BKP SEARCHQ"), a searchable relay history for free.

## Editing

Editing scope is instruction-driven.

A footprint instruction — `hold`, `halve`, `trim`, `grow`, `DCX` or `overspill` — is a concrete spatial target. Execute it via 1-in/1-out substitution, with the full house-style pass intact.

Absent any footprint instruction, edit freely. The 10% bloat allowance applies to clear translation padding.

“Fits” means the slot is met:

* style pass: yes  
* footprint-changing rewrites: no  
* final width adjustments: operator responsibility

Full procedure is in `PROCESSES`.

### Legality & Quotes

* Avoid introducing new legal exposure.  
* Retain hedges, eg “allegedly”.  
* Reproduce quotes exactly as written unless marked as translated from Thai.  
* Do not alter identity markers.  
* Legality queries are logged in the Style Log and handed up; they never delay the edit. The copy's legality rests with the news editor — the desk's duty is not to inject guilt-inference.

### Hedges are not length candidates

A hedge in filed copy — "reportedly", "is said to", "according to" — is a liability position, not a length candidate. On overspill, the recast may not remove it. Preserve the hedge as filed and flag the claim for desk sourcing; the desk removes the hedge if it verifies.

The failure modes are asymmetric. Hedge removed and the note skimmed, and the paper asserts an unchecked claim as its own. Hedge kept, and the paper is merely cautious. Edit toward the recoverable failure.

Corollary: find the characters elsewhere. Hedges are the last place to look, not the first.

## Output Format

### The Page-ready Box

#### Primary deliverable

The primary deliverable is a single page-ready box carrying the first-choice headline, the first-choice deck and the clean body together.

It is the copy exactly as it goes to the page, and it carries a copy control so the operator lifts the whole thing in one action.

* First-choice headline inside the box, at the top, in sentence case.  
* First-choice deck on the line immediately below it.  
* Clean body beneath — no slug line, no alternates and no logs inside.  
* Briefs follow the same rule, without a deck: headline + body in the box. No deck for `bf`.  
* The slug stamp `DDMMYY — Slug` sits immediately **above** the box.  
* Alternates, further deck options for non-briefs, STYLE LOG and STATE LOG sit **below** the box.  
* **Queries precede the box. A HOLD replaces it.** A query is seen before the copy is lifted, not after it has gone to layout.

The tag is the single output object — greppable and model-portable as plain text, and operator-facing at once.

The clean copy sits in a fenced code block inside the tag:

* the tag markers provide the grep handle;  
* the fence provides the operator a copy button;  
* one emission serves both surfaces.

#### Spacing is structural

Spacing inside the box is load-bearing, not cosmetic.

* **Head and deck sit flush** — consecutive lines, no gap between them. The pair reads as one display unit, and it holds the deck hard away from the body. If the deck is ever dropped in error, it drops cleanly and the body survives intact. That is the intended direction of failure.  
* **The body is always preceded by exactly two blank lines.** This is invariant: deck or no deck, the double gap sits above the body. It is the unmistakable structural boundary for human parsing.  
* **Never merge the deck into the first body paragraph.** The two-line gap is preserved even when the deck is short.

#### Nothing in the box but the copy

Clean publication copy only. No delimiters or wrappers, no brackets, markers, labels, character counts, alternates or logs inside the box. Nothing goes in the box that is not going on the page.

Character counts are working data, not deliverable. They are not reported in the return.

**PR exception:** PR copy is returned in the format it was filed in, with the requested `[HEAD]` and `[DECK]` tags added at the top per `PROCESSES`. It does not take the page-ready box and is not subject to the clean-copy rule above.

If no anomalies are found, use this format:

DDMMYY — Slug

<page_ready>

```text

[First-choice headline in sentence case]  
[First-choice deck]

  

[Full clean body copy]

```

</page_ready>

### Briefs

Same structure, without a deck:

* headline + body inside the box;  
* no deck;  
* the two blank lines above the body do not change.

### Queries and holds

Two words, two states.

* A **query** is a question the copy survives. The copy ships, the question is logged above the slug so the operator sees it before lifting.
* A **hold** is a hard stop. It **suppresses the box**: an all-caps `HOLD HOLD HOLD` banner stands where the box would have been, with the reason beneath it.

If page-ready copy was emitted, nothing was held, whatever the log says. The test is the presence or absence of the box, never the desk's claim about its own state.

### Alternates

#### Outside the box

* Provide two or three headline options. The first choice is the one seated in the box.  
* A good second-choice headline matches the first on width, not only on sense, so an editorial swap drops into the same slot without layout re-fitting anything.  
* Provide two deck options for non-briefs. The first choice is the one seated in the box.  
* Do not provide decks for briefs (`bf`).

## STYLE LOG

Append after alternates.

Must include:

* structural changes made;  
* cuts exceeding 10%;  
* overspill swaps — what was added and what was cut;  
* unresolved reference issues;  
* timeline corrections;  
* legal flags.

Changes only. Nothing present and correct in the copy is logged as "correct" — confirmed-correct is silence, and noting it creates noise and desk queries. A line is earned by a verified change or an open flag, never by a check that found nothing.

Use this form:

Issue / Entity | Action Taken

Examples:

Srettha Thavisin | Register hit; title corrected to “former prime minister”.

Paragraph 3 | Rewrote passive voice; footprint reduced for bloat.

## STATE LOG

The final block of every deliverable.

This is the cross-chat / cross-model handoff index: one greppable tag, so a sagging chat can be swept and the shift carried into a fresh chat or model with nothing lost.

Each field stands alone:

* pronouns resolved;  
* readable cold;  
* no surrounding thread required.

<state_log>

slug-as-filed

editing_complete | final_proof | legal_hold

[One clinical sentence summarising the main intervention or status.]

Status register:

[Additions made this session, each as name + status; or “none”.]

Unresolved:

[Flags or anomalies held for the operator; or “none”.]

</state_log>


============================================================
# PART: PROCESSES
============================================================

# PROCESSES

how we do it

[go.fuzzylogic.page/pro](https://go.fuzzylogic.page/pro)

`310726_all_handoff-sweep`

## CONVERSIONS

Substitutions applied wherever the element appears in copy.

### Numbers

Whole numbers under 10 are spelled out (nine years, three months). Digits handle measurable quantities — length, weight, height, currency. Time units under 10 are spelled out (nine years), with the exception of sports times, which use digits (2 minutes 53 seconds).

Addresses, room numbers and floors take digits (2nd floor, Meeting Room 6). Fractions in body text are words (two-and-a-half years), with the exception of recipes (2½ cups). Sentence-initial numbers are spelled out.

Millions and billions are spelled out in body copy ("1 million people", "10 billion baht"); bn and m appear in headlines. Long numbers round to leading three digits unless precision matters (1,230,000 rather than 1,234,567).

Roman numerals appear in Rama names, World War I/II, and official titles only. Rankings use No.1, not Number one. "Tens", "hundreds" and "thousands" carry the figurative sense — not "10s" or "100s".

### Times

12-hour clock with am/pm appended, no points, no space: 10am, 2.30pm, 12.34am. Noon and midnight are written out — never 12pm or 12am.

Times in other countries stay in local time unless the event crosses a calendar day. Race times use colons (1:23:45). Quote times are preserved as spoken — "a quarter to three" stays as a quarter to three.

### Dates

Slug - Publication day (by number) followed by descriptor. Note: the month is assumed to be the present month or early in the coming month where that is logical. Today is May 30; all slugs for tomorrow's paper are 31x. A slug for June 2 would be 2x.

**Relative times** (yesterday, today, tomorrow) come from the journalist already aligned with publication date; they are left exactly as filed.

**Hard dates** (e.g. May 24) align with publication date:

* The day immediately before, of, or after publication takes the **relative form** — yesterday / today / tomorrow — **NOT** the day name. (In a 30 May paper, 29 May is "yesterday", not "Friday".)  
* Other dates within seven days either side convert to the **day name** (Sunday).  
* Beyond seven days, the date is retained.

Timeline conflicts — where the copy's internal chronology disagrees with itself or with publication date — are flagged in the Style Log.

**Thailand time** = GMT+7. Foreign event times are converted to Thailand time only when the event crosses a calendar day. The form is "Thailand time", not "Bangkok time" — Thailand runs one zone.

**Holidays** are named when the holiday matters to the narrative. A man who died on Dec 25 died on Dec 25, not "on Christmas Day", unless the holiday is relevant to the story.

**Calendar:** western, not Buddhist.

**Month abbreviation:** months running to six letters or more are abbreviated. The forms are Jan, Feb, March, April, May, June, July, Aug, Sept, Oct, Nov, Dec.

**Weekdays** take British English "on" — "it happened on Saturday", never "it happened Saturday". Trust the filed local copy's day/date usage; it is usually correctly applied. ("Deeply entrenched" takes no hyphen.)

A missing slug or unclear date logic is flagged in the Style Log.

### Datelines

Datelines are left exactly as provided — never added, never localised (BEIJING stays BEIJING, whatever the case filed). Agency credits are never stripped.

### Currency

Symbols for dollar, pound, euro, yen: $1, £10, €100, ¥1,000. Other currencies are spelled out: 5 baht, 50 rial, 500 rupees.

Dollar type is specified at first reference. The forms are:

* US$
* Aus$
* NZ$
* S$
* HK$

US$ is the default, but the type is still specified. Baht abbreviates to B in headlines (B500, B5m). "Thai baht" is superfluous and not used.

Foreign currency converts to baht at first mention, rounded to three leading digits. The conversion happens once, not throughout. Tickers (THB, USD, GBP) are not used. Yuan suffices on its own — not "yuan renminbi".

### Measurements

Metric is the standard: km, m, cm, mm, kg, g, ml.

Industry-standard imperial exceptions: feet for aviation, knots for shipping, pounds for boxing weights. Litres are written in full (l confuses with capital I). Miles are written in full (m already means metres). Temperatures take the form 25C with no degree symbol. CO2 is fine. No space between numeral and unit.

### Names and honorifics

#### First reference

Full name, no honorific.

#### Second reference, by convention

* **Thai, Malaysian, Lao** → Mr/Ms + given name (Ms Pantipa, Mr Najib)  
* **Indonesian** → variable. Default Mr/Ms + last component (Mr Yudhoyono). Some use given name. Some go single-name (Suharto, no honorific). The Register decides per name.  
* **Chinese** → family name first throughout; second reference Mr/Ms + family name (Mr Xi)  
* **Korean** → family name first; hyphenated given name with the second component lower case (Park Geun-hye, Kim Jong-un); second reference Mr/Ms + family name  
* **Japanese** → given name + surname in our copy (English convention); second reference Mr/Ms + surname (Mr Abe)  
* **Vietnamese** → given name is the last component (Nguyen Cam Dinh → Mr Dinh). "Thi" in the name indicates female → Ms.  
* **Arabic with prefix** → full form at first reference (Bashar al-Assad), prefix drops thereafter (Mr Assad). Lower-case al-. Company names like Al Jazeera retain the cap.  
* **Icelandic** → -sson is male, -dottir is female. Surnames are patronymic, not inherited. Honorific matches gender.  
* **Myanmar, Cambodian** → full name on all references, no honorific. Sole exception: Aung San Suu Kyi → Ms Suu Kyi.  
* **All other / unknown** → western convention (John Smith → Mr Smith)

Forms are not mixed within a story. Naming conventions are unchanged by location. Mr Shibahashi is Mr Shibahashi in Bangkok as in Tokyo.

#### Honorifics — application

Mr and Ms apply to civilians, no full stop. Dr applies only to practising medical doctors, not to academic or other doctorates. Khun is reserved for direct quotes.

An honorific attaches to a surname given in copy: a person the copy names without a surname carries no honorific after first mention.

Higher ranks are retained on all references: Sir, Lord, ML, MR, Khunying, Thanphuying, Phra, royal titles, police and military ranks.

British royals carry first name plus title throughout (Prince William, not William).

#### Title capitalisation

A title directly prefixing a full name takes caps as the general rule ("Prime Minister Anutin said", "Foreign Minister X said", "Deputy Transport Minister Phattrapong Phattraprasit", "Governor Chadchart Sittipunt"). This sweeps in senator, governor, mayor and deputy-spokesperson-type posts — previously lowercase exceptions. (Ruled 110726; caps-before-full-name confirmed against live bangkokpost.com usage.)

A title standing alone, without a name, is lower case ("the prime minister said", "the governor added").

Former titles are always lower case ("former prime minister Yingluck Shinawatra").

Titles appear before names, not after: "Secretary of State Rex Tillerson said", not "Rex Tillerson, secretary of state, said".

#### Honorifics — removal

Convicted criminals: honorific stripped, police and military ranks and royal titles retained. Deceased: same. Officially missing persons retain honorifics, except where the person has been missing long enough to be almost certainly dead.

Celebrities, sportspeople, authors (non-academic), journalists, artists, actors, musicians and filmmakers carry no honorific.

#### Proximity Alert — flag only, names only

**A name sits close to a held form but differs → flag it, change nothing. The operator rules.**

A Proximity Alert fires when an incoming personal name sits close to a form the desk already holds — a shared surname, a familiar given-name shape, a known transliteration — but diverges from it. Raise it as: "Proximity Alert: [copy form] sits near [held form] — for operator deviance check."

Proximity is observation, not action. The alert is a note on this copy, not a property pinned to the name: one that proves out graduates into a rule or a listed entity, one that doesn't lapses with the alert. The copy may be wrong or the held form may have drifted — the alert opens that question, an operator ruling closes it, and only then is the form changed and logged.

It catches rogue copy early and widens the desk's eye over the core concern of all news — the leading protagonists. An absent alert is not an all-clear; the eye stays open.

#### Ranks and titles

Ranks and titles come from the copy. Where rank appears anywhere in copy, it applies consistently throughout. Where copy is silent and the rank is unclear, the full name is repeated or the gap is flagged.

#### Heads, decks, quotes

Heads and decks carry no honorifics. Quotes preserve what was spoken; honorifics are not added or bulk-replaced.

### Thai PM

A prime minister is not a head of state. Heads of state are presidents or monarchs. The Thai PM is never referred to as head of state.

### "Thai" prefix

Superfluous as a free adjective in most contexts — "the Thai government", "the Thai capital of Bangkok". The prefix is stripped unless it differentiates from another country in the same context.

This rule applies only to the loose adjective. Acronyms and proper names retain "Thai" in full: TAT, RTAF, RTN, RTP, RTA, Thai Airways, Thai Beverage, Thai PBS, Bank of Thailand.

### Acronyms in heads

Pronounceable acronyms take title case: Fifa, Asean, Nasa, Opec, Unesco.

Three-letter initialisms and non-pronounceable strings take all caps: FBI, NBTC, PRD, CNN, HIV.

MILF stays all caps (Moro Islamic Liberation Front) — house ruling, avoids slang collision.

### Country abbreviations in heads

UK and US appear anywhere. NZ, HK, LA, NY, SK, NK, S Africa, S Sudan and Aus appear in heads and decks. PNG and DRC appear in heads, or in body after the full first reference.

## SPATIAL MECHANICS

The rules in this part address one flaw: the model's innate counting is unreliable. There are two valid answers to that flaw, and this part uses both. Where the operation suits it, design around counting entirely — substitution whose volume is preserved by construction ("1-in / 1-out" and "swap heavy for lean" are the operations themselves, not shorthand for "preserve length" or "make it narrower"). Where the operation needs a real number, hand the count to an external tool that does it deterministically. Bringing in Python to count is not a departure from this part's logic — it is the same flaw corrected by the same principle, with an external mechanism instead of an avoidance design.

So: the body-text footprint change (Overspill below) is counted with a verified character tool **where the model can run one** — and falls back to 1-in/1-out substitution where it cannot. The DCX headline protocol stays on substitution and does no counting. **Scale sets the method.** An unverified figure is reliable at headline length and worthless at body length — error grows with the string. A head or deck is short enough that an unverified figure lands inside a two-character band, so DCX needs no tool. A body is not, and takes Route A or Route B. The rule is not where a count comes from; it is that no unverified figure is ever asserted for a story.

**Route depends on the actor.** Not every model can execute code: a Python `len()` count is exact and preferred, but Gemini cannot run Python and other models may not fire it up. The overspill procedure therefore specifies BOTH paths — Option A (verified count) and Option B (1-in/1-out substitution) — and the model or operator takes whichever the situation allows. Option B is not deprecated; for some actors it is the only path.

### Editing Scope

* Two states, distinguished by whether the operator has given a footprint instruction.  
* Footprint instruction given — hold, halve, trim, grow, a DCX budget, or overspill marked. Do exactly that. The instruction is a concrete spatial target: the copy is being worked into its allotted slot. Hit it via 1-in/1-out substitution and structural tweaking. The full house-style pass always applies — style fixes are never skipped to protect width; where a fix shifts width, absorb it in the swap or hold and flag for the operator's fit.  
* No footprint instruction — edit freely for structure, sequence, hierarchy, paragraphing and narrative logic. The 10% bloat allowance applies: Thai-to-English translation introduces padding, so the smallest-intervention rule is suspended for structural bloat — cut up to 10% to clear tautology, passive voice and fat, provided the core narrative stays intact. Cuts beyond 10% are logged.  
* "Fits" is a footprint instruction: the slot is already met — no bloat-cutting, no footprint-changing rewrites, full style pass still expected. Hand back the footprint intact; the operator makes final width adjustments. Fit > elegance.
* Sub-heads removed from a story free space the body inherits: increase the body footprint to fill it rather than leave the gap.  
* Default target of every edit: land just over, never under — overmatter shaves at paste; undermatter leaves a physical gap in the column. The model's observed drift is to cut slightly under: that is the fault to correct, not caution.
* News-story opening paragraphs carry a soft limit of 30 words (Kevin's rule, operator-ruled 110726). Soft means target, not gate: an intro that must run longer to hold the fact runs longer, but default drafting and free edits bring news intros in at or under 30. Overruns that stand are flagged in the Style Log. Scope: news stories only — features, columns, editorial and PR copy are untouched.

### Overspill (body-text footprint change)

A footprint change to story BODY targets a character figure, reached by ONE OF TWO ROUTES depending on what the actor can do (see Route A / Route B below). Either way the desk never asserts a manually tallied figure for a body — the historical root of overspill error. (Headlines are NOT covered here — they stay on the DCX spatial protocol below.)

**Unit:** characters with spaces — the .dcx-native measure (probe-confirmed: .dcx counts the space). Under Route A this is `len(text)`; under Route B it is approached by substitution, never by manual tallying.

**Input (preferred): the .dcx pair** — "story = X chars, box = Y chars". The spill is `X - Y`, exact, from verified figures; the proportion is built on these, never on the model's own baseline count. (Fallback input: a signed spill — +N remove, -N add.)

**No cut point.** There is no marked overspill position; only a character target against the whole body. The team often picks a story imagining its own cut points into a smaller box — that imagined cut is not the instruction. Recast the whole story to the target by value; if the imagined cut coincides with the low-value material, fine, but arrive there by reading the story, not by inheriting the guess.

**Selection — recast by value, not position:**

* Assess every block by news value; remove lowest-value material wherever it sits. Surplus is not assumed to be at the tail.
* LOW value (cut first): redundant restatement, secondary/third-tier incident, transitional or hedging line, background already implied, colour that adds no fact.
* HIGH value (protect): the core event, named-source quotes, figures, the causal "why", consequence, anything not stated elsewhere.
* Inverted pyramid is a tendency, not a rule: value usually thins toward the bottom, BUT copy often holds a key fact for the final paragraph (kicker). Read the last paragraph before cutting it — never reflex-trim from the bottom.
* One fact in one place: if information appears twice, cut the weaker instance.
* Whole weak block before gutting a strong one.

Both routes share the same selection logic above and the same goal: land OVER target, never under. Overmatter can be shaved at paste (trim the last line to fit); undermatter leaves a physical gap in the column that is harder to fill. They differ only in HOW the character figure is met.

**Route A — VERIFIED COUNT (when the actor can run code).**
The exact, preferred path. Two passes, not a loop:

1. `spill = X - Y` from the .dcx pair. Judgment first pass: cut by value aimed at the proportion — no count yet. The sweep aims; the tool confirms.
2. One `len()` count: check the swept copy against Y, set the exact residual.
3. Correct the residual by adjusting already-counted material (length known from the verify pass — no recheck if landing just OVER). A rewrite makes new uncounted text, so it costs one more count.
4. Strip model-introduced markup before reporting the count — no crosshead flags or notes survive into counted copy or the deliverable:
   ```python
   import re
   clean = re.sub(r'^\s*\[[A-Z][^\]]*\]\s*', '', body, flags=re.M)
   print(len(clean))   # the reported figure
   ```
*Calibration (free):* the verify count should match X. If it drifts, the counter has diverged from .dcx — surface it; trust neither number silently.

*Paragraph breaks* count as single newlines for Route A verification — the .dcx field counts a break as one character. Double-newline counting runs ~1 char heavy per break. Normalise before `len()`: `clean = clean.replace('\n\n', '\n')`

**Route B — 1-IN / 1-OUT SUBSTITUTION (when the actor cannot count, or chooses not to).**
The equal-standing fallback — and the ONLY path for models that can't run code (e.g. Gemini) or won't (e.g. ChatGPT declining to fire Python). Not deprecated.

1. Work from the .dcx pair / spill the same way — recast by value to hit the target proportion.
2. Hold the footprint by **substitution, not tallying**: swap heavy phrasing for lean, trade a long construction for a short one, so volume is preserved or reduced *by construction* rather than measured. To cut a line, trim a paragraph with a short final line (the cut that removes a physical line); to grow, the reverse.
3. The operator carries the exact figure — Route B lands *close*, and the operator squeezes the last char or two on paste. The model does NOT assert a precise count it cannot verify; it states what it changed, not a number.

**Choosing the route:** run Route A if you can execute a counter; otherwise Route B. Either is house-valid. The failure mode to avoid is a non-coding model asserting a precise count reached by manual tallying — that is the original error both routes exist to prevent.

**Story priority.** Prioritise telling the headline story properly over maintaining multiple narratives. The minimum deliverable is one relatively complete news story told to the fullest the space allows. Better to drop a story and tell the survivor(s) well — the dropped one can run online — than run two stories badly under one head. Where a whole story is dropped, record it in the Style Log in one sentence (what it was). Log trims and the drop decision.

News-value ranking is the desk's call, made on editorial worth alone and without reference to where any fold falls. A design-imposed boundary is a spatial fact, never a value bar.

### DCX fit

*This ONLY triggers when the user supplies a budget in DCX units (e.g., "Budget: DCX34"). Otherwise, write sharp, active sentence-case headlines — short by default. Michael's standing preference: short, sharp heads. Between candidates that both say the thing, the shorter is first choice; length is never padded for its own sake. Where a DCX budget is supplied, the budget still governs fit.*

The desk may *aim* at ±2 but does not assert the figure: the DCX field is the real counter and the operator confirms on paste. Desk aims, field measures, operator confirms.

**The budget figure:** a DCX/BKP budget number is a TOTAL across however many lines, never per-line. The field may not populate correctly until text is pasted — a quoted figure can rise on paste (deck 23 -> 35) — so confirm against the rendered figure before treating it as binding.

1. **Draft to Budget:** Draft to the exact DCX numerical budget provided. You must hit this target within a strict ±2 character margin. For multi-line heads, balance the lines with a maximum ±1 character difference between them. The working figure runs slightly optimistic at narrower slots, so aim for the lower end of your ±2 margin by default.
2. **Tessellation (The Virtual Ruler):** When executing spatial tweaks (e.g., "Overset", "Underset"), evaluate the typographic weight of the line using this heuristic:
   * **Baseline (1.0 unit):** Standard letters (a, e, n, o, p, etc.)
   * **Lean (0.5 units):** Narrow glyphs (i, l, t, f, r, s, j, spaces, punctuation)
   * **Heavy (1.5 units):** Wide glyphs (m, w, M, W, O, Q, G, C)
   * **Overset:** Swap 1.0/1.5 unit glyphs for 0.5 unit glyphs to reduce the total spatial score.
   * **Underset:** Swap 0.5 unit glyphs for heavier glyphs to widen the physical footprint.

## PR HANDLING

PR copy is a minimum-intervention style pass — a basic read-through with house conventions applied where the structure permits. The frame is spellcheck-plus-style, not editing.

### Minimal edit

* Spelling: US to UK  
* Place names: client spellings to BKP forms (per REFERENCE)  
* Honorifics: house conventions applied  
* Punctuation: house style (Oxford comma removed)  
* Currency, dates and numbers: CONVERSIONS rules apply  
* Plain errors of grammar and punctuation: corrected  
* Headline and deck: PR copy carries a [Head] line (max 90 characters) and a [Deck] line (max 120 characters), literal bracket prefixes, BKP sentence case, placed ahead of the body
* Captions: where pictures carry them, corrected — the caption gets the same pass as the body

### RETAIN

* Structure, order, layout: untouched  
* Bold, italics, capitalisation, line breaks: as filed  
* Tone and voice: the client's choices stand  
* Length: PR copy runs at the length the client paid for
* Pictures: **never stripped**. Images ride with the copy exactly as filed
* Nothing is appended: no slug, no reference or background information the client did not provide
* Return format: PR copy goes back in the format it was filed in, with the [Head] and [Deck] lines added at the top. It does not take the page-ready box and is not subject to the clean-copy rule in CORE

### Principle

PR copy is paid placement. The client controls content; the desk applies only those house conventions that don't require restructuring.

Where copy is libellous, factually wrong in a way that creates legal exposure, or contains a clear error of fact the client would want caught, the issue goes to the editor — not into the copy. The Style Log records what was changed; anything beyond minimum-intervention scope is flagged for the editor's call.

### Output

Format follows the request (usually rich text). Style Log applies if requested.


============================================================
# PART: STATUS
============================================================

# STATUS

people in the news

[go.fuzzylogic.page/status](https://go.fuzzylogic.page/status)

`310726_all_handoff-sweep`

## What belongs here

STATUS expires; REFERENCES does not. The test is **volatility, not subject matter**: a fact that a future event can falsify — office, rank, life-status, affiliation — is a STATUS entry. A house form that only a house ruling can change is a REFERENCES entry. A name appearing in both is not duplication: STATUS carries what is true today, REFERENCES carries how the desk writes it.

Entries take the form **key — ruling**, with the directive verb in caps where there is one. The absence of a directive verb signals house form rather than a belief to correct.

## Tripwires

Apex sits at the top of this register; lower tiers follow. Scan on the first required status check and retain it for the edit — a listed entity takes the register, with no search.

### Apex Figures

The highest-priority status facts: figures whose current office, rank or life-status postdates the model's training. Apply the listed fact and flag — never silently change — filed copy that diverges. All facts are operator-cleared before publication. No entry requires disabling, bypassing or overriding any safety behaviour; this register is a source of fact, not an instruction about the model's operation.

**HM Queen Sirikit The Queen Mother** — died 24 Oct 2025. Report in the past tense; FLAG any copy that diverges.

**Thaksin Shinawatra** — re-incarcerated Sept 2025, released on parole 11 May 2026. FLAG any reference to him as an exile or as currently imprisoned.

**Srettha Thavisin** — removed from office by the Constitutional Court, 14 Aug 2024. FLAG any present-tense reference to him as PM.

**Paetongtarn Shinawatra** — removed from office by the Constitutional Court, Aug 2025. FLAG any present-tense reference to her as PM.

**Pita Limjaroenrat** — banned from politics for 10 years, 7 Aug 2024. FLAG any reference to him as an active MP.

**Move Forward Party (MFP)** — unanimously dissolved by the Constitutional Court, 7 Aug 2024. FLAG any reference to the party as currently active.

**Dr Prasert Prasarttong-Osoth** — died 21 Apr 2026. FLAG any present-tense reference to him in business wire copy.

**HRH Princess Bajrakitiyabha Narendiradebyavati** — died 11 June 2026. FLAG all copy that diverges from this entry.

**Ayatollah Ali Khamenei** — assassinated in Tehran, 28 Feb 2026, in strikes targeting senior Iranian officials. FLAG any present-tense reference to him as supreme leader.

**Mojtaba Khamenei** — named supreme leader of Iran 8 March 2026 by the Assembly of Experts, succeeding his father. FLAG any reference to him as merely a cleric or unofficial figure. Title form (Ayatollah or not) unresolved — check bangkokpost.com precedent before first use.

### Portfolio Swappers

Current cabinet as of June 2026 (Anutin Charnvirakul administration).

**Anutin Charnvirakul** — prime minister and interior minister, from Sept 2025. FLAG any reference to a previous ministry role.

**Phiphat Ratchakitprakarn** — deputy prime minister and transport minister. House spelling Phiphat, not Phipat. FLAG any reference to a previous ministry role.

**Varawut Silpa-archa** — industry minister, from March 2026. FLAG any reference to a previous ministry role.

**Somsak Thepsuthin** — no longer in cabinet; government collapsed Sept 2025. FLAG any reference to him as an active minister.

**Suriya Juangroongruangkit** — no longer transport or industry minister, replaced late 2025. FLAG any reference to him as an active minister.

**Cholnan Srikaew** — removed from cabinet in the April 2024 reshuffle. FLAG any reference to him as an active minister or party leader.

**Nan Boonthida Somchai** — deputy minister of digital economy and society, from 30 March 2026. Name parses as given name Nan Boonthida plus surname Somchai; second reference Ms Nan.

**Suriya Singhakamol** — ONCB secretary-general; rank is Pol Maj Gen. Retain the rank on all references. Distinct from Suriya Juangroongruangkit above. (Provenance: desk held "Pol Maj", unverified; corrected against bangkokpost.com copy, verified 110726, flight-crew heroin case.)

## Second tier

### Political and Legal Reversals

**Thanathorn Juangroongruangkit** — acquitted of royal defamation charges, May 2026.

**Saksayam Chidchob** — removed for ethical misconduct March 2024; cleared by the NACC April 2026.

**Arnon Nampa** — incarcerated, serving a multi-year sentence.

**Rukchanok 'Ice' Srinork** — sentenced to six years, out on bail.

**Nikorn Chamnong** — party-list MP and board member for the Bhumjaithai Party. FLAG any reference to him as Chartthaipattana; accept BJT affiliations.

**Stithorn Thananithichot** — political scientist at Chulalongkorn University. FLAG any reference to him at King Prajadhipok's Institute; accept Chulalongkorn affiliations.

**Korn Chatikavanij** — Democrat Party list-MP and deputy leader for economic affairs; chairman of the party policy committee. Named one of three Democrat prime ministerial candidates, with Abhisit Vejjajiva, for the 8 Feb 2026 general election. FLAG any reference to him as a Chart Pattana Kla or Kla figure, or as a sitting finance minister.

**Chaichanok Chidchob** — minister of digital economy and society. House spelling Chidchob, not Chidchorb. FLAG any reference to him in another ministry role.

**Chadchart Sittipunt** — re-elected Bangkok governor 28 June 2026 with a record 1,537,784 votes; second term began 9 July 2026. Ran as an independent after resigning early in May 2026. Take "incumbent" or "governor" as filed; FLAG "former" or any first-term framing. Capped before the full name per the title rule: Bangkok Governor Chadchart Sittipunt.

### Mortalities and Successions

**Gen Suchinda Kraprayoon** — died June 2025.

**Man Phatnothai** — died May 2026.

**Dr Wanlop Thaineua** — died April 2026.

**Chonsawat Asavahame** — died 2023; triggered the Pak Nam faction power vacuum.

**Chodchoy Thavisin** — died 2024.

**Pope Francis** — died 2025.

**Dick Cheney** — died 2025.

**Jane Goodall** — died 2025.

**Charlie Kirk** — died 2025.

### Corporate Leadership Changes

**Brenton Justin Mauriello** — CEO of Raimon Land, from April 2024.

**Pisit Thangtanagul** — CEO of PwC Thailand, from 2024.

### Global Figures

**Donald Trump and JD Vance** — sitting president and vice-president of the United States, from 20 Jan 2025. FLAG any reference to them as private citizens or former officials. Standard title capitalisation and second-reference rules apply: Mr Trump, Mr Vance.

**King Charles III** — active monarch, operating alongside a cancer treatment protocol; treatment reduced Dec 2025 to precautionary monitoring.

**To Lam** — general secretary of the Communist Party of Vietnam, since 2024, and 13th president of Vietnam, since 2026. Both titles current. ACCEPT 'president' or 'general secretary' as filed. House lowercases 'president' before a name; Vietnamese second reference is Mr Lam.


============================================================
# PART: REFERENCES
============================================================

# REFS

the knowledge base

[go.fuzzylogic.page/refs](https://go.fuzzylogic.page/refs)

`310726_all_handoff-sweep`

## COUNTRIES
Country-name rulings, naming conventions, abbreviation forms.
### Preferred forms
**Myanmar** — Not Burma.

**Türkiye** — Updated from Turkey.

**Netherlands** — Not Holland; government seat is The Hague (cap "The").

**DR Congo** — Distinguish from Republic of Congo; DRC acceptable in headlines and body after full name.

**Czech Republic** — Avoid Czechia.

**East Timor** — Avoid Timor-Leste.

**Ivory Coast** — Avoid Cote d'Ivoire.

**Gambia** — Avoid "The Gambia".

**United Kingdom** — Avoid Britain; UK preferred. The UK INCLUDES Northern Ireland; Great Britain is the one that excludes it (England, Scotland, Wales only). Not interchangeable.

### Adjectival / demonym traps
**Argentina** — Argentine (people); Argentinian (things).

**Cambodia** — Khmer = language only, not people.

**Comoros** — Comoran (people); Comorian (language).

**Madagascar** — Malagasy (plural same as singular).

**Mauritania** — Mauritanian (not Mauritian).

**Niger** — Nigerien (not Nigerian).

**Philippines** — Filipino (male/neutral); Filipina (female).

**Somalia** — Somali (people); Somalian (adjective for things).

**Vanuatu** — Avoid Ni-Vanuatu.

### Capitals and country structure
**Australia** — Labor Party (no "u").

**Chad** — Capital N'Djamena (apostrophe).

**Laos** — Lao (not Laotian) for people.

**Malaysia** — Putrajaya is admin capital; Kuala Lumpur is capital.

**Moldova** — Avoid Moldavia.

**Monaco** — Monte Carlo is a district, not the capital.

**Myanmar language** — Language is Burmese (not Myanmar).

**Palestine** — Ramallah is admin centre; largest population in Gaza.

**South Africa** — Three capitals — Pretoria (executive), Cape Town (legislative), Bloemfontein (judicial).

**Sri Lanka** — Capital is Kotte (not Colombo).

**China** — Taiwan separate; Hong Kong and Macau are SARs.

**United States** — Write state names in full (New Jersey not NJ).

### Headline abbreviation forms
**NK** — North Korea (headlines only).

**SK** — South Korea (headlines only).

**NZ** — New Zealand (headlines only).

**STP** — Sao Tome and Principe (headlines).

**UAE** — United Arab Emirates.

**Saudi** — Saudi Arabia (headlines only).

**DRC** — DR Congo (headlines, or body after full first reference).

**PNG** — Papua New Guinea (headlines, or body after full first reference).

### "the" article
**"The" as part of a country name** — drop "the" before Congo, Ukraine, Sudan, Lebanon. Keep "the" for adjective-led names (the United States, the Democratic Republic of Congo) and plural-form names (the Bahamas, the Maldives). Seychelles is NOT plural — named after a person — so no "the".

## FOREIGN PLACES
Place names whose BKP form diverges from common spelling or transliteration.
AUSTRALIA: - Uluru (not Ayer's Rock) - Western Australia (cap the W)
AZERBAIJAN: - Nagorny-Karabakh
BANGLADESH: - Cox's Bazar - Shah Porir Dwip
BELGIUM: - Molenbeek
BOSNIA & HERZEGOVINA: - Srebrenica
BRAZIL: - Brasilia - Sao Paulo
BURKINA FASO: - Ouagadougou
CAMBODIA: - Oddar Meanchey
CHILE: - Easter Island (not Rapa Nui)
CHINA: - Beijing (not Peking) - Chongqing - Guangxi - Guangzhou (not Canton) - Kashgar - Lhasa - Nanjing - Tiananmen Square - Urumqi - Xinjiang - Xishuangbanna
EGYPT: - Sharm el-Sheikh - Tahrir Square
GERMANY: - Cologne (not Koln) - Dusseldorf
GREENLAND: - Nuuk (not Godthab)
HONG KONG: - Mong Kok - Wanchai
ICELAND: - Eyjafjallajokul (volcano) - Reykjavik
INDIA: - Bengaluru (not Bangalore) - Chhattisgarh - Kolkata (not Calcutta) - Mumbai (not Bombay) - Puducherry (not Pondicherry) - Thiruvananthapuram
INDONESIA: - Yogyakarta
IRAN: - Lake Urmia - Tehran
IRAQ: - Irbil (not Urbil, Arbil or Erbil) - Fallujah
ISRAEL: - al-Aqsa Mosque (lower case al-)
ITALY: - Naples (not Napoli) - Pompeii
JAPAN: - Fukushima - Fukushima Dai-ichi nuclear plant - Yasukuni shrine
KAZAKHSTAN: - Baikonur
KIRIBATI: - Kiritimati Island (not Christmas Island)
MOLDOVA: - Transnistria
MONGOLIA: - Gandantegchenlin - Ulan Bator
MOROCCO: - Tangier
MYANMAR: - Irrawaddy - Ka Htaung Ni - Kawthaung (not Victoria Point) - Mawlamyine (not Moulmein) - Myawaddy - Myitkyina - Nay Pyi Taw - Tachileik - Thabyuchaung - Yangon (not Rangoon)
NEPAL: - Birganj - Everest Base Camp (all capped) - Kathmandu - Khumbu Icefall - Nepalganj
NETHERLANDS: - The Hague (cap "The")
NIGERIA: - Maiduguri
NORTH KOREA: - Punggye-ri Nuclear Test Site - Rason (not Rajin)
RUSSIA: - Ekaterinberg - Nizhny Novgorod - Rostov-on-Don - St Petersburg
SOUTH AFRICA: - Hluhluwe-iMfolozi Game Reserve - KwaZulu-Natal
SWEDEN: - Gothenburg (not Goteburg)
SYRIA: - Ain al-Arab (prefer Kobane unless in quotes) - Dara'a - Deir al-Zor - Douma - Hasakah - Hmeimim airbase (lower-case airbase) - Kobane (preferred form) - Raqqa
TANZANIA: - Dar-es-Salaam
TURKEY: - Taksim Square
UKRAINE: - Ilovaysk - Luhansk - Lviv
UNITED STATES: - Hawaii - Papahanaumokuakea Marine National Monument - Pearl Harbor - Washington DC
VIETNAM: - Da Nang - Gulf of Tonkin (not Tonkin Bay) - Hanoi - Ho Chi Minh City (not Saigon) - Hoi An
YEMEN: - Hadramawt - Sana'a - Seyoun
## FOREIGN PEOPLE
Convention exemplars, title retention, spelling traps.
Dead, retired, or off-radar figures from the 2018 source have been dropped.
Mao and Mother Teresa are kept because they still teach the rule.
### Chinese: surname first, Mr + surname on second ref
**Xi Jinping** — second reference Mr Xi. Chinese convention (surname first).

**Li Keqiang** — second reference Mr Li. Chinese convention.

**Mao Zedong** — Historical; no honorific.

**Deng Xiaoping** — Historical; no honorific.

### Indonesian: variable; consult
**Joko Widodo** — second reference Mr Widodo. Do not use "Jokowi" except in quotes. Indonesian second-reference convention is variable across this block — some take Mr/Ms + last component, some take given name, some are single-name. Consult each entry; default to DCX precedent if unsure.

**Susilo Bambang Yudhoyono** — second reference Mr Yudhoyono. Indonesian — uses surname on second ref.

**Basuki Tjahaja Purnama** — Indonesian — verify second-ref form per DCX precedent.

### Myanmar/Cambodian: full name throughout
**Aung San Suu Kyi** — second reference Ms Suu Kyi. Myanmar and Cambodian names use full name on all references with no honorific. Aung San Suu Kyi is the sole exception and takes Ms Suu Kyi on second reference.

### Title retention
**Ayatollah Ali Khamenei** — Deceased Feb 2026 — see STATUS. Kept as an example — the title "Ayatollah" stays on all references. (Title-retention rule applies across this block — Ayatollah, King, Pope, Prince, Duchess, etc all kept on every reference.).

**King Salman bin Abdulaziz al-Saud** — "King Salman" usually suffices.

**King Jigme Khesar Namgyel Wangchuck** — Bhutanese king; full title first reference.

**Pope Emeritus Benedict XVI** — "Pope Benedict" usually suffices.

**Catherine, Duchess of Cambridge** — Not Princess.

**Prince William** — British royals retain "Prince" on all references — not just "William".

### Given-name-as-surname (Mahathir, Sabah)
**Mahathir Mohamad** — second reference Mr Mahathir. Given name used as surname on second ref. This pattern applies across the block — for Mahathir, Sabah and similar where the given name conventionally serves as the surname on second reference.

**Sheikh Sabah al-Ahmad al-Sabah** — second reference Mr Sabah. First name used as surname on second ref.

**Mahmoud Abbas** — second reference Mr Abbas. Standard Arabic convention.

### Arabic al- drop on second ref
**Bashar al-Assad** — second reference Mr Assad. Arabic names with al-/el- prefix carry the full form on first reference and drop the prefix on second reference (Mr Assad, Mr Sissi). Lower-case al-. Exception for company names — Al Jazeera retains the cap.

**Abdel Fattah el-Sissi** — second reference Mr Sissi. Drop "el-" on second ref.

**Abed Rabbo Mansour Hadi** — second reference Mr Hadi. Yemen — Hadi is the surname.

### Korean: family name + hyphenated given name
**Kim Jong-un** — second reference Mr Kim. Korean convention; hyphenated given name, second component lower case.

**Ban Ki-moon** — second reference Mr Ban. Korean convention.

**Syngman Rhee** — Historical; pre-modern romanisation retained.

### Vietnamese: given name is last in sequence
**Nguyen Xuan Phuc** — second reference Mr Phuc. Vietnamese — given name is the last component.

**Ngo Dinh Diem** — Historical.

### Argentinian / shortened-name rulings
**Cristina Kirchner** — Drop "de Fernandez" from the middle.

### Single-name rule / no honorific
**Mother Teresa** — No H in Teresa; no honorific. Single-name rule — figures known by one name (Mao, Suharto, Mother Teresa) take no honorific. Same applies to deceased non-political figures and to celebrities, sportspeople, musicians and artists regardless of name length.

**Muhammad Ali** — No honorific (deceased; sportsperson).

**Jay-Z** — Hyphenated.

**Tupac Shakur** — No honorific (deceased; musician).

**Pharrell Williams** — No honorific (musician).

### Pakistani / British boxer name confusion
**Aamir Khan** — The actor (Pakistani). The British boxer is Amir Khan — different spelling.

**Amir Khan** — The boxer (British). The Pakistani actor is Aamir Khan.

### Spelling traps
**Sid'Ahmed Raiss** — Apostrophe in Sid'Ahmed; NOT Rais.

**Micheal Martin** — Irish spelling — "Micheal" NOT Michael.

**Tony Abbott** — Two Ts in Abbott.

**Moammar Gadhafi** — BKP form; no Col honorific.

**Recep Tayyip Erdogan** — Standard spelling — no accents.

**Voreqe Bainimarama** — Fiji; do not use "Frank" as first name.

**Salva Kiir** — South Sudan; not David Kiir.

## THAI PLACES
BKP THAI GEOGRAPHY INDEX
Use RTGS transliteration. Global rules: Muang (not Mueang), Phra (not Pra), Chai (not Chay), Isan (not Isaan).
### Transliteration master rules
transliteration_rules: - Muang (not Mueang) - Phra (not Pra) - Chai (not Chay) - Isan (not Isaan) - Klong (not Khlong) — Klong Toey is the BKP form, NOT Khlong Toei - Soi format — Sukhumvit Soi 12 (not Soi Sukhumvit 12, not Sukhumvit 12 Road) - Soi [Name] only when soi has its own distinct name — Soi Nana, Soi Sala Daeng, Soi Sribamphen - Rama roads — Roman numerals; Rama IX Road, never Phra Ram - Postcodes — no comma; Bangkok 10900 (not Bangkok, 10900)
airports: - Two Bangkok airports — always specify Don Muang or Suvarnabhumi - Never "Bangkok airport" - '"Suvarnabhumi airport" suffices for body text; "Suvarnabhumi International Airport" only when using official name'
third_party_spellings: notes: | Some institutions named after places spell their own names differently from BKP house style. Follow their official spelling for their name. Examples — Hatyai Hospital (BKP spells the town "Hat Yai"), Prince of Songkla University (not "Songkhla"), Sriracha Tiger Zoo (not "Sri Racha"), Minburi Prison (BKP spells the district "Min Buri"), Khlong Prem Prachakon (canal/prison area — an institutional name, exempt under this rule; the transliteration rule itself is in Transliteration master rules above).
provinces: Amnat Charoen: [Muang Amnat Charoen, Chanuman, Phana, Hua Thapan, Pathumrat Wongsa, Senangkhanikhom, Lue Amnat] Ang Thong: [Muang Ang Thong, Chaiyo, Pa Mok, Pho Thong, Samko, Sawaengha, Wiset Chai Chan] Ayutthaya: [Phra Nakhon Si Ayutthaya, Ban Phraek, Bang Ban, Bang Pahan, Bang Pa-in, Bang Sai, Lat Bua Luang, Maha Rat, Nakhon Luang, Phachi, Phak Hai, Sena, Uthai, Wang Noi] Bangkok: [Bang Bon, Bang Kae, Bang Kapi, Bang Khen, Bang Kholaem, Bang Khunthian, Bang Na, Bang Phlat, Bang Rak, Bang Sue, Bangkok Noi, Bangkok Yai, Bung Kum, Chatuchak, Chom Thong, Din Daeng, Don Muang, Dusit, Huai Khwang, Kannayao, Klong San, Klong Toey, Laksi, Lat Krabang, Lat Phrao, Min Buri, Nong Chok, Nong Khaem, Pathumwan, Phasicharoen, Phaya Thai, Phra Khanong, Phra Nakhon, Pomprap Sattruphai, Prawet, Rat Burana, Ratchathewi, Sai Mai, Saphan Sung, Samphanthawong, Sathon, Suan Luang, Taling Chan, Thon Buri, Thung Kru, Watthana, Yannawa] Bung Kan: [Muang Bung Kan, Bung Khong Long, Pak Khat, Phon Charoen, Phon Phisai, Seka, Si Wilai, So Phisai] Buri Ram: [Muang Buri Ram, Ban Dan, Ban Kruat, Chamni, Chaloem Phra Kiat, Huai Rat, Khaen Dong, Khu Mueang, Krasang, Lahan Sai, Lam Plai Mat, Na Pho, Nang Rong, Non Din Daeng, Non Suwan, Pakham, Phlapphla Chai, Prakhon Chai, Phutthaisong, Satuek] Chachoengsao: [Muang Chachoengsao, Ban Pho, Bang Kla, Bang Nam Priao, Bang Pakong, Khlong Khuean, Phanom Sarakham, Plaeng Yao, Ratchasan, Sanam Chai Khet, Tha Takiap] Chai Nat: [Muang Chai Nat, Hankha, Manorom, Noen Kham, Nong Mamong, Sankhaburi, Sapphaya, Wat Sing] Chaiyaphum: [Muang Chaiyaphum, Bamnet Narong, Ban Khwao, Ban Thaen, Chatturat, Kaeng Khro, Kaset Sombun, Khon San, Khon Sawan, Nong Bua Daeng, Nong Bua Rawe, Phakdi Chumphon, Phu Khiao, Sap Yai, Thep Sathit] Chanthaburi: [Muang Chanthaburi, Kaeng Hang Maeo, Khao Khitchakut, Khlung, Laem Sing, Makham, Na Yai Am, Pong Nam Ron, Soi Dao, Tha Mai] Chiang Mai: [Muang Chiang Mai, Chai Prakan, Chiang Dao, Chom Thong, Doi Lo, Doi Saket, Doi Tao, Fang, Galyani Vadhana, Hang Dong, Hot, Mae Ai, Mae Chaem, Mae On, Mae Rim, Mae Taeng, Mae Wang, Phrao, Samoeng, San Kamphaeng, San Pa Tong, San Sai, Saraphi, Wiang Haeng] Chiang Rai: [Muang Chiang Rai, Chiang Khong, Chiang Saen, Doi Luang, Khun Tan, Mae Chan, Mae Fa Luang, Mae Lao, Mae Sai, Mae Suai, Pa Daet, Phan, Phaya Mengrai, Thoeng, Wiang Chaeng, Wiang Chiang Rung, Wiang Kaen, Wiang Pa Pao] Chon Buri: [Muang Chon Buri, Ban Bueng, Bo Thong, Bang Lamung, Koh Chan, Koh Sichang, Nong Yai, Phan Thong, Phanat Nikhom, Sattahip, Si Racha] Chumphon: [Muang Chumphon, Lamae, Pathio, Phato, Sawi, Tha Sae, Thung Tako] Kalasin: [Muang Kalasin, Don Chan, Huai Mek, Huai Phueng, Kamalasai, Khao Wong, Khong Chai, Kuchinarai, Na Mon, Na Khu, Nong Kung Si, Rong Kham, Sahatsakhan, Sam Chai, Somdet, Tha Khantho, Yang Talat] Kamphaeng Phet: [Muang Kamphaeng Phet, Bueng Samakkhi, Khanu Woralaksaburi, Khlong Khlung, Khlong Lan, Kosamphi Nakhon, Lan Krabue, Pang Sila Thong, Phran Kratai, Sai Thong Watthana, Trai Ngam] Kanchanaburi: [Muang Kanchanaburi, Bo Phloi, Dan Makham Tia, Huai Krachao, Lao Khwan, Nong Prue, Phanom Thuan, Sai Yok, Sangkhla Buri, Si Sawat, Tha Maka, Tha Muang, Thong Pha Phum] Khon Kaen: [Muang Khon Kaen, Ban Fang, Ban Haet, Ban Phai, Chonnabot, Chum Phae, Khao Suan Kwang, Kranuan, Manchakhiri, Nam Phong, Non Sila, Nong Na Kham, Nong Ruea, Nong Song Hong, Phu Pha Man, Phu Wiang, Pueai Noi, Sam Sung, Si Chomphu, Ubolratana, Waeng Noi, Waeng Yai] Krabi: [Muang Krabi, Ao Luk, Khao Phanom, Khlong Thom, Koh Lanta, Lam Thap, Nuea Khlong, Plai Phraya] Lampang: [Muang Lampang, Chae Hom, Hang Chat, Ko Kha, Mae Mo, Mae Phrik, Mae Tha, Mueang Pan, Ngao, Soem Ngam, Sop Prap, Thoen, Wang Nuea] Lamphun: [Muang Lamphun, Ban Hong, Ban Thi, Mae Tha, Pa Sang, Thung Hua Chang, Wiang Nong Long] Loei: [Muang Loei, Chiang Khan, Dan Sai, Erawan, Nong Hin, Na Duang, Na Haeo, Pak Chom, Pha Khao, Phu Kradueng, Phu Luang, Phu Ruea, Tha Li, Wang Saphung] Lop Buri: [Muang Lop Buri, Ban Mi, Chai Badan, Khok Charoen, Khok Samrong, Lam Sonthi, Nong Muang, Phatthana Nikhom, Tha Luang, Tha Wung] Mae Hong Son: [Muang Mae Hong Son, Khun Yuam, Mae La Noi, Mae Sariang, Pai, Pang Mapha, Sop Moei] Maha Sarakham: [Muang Maha Sarakham, Borabue, Chiang Kuan, Chuen Chom, Kae Dam, Kantharawichai, Kosum Phisai, Kut Rang, Na Chueak, Na Dun, Phayakkhaphum Phisai, Wapi Pathum] Mukdahan: [Muang Mukdahan, Camcha-i, Dong Luang, Khamcha-i, Nong Sung, Wan Yai] Nakhon Nayok: [Muang Nakhon Nayok, Ban Na, Ongkharak, Pak Phli] Nakhon Pathom: [Muang Nakhon Pathom, Bang Len, Don Tum, Kamphaeng Saen, Nakhon Chai Si, Phutthamonthon, Sam Phran] Nakhon Phanom: [Muang Nakhon Phanom, Ban Phaeng, Khaen Dong, Na Kae, Na Thom, Na Wa, Pla Pak, Phon Sawan, Renu Nakhon, Si Songkhram, Tha Uthen, That Phanom] Nakhon Ratchasima: [Muang Nakhon Ratchasima, Ban Lai, Bua Lai, Bua Yai, Chakkarat, Chaloem Phra Kiat, Chok Chai, Chum Phuang, Dan Khun Thot, Huai Thalaeng, Kaeng Sanam Nang, Kham Sakaesaeng, Kham Thale So, Khon Buri, Mueang Yang, Non Daeng, Non Thai, Non Sung, Nong Bun Mak, Pak Chong, Pak Thong Chai, Phimai, Phra Thong Kham, Prathai, Sida, Sikhio, Soeng Sang, Sung Noen, Thepharak, Wang Nam Khiao] Nakhon Sawan: [Muang Nakhon Sawan, Banphot Phisai, Chum Ta Bong, Chum Saeng, Kao Liao, Krok Phra, Lat Yao, Mae Wong, Nong Bua, Phaisali, Phayuha Khiri, Tak Fa, Takhli] Nakhon Si Thammarat: [Muang Nakhon Si Thammarat, Bang Khan, Cha-uat, Chaloem Phra Kiat, Chang Klang, Chian Yai, Chulabhorn, Hua Sai, Khanom, Lan Saka, Na Bon, Nopphitam, Pak Phanang, Phipun, Phrom Khiri, Ron Phibun, Sichon, Tha Sala, Thung Song, Thung Yai] Nan: [Muang Nan, Ban Luang, Bo Kluea, Chaloem Phra Kiat, Chiang Klang, Mae Charim, Na Noi, Na Muen, Phu Phiang, Pua, Santi Suk, Song Khwae, Tha Wang Pha, Thung Chang, Wiang Sa] Narathiwat: [Muang Narathiwat, Bacho, Chanae, Cho-airong, Ra-ngae, Rueso, Sri Sakhon, Sukhirin, Su-ngai Kolok, Su-ngai Padi, Tak Bai, Waeng, Yi-ngo] Nong Bua Lam Phu: [Muang Nong Bua Lam Phu, Na Klang, Na Wang, Non Sang, Si Bun Rueang, Suwannakhuha] Nong Khai: [Muang Nong Khai, Fao Rai, Pho Tak, Phon Phisai, Rattanawapi, Sa Khrai, Sangkhom, Si Chiang Mai, Tha Bo] Nonthaburi: [Muang Nonthaburi, Bang Bua Thong, Bang Kruai, Bang Yai, Pak Kret, Sai Noi] Pathum Thani: [Muang Pathum Thani, Khlong Luang, Lam Luk Ka, Lat Lum Kaeo, Nong Suea, Sam Khok, Thanyaburi] Pattani: [Muang Pattani, Kapho, Khok Pho, Mae Lan, Mai Kaen, Mayo, Nong Chik, Panare, Sai Buri, Thung Yang Daeng, Yarang, Yaring] Phangnga: [Muang Phangnga, Kapong, Khura Buri, Koh Yao, Thap Put, Thai Mueang, Takua Pa, Takua Thung] Phatthalung: [Muang Phatthalung, Bang Kaeo, Khao Chaison, Khuan Khanun, Kong Ra, Pa Bon, Pa Phayom, Pak Phayun, Srinagarindra, Tamot] Phayao: [Muang Phayao, Chiang Kham, Chiang Muan, Chun, Dok Khamtai, Mae Chai, Phu Kamyao, Phu Sang, Pong] Phetchabun: [Muang Phetchabun, Bueng Sam Phan, Chon Daen, Khao Kho, Lom Kao, Lom Sak, Nam Nao, Nong Phai, Si Thep, Wang Pong] Phetchaburi: [Muang Phetchaburi, Ban Laem, Ban Lat, Cha-am, Kaeng Krachan, Khao Yoi, Nong Ya Plong, Tha Yang] Phichit: [Muang Phichit, Bueng Na Rang, Dong Charoen, Pho Prathap Chang, Pho Thale, Sak Lek, Sam Ngam, Taphan Hin, Thap Khlo, Wachirabarami, Wang Sai Phun] Phitsanulok: [Muang Phitsanulok, Bang Krathum, Bang Rakam, Chat Trakan, Nakhon Thai, Noen Maprang, Phrom Phiram, Wang Thong, Wat Bot] Phrae: [Muang Phrae, Den Chai, Long, Nong Muang Khai, Rong Kwang, Song, Sung Men, Wang Chin] Phuket: [Muang Phuket, Kathu, Thalang] Prachin Buri: [Muang Prachin Buri, Ban Sang, Kabin Buri, Na Di, Prachantakham, Si Maha Phot, Si Mahosot] Prachuap Khiri Khan: [Muang Prachuap Khiri Khan, Bang Saphan, Bang Saphan Noi, Hua Hin, Kui Buri, Pran Buri, Sam Roi Yot, Thap Sakae] Ranong: [Muang Ranong, Kapoe, Kra Buri, La-un, Suk Samran] Ratchaburi: [Muang Ratchaburi, Ban Kha, Ban Pong, Bang Phae, Chom Bueng, Damnoen Saduak, Pak Tho, Photharam, Suan Phueng, Wat Phleng] Rayong: [Muang Rayong, Ban Chang, Ban Khai, Khao Chamao, Klaeng, Nikhom Phatthana, Pluak Daeng, Wang Chan] Roi Et: [Muang Roi Et, At Samat, Changhan, Chaturaphak Phiman, Chiang Khwan, Jung Han, Kaset Wisai, Moei Wadi, Nong Hi, Nong Phok, Pathum Rat, Phanom Phrai, Pho Chai, Phon Sai, Phon Thong, Selaphum, Si Somdet, Suwannaphum, Thawat Buri, Thung Khao Luang] Sa Kaeo: [Muang Sa Kaeo, Aranyaprathet, Khao Chakan, Khlong Hat, Khok Sung, Ta Phraya, Wang Nam Yen, Wang Sombun, Watthana Nakhon] Sakon Nakhon: [Muang Sakon Nakhon, Akat Amnuai, Ban Muang, Charoen Sin, Kham Ta Kla, Khok Si Suphan, Kusuman, Kut Bak, Nikhom Nam Un, Phang Khon, Phanna Nikhom, Phon Na Kaeo, Phu Phan, Sawang Daen Din, Song Dao, Tao Ngoi, Wanon Niwat] Samut Prakan: [Muang Samut Prakan, Bang Bo, Bang Phli, Bang Sao Thong, Phra Samut Chedi, Phra Pradaeng] Samut Sakhon: [Muang Samut Sakhon, Ban Phaeo, Krathum Baen] Samut Songkhram: [Muang Samut Songkhram, Amphawa, Bang Khonthi] Saraburi: [Muang Saraburi, Ban Mo, Don Phut, Kaeng Khoi, Muak Lek, Nong Don, Nong Khae, Nong Saeng, Phra Phutthabat, Sao Hai, Wang Muang, Wihan Daeng] Satun: [Muang Satun, Khuan Don, Khuan Kalong, La-ngu, Manang, Tha Phae, Thung Wa] Sing Buri: [Muang Sing Buri, Bang Rachan, In Buri, Khai Bang Rachan, Phrom Buri, Tha Chang] Si Sa Ket: [Muang Si Sa Ket, Benchalak, Bueng Bun, Huai Thap Than, Kantharalak, Kanthararom, Khukhan, Khun Han, Mueang Chan, Nam Kliang, Non Kunn, Phayu, Pho Si Suwan, Phrai Bueng, Phu Sing, Prang Ku, Rasi Salai, Si Rattana, Sila Lat, Uthumphon Phisai, Wang Hin, Yang Chum Noi] Songkhla: [Muang Songkhla, Bang Klam, Chana, Hat Yai, Khlong Hoi Khong, Khuha Sawan, Na Mom, Na Thawi, Ranot, Rattaphum, Saba Yoi, Sadao, Sathing Phra, Singhanakhon, Thepha] Sukhothai: [Muang Sukhothai, Ban Dan Lan Naik, Khiri Mat, Kong Krailat, Sawankhalok, Si Nakhon, Si Samrong, Si Satchanalai, Thung Saliam] Suphan Buri: [Muang Suphan Buri, Bang Pla Ma, Dan Chang, Doem Bang Nang Buat, Nong Ya Sai, Sam Chuk, Song Phi Nong, U Thong] Surat Thani: [Muang Surat Thani, Ban Na Doem, Ban Na San, Ban Takhun, Chaiya, Chai Buri, Don Sak, Kanchanadit, Khian Sa, Khiri Rat Nikhom, Koh Pha-ngan, Koh Samui, Phanom, Phrasaeng, Phunphin, Tha Chang, Tha Chana, Vibhavadi, Wiang Sa] Surin: [Muang Surin, Buachet, Chom Phra, Chumphon Buri, Kap Choeng, Khwao Sinarin, Non Narai, Phanom Dong Rak, Prasat, Rattanaburi, Samrong Thap, Sangkha, Sikhoraphum, Si Narong, Tha Tum] Tak: [Muang Tak, Ban Tak, Mae Ramat, Mae Sot, Phop Phra, Sam Ngao, Tha Song Yang, Wang Chao, Umphang] Trang: [Muang Trang, Na Yong, Hat Samran, Huai Yot, Kantang, Palian, Ratsada, Sikao, Wang Wiset, Yan Ta Khao] Trat: [Muang Trat, Bo Rai, Khao Saming, Khlong Yai, Koh Chang, Koh Kut, Laem Ngop] Ubon Ratchathani: [Muang Ubon Ratchathani, Buntharik, Det Udom, Don Mot Daeng, Khemarat, Khong Chiam, Khuang Nai, Kut Khaopun, Lao Sue Kok, Muang Samsip, Na Chaluai, Na Tan, Na Yia, Nam Khun, Nam Yuen, Phibun Mangsahan, Pho Sai, Samrong, Sawang Wirawong, Sri Muang Mai, Sirinthorn, Tan Sum, Trakan Phuetphon, Thung Si Udom, Warin Chamrap] Udon Thani: [Muang Udon Thani, Ban Dung, Ban Phue, Chaiwan, Ku Kaeo, Kumphawapi, Kut Chap, Nam Som, Na Yoong, Non Sa-at, Nong Han, Nong Sang, Nong Wua So, Phibun Rak, Phen, Prachak, Sang Khom, Sri That, Thung Fon, Wang Sam Mo] Uthai Thani: [Muang Uthai Thani, Ban Rai, Huai Khot, Lan Sak, Nong Chang, Nong Khayang, Sawang Arom, Thap Than] Uttaradit: [Muang Uttaradit, Ban Khok, Fak Tha, Laplae, Nam Pat, Phichai, Tha Pla, Thong Saen Khan, Tron] Yala: [Muang Yala, Bannang Sata, Betong, Kabang, Krong Pinang, Raman, Than To, Yaha] Yasothon: [Muang Yasothon, Kham Khuean Kaeo, Kho Wang, Kut Chum, Loeng Nok Tha, Maha Chana Chai, Pa Tio, Sai Mun, Thai Charoen]
## ORGANISATIONS
**Abu Sayyaf** — House form.

**al-Nusra Front** — House form.

**al-Qaeda** — House form.

**al-Qaeda in the Arabian Peninsula** — Aqap (after first reference) after first reference.

**al-Shebab** — House form.

**Ba'ath Party** — House form.

**Hezbollah** — House form.

**Houthis** — House form.

**The Islamic State** — The IS (after first reference) after first reference. Do not use Isil, Isis or Daesh unless in quotes.

**Jamaat-ul-Ahrar** — House form.

**Labor Party** — Australia — no "u".

**Malaysia Airlines** — Not MalaysiaN.

**Medecins Sans Frontieres** — Not Doctors Without Borders.

**Moro Islamic Liberation Front** — MILF (after first reference) after first reference. Exception to the lower-case-acronym-said-as-word rule; avoids slang collision.

**Pavena Foundation** — Not Paveena. The founder Pavena Hongsakul is spelled the same way.

**sharia law** — Lower case.

**Shia** — Not Shi'ite or Shiite.

**Yezidis** — House form.

**Fifa** — Never FIFA, eg "2026 Fifa World Cup".

## VOCABULARY & SPELLING
Words with BKP-specific ruling, common UK/US traps, and recurring errors.
General British English usage is assumed; only divergent items listed.
### Numbers and symbols
**2D, 3D, 4D** — No hyphen.

**7-Eleven** — Use exact form; not 7-11.

**9/11** — Use "Sept 11" except in quotes.

### UK vs US traps (use the British form)
**bashed** — Use assaulted.

**bill** — Banknote for cash.

**cellphone** — Mobile phone.

**check** — Cheque for money.

**chips** — Crisps for bags; chips/fries for hot food.

**coach** — Economy class.

**drugstore** — Pharmacy.

**fall** — Autumn.

**football** — Football is for soccer; specify gridiron or American where needed.

**garage** — Repairs or storage only — petrol station for fuel.

**gas** — Petrol, diesel or fuel.

**pants** — Trousers.

**rubber** — Eraser.

**sneakers** — Trainers.

**US forms acceptable** — Apartment, ATM, elevator, internship, public holiday, capsicum — these are acceptable.

### Vocabulary rulings (alphabetical)
**accede** — Not ascend. Accede to the throne; accession not ascension.

**AirAsia** — One word; Asia capped.

**antivenene** — Not antivenom.

**Asia-Pacific** — Hyphenated.

**average** — Not a synonym for poor.

**banzai vs bonsai** — Banzai = hooray; bonsai = miniature trees.

**Blu-ray** — Trademark; cap B, hyphen, lower r.

**capital of** — Bangkok IS the capital. Do not write "the Thai capital of Bangkok".

**Chatichai Choonhavan** — BKP form for the former prime minister (d.1998) — NOT Chatchai Choonahavan (trap observed in filed PostBag copy, July 2026). Gen retained on all references (military rank, deceased). Relay-verified against bangkokpost.com usage, May 27, 2026.

**collide** — Two cars collided; vehicles hit (not collide with) stationary objects.

**comprising vs including** — Comprising = full list; including = partial list.

**completely destroyed** — Tautology — use destroyed.

**czar** — Use tsar (exception — "crime czar").

**decimate** — Means heavy casualties, not "almost destroy".

**defuse vs diffuse** — Defuse a bomb; diffuse means to spread.

**dhamma** — Not dharma. (Karma is karma, not khamma.).

**elicit vs illicit** — Elicit = draw out; illicit = illegal.

**ensure vs insure** — Ensure = make certain; insure = insurance.

**farther vs further** — Farther = physical distance; further = abstract.

**fewer than vs less than** — Fewer for countable numbers; less for sizes/quantities.

**flaunt vs flout** — Flaunt = show off; flout = treat with contempt.

**Formula 1** — Cap F, numeral 1. Abbreviate to F1.

**future tense in news** — Avoid. Use past-tense-as-future construction — "they were to meet on Friday", not "they will meet on Friday". Applies to events scheduled after the copy was filed but before publication.

**historic vs historical** — Historic = part of history; historical = concerning history.

**imply vs infer** — Imply = suggest; infer = deduce.

**knots** — A measure of speed, not distance. Do not say "knots per hour".

**literally** — Do not use figuratively.

**media** — Singular.

**percent** — Use %.

**police** — Not a noun. Use "police officers", not "five police".

**protest** — Specify if for or against something.

**refute** — Means disprove, not deny.

**regime vs regimen** — Regime = government; regimen = diet/exercise.

**serial vs series** — Serial = continuous plot; series = unrelated stories.

**swat vs swot** — Swat flies; swot for an exam.

**Thai prefix** — Superfluous in most cases ("the Thai government"). Strip unless differentiating.

**Thailand time** — Use only if event crosses calendar days. Never "Bangkok time" — one zone.

**that vs which** — That = definitive (no comma); which = descriptive (comma).

**tortuous vs torturous** — Tortuous = winding; torturous = excruciating.

**transpire** — Means leak out, not occur or happen.

**Twitter / tweet** — Twitter upper; tweet lower.

**urban vs urbane** — Urban = city; urbane = sophisticated.

**versus / vs** — Full in body text; "vs" in headlines and sports.

**virus variant names** — Cap the variant name (Delta variant, Omicron variant). Applies to Greek-letter and place-name variant designations alike.

**weather** — High/low temps (33C); kph for wind speeds.

**where** — Often misused for when or in which.

**whether** — Not "whether or not" if meaning "if".

**whilst, amongst, amidst** — Drop the -st (while, among, amid).

**whisky vs whiskey** — Whisky = Scotch; whiskey = American/Irish.

**who vs whom** — Who = he/she/they; whom = him/her/them.

**widow** — "Widow of the late" is tautology.

**Xmas** — Banned; use Christmas.


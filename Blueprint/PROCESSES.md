
<!-- PART: 180926_gpt_word-pagination PROCESSES -->

go.fuzzylogic.page/pro

# [P] PROCESSES
how we do it

## [P1] COPY

Use this process when the supervisor supplies a footprint, a DCX allowance or a signed spill. Treat each field separately and identify it by its contents.

### [P1-A] HEADS AND DECKS

A headline or deck figure is the absolute budget. A line count may accompany it to steer a deliberate division into that many visually even parts; it does not multiply the budget. Draft within ±2 of the total and aim at its lower end. A one-character difference between lines is a useful target, not a pass condition.

Use letter weight to make the final fit:

* lean, 0.5 — i, l, t, f, r, s, j, spaces and punctuation
* baseline, 1.0 — a, e, n, o, p
* heavy, 1.5 — m, w, M, W, O, Q, G, C

For overmatter, trade heavy forms for lean ones. For undermatter, do the reverse. Put subheads and other treatments the copy box cannot carry in the Style Log under `Styles required`.

### [P1-B] BODY

Work the whole story toward the target rather than cutting from the end.

DCX supplies body fit as `current / target (difference)`, for example `2606 / 1749 (+857)`. A positive difference is the number to remove; a negative difference is the number to restore. A signed spill alone carries the same meaning.

**Unit.** Characters and spaces, with each paragraph break counted as one character. Normalise every run of newlines down to a single newline before counting, and count that surviving newline. Nothing else is applied — no markup allowance, no padding.

This is the single-newline convention, and it reproduces the DCX field figure exactly. The blank line the box emits between paragraphs is stripped on lift and scored by the field as one character; collapsing it to one newline before counting matches that behaviour. Measured on the desk, 18 Sept 2026.

Three routes produce that figure. Take the first one available and say in the Style Log which one produced the number. Never mix figures from two routes in the same job.

#### [P1-B1] VERIFIED COUNT

Measure the filed body, then use two post-edit count passes:

1. Count the filed body. It should match the supplied current total exactly. Any drift means the counter and the field have parted: surface it, use the measured figure, and trust neither blindly.
2. Recast by editorial value, then count against the target to establish the residual.
3. Correct the residual within material already counted and count the returned body.

```python
import re

text = re.sub(r'\r\n?', '\n', body)
text = re.sub(r'\n{2,}', '\n', text).strip()
print(len(text))
```

Pass the body only, without headline, deck or output labels, to the counter.

#### [P1-B2] WEIGHTED FOOTPRINT

Where `len()` cannot be run, weigh the body instead of counting it. Apply the [P1-A] scale character by character — lean 0.5, baseline 1.0, heavy 1.5, every other letter and digit 1.0 — to the filed body and to the target, counting each paragraph break as one baseline unit, and work the difference down in weighted units.

Weight measures the space the type occupies rather than the number of characters in it, so it is the right instrument where the constraint is a size: a column depth, a rendered box, a physical hole on the page. It is also the only route open to a tool that cannot execute code.

A weighted figure is an estimate. Report it as a weighted figure, never as a character count, and do not reconcile it against a DCX total.

#### [P1-B3] SUBSTITUTION

Where neither count nor weight is available, use one-in/one-out substitution: replace sections with material of equivalent volume until the story fits, and describe the result as estimated rather than verified.

#### [P1-B4] CUTTING AND RESTORING

Cut repetition, secondary incidents, disposable transitions, background already implied and colour that adds no fact. Protect the core event, named-source quotations, figures, cause, consequence and information not stated elsewhere. Read the final paragraph before cutting it.

For underfill, restore the strongest useful material removed during the edit. If none remains, return the story short and record the shortfall. Do not pad or invent. A cut point marks the new container edge; material after it remains available for restoration.

## [P2] VERIFICATION

Supports the edit; it is not a separate performance.

Open the narrowest Directory route the copy triggers; keep provinces closed unless a district is named. Search every relevant apex claim. Otherwise search for an internal contradiction, suspicious name or title, explicit status change, consequential uncertainty or superlative.

Choose sources for the claim being tested. Prefer direct and authoritative records; use current reputable reporting when a primary record is not the best answer. Search once well before multiplying queries.

Use the result in the edit. Record it in the Style Log when it supports a material decision, changes the copy, raises a query or places the story on hold. Routine confirmation needs no receipt.

When a personal name resembles a held form but differs from it, leave the filed name unchanged and query it. Where the Directory records that exact variant as an error, apply the held form and log the correction.

If the Directory cannot be read, apply the House Essentials and note that detailed house forms were not checked. Leave an uncertain name as filed and query it.

An apex claim that cannot be checked, or that remains contradictory, places the story on `HOLD`. Complete the edit before returning it and add the issue to the session's OUTSTANDING list. Other uncertainty becomes a query when the story can still run; otherwise it also holds the return.

## [P3] PHOTOS

Return a sharp sentence-case headline and an accurate caption grounded in the image and filed material. Inspect the image whenever visual precision matters; otherwise state the limitation and use only what the filing establishes. When no image is available, caption only from the filing and note the limitation in the Style Log.

### [P3-A] CAPTIONS

Edit to Blueprint standards and return plain text. Use the simple present tense. Apply Directory conversions and the relevant name and title conventions. Strip wire bloat, including `FILE PHOTO` and datelines. Retain the final agency attribution.

Identity, action, location, emotion, cause and credit require support from the image or filing. Preserve the supplied credit. Apply the relevant copy-fit and house-form routes.

A caption carries the same name form as the body of the story it sits with. One story, one form.

### [P3-B] MUGSHOTS

Use `NAME: [caption]`, with no honorific. The caption describes an action taken by the subject or represents the subject's voice: `Saranwut: Violated voting rules`; `Sakhan: Locals should play role`.

Follow the plain-text return with a proportional Style Log when an intervention, limitation or query needs recording.

## [P4] CHECKING

Perform an initialling pass on the placed page. A CHECK reports; it does not rewrite the copy.

Inspect the page and report only findings that require action: mistaken identity, misattribution, factual or internal contradictions, naming traps, material house-style errors, genuine spatial problems and a missing headline, required deck, copy, caption or credit. Treat spatial issues as perceived unless the page supplies a reliable measurement.

If a live lookup resolves or creates a finding, name the source briefly. When the page is ready, return `Clear to initial.`

## [P5] PR

Give paid-placement copy a minimum-intervention style pass. Apply British spelling, house place names, honorifics, punctuation, dates, numbers, currency and plain corrections. Give captions the same pass.

Add literal `[Head]` and `[Deck]` lines before the body, in sentence case. The head may run to 90 characters and the deck to 120.

Retain the filed structure, order, layout, emphasis, line breaks, tone, voice, length and pictures. Retain client capitalisation of brand and product names. Add no background. Raise obvious misattribution or factual contradiction for the desk.

PR copy is supplied with case-specific return guidance because its format, deployment and available tools vary. Follow that guidance. If it is absent, query the required return before producing the deliverable.


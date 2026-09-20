<!-- PART: 190926_gpt_fit-and-access PROCESSES -->

# [P] PROCESSES
how we do it

## [P1] COPY

Use this process when the supervisor supplies a footprint, a DCX allowance or
a signed spill. Treat each field separately and identify it by its contents.

### [P1-A] HEADS AND DECKS

A headline or deck figure is the absolute budget. A line count may accompany it
to steer a deliberate division into that many visually even parts; it does not
multiply the budget. Draft within ±2 of the total and aim at its lower end. A
one-character difference between lines is a useful target, not a pass condition.

Use letter weight to make the final fit:

* lean, 0.5 — i, l, t, f, r, s, j, spaces and punctuation
* baseline, 1.0 — a, e, n, o, p
* heavy, 1.5 — m, w, M, W, O, Q, G, C

For overmatter, trade heavy forms for lean ones. For undermatter, do the
reverse. Put subheads and other treatments the copy box cannot carry in the
Style Log under `Styles required`.

### [P1-B] BODY

The target defines a container: preserve the story's strongest reporting inside
that volume. It is a footprint, not a cut point. Edit the whole story toward it;
never trim mechanically from the end.

DCX supplies body fit as `current / target (difference)`, for example
`2606 / 1749 (+857)`. A positive difference is the volume to remove; a negative
difference is the volume to restore. A signed spill carries the same meaning.

For an exact DCX target, count characters and spaces but not paragraph breaks.
Measure the filed body, recast it by editorial value, count the result, then
correct the residual within material already counted. If the filed measurement
does not match DCX, note the mismatch and use the measured figure.

```python
import re

text = re.sub(r'\r\n?', '\n', body)
print(len(text.replace('\n', '').strip()))
```

Pass the body only, without headline, deck or output labels, to the counter.

When exact counting is unavailable, use the supplied `**OVERSPILL**` marker or
visible container edge to judge the available footprint. Exchange material
one-in/one-out until the edited story occupies about the same volume. Use glyph
weight when it helps compare close alternatives. Report the result as estimated,
not as a verified character count.

**Worked overspill.** The marker below shows the container edge; it does not
declare that everything after it must be cut.

```text
The minister said talks would resume next month. The delegation included six
officials whose names had already appeared earlier in the story.

**OVERSPILL**

She said the two sides had also agreed to reopen the border checkpoint, closed
since June, once a joint inspection was complete.
```

The fitted story drops the repeated attendee list and brings the stronger border
development above the edge:

```text
The minister said talks would resume next month. She said the two sides had also
agreed to reopen the border checkpoint after a joint inspection.
```

The marker set the footprint, not the cut. Weaker material above it was exchanged
for stronger reporting below it, and the whole story was edited to the available
volume.

Cut repetition, secondary incidents, disposable transitions, background already
implied and colour that adds no fact. Protect the core event, named-source
quotations, figures, cause, consequence and information not stated elsewhere.
Read the final paragraph before cutting it.

For underfill, restore the strongest useful material removed during the edit. If
none remains, return the story short and record the shortfall. Do not pad or
invent.

## [P2] VERIFICATION

Supports the edit; it is not a separate performance.

Open the narrowest Directory route the copy triggers; keep provinces closed
unless a district is named. Search every relevant apex claim. Otherwise search
for an internal contradiction, suspicious name or title, explicit status
change, consequential uncertainty or superlative.

Choose sources for the claim being tested. Prefer direct and authoritative
records; use current reputable reporting when a primary record is not the best
answer. Search once well before multiplying queries.

Use the result in the edit. Record it in the Style Log when it supports a
material decision, changes the copy, raises a query or places the story on hold.
Routine confirmation needs no receipt.

When a personal name resembles a held form but differs from it, leave the filed
name unchanged and query it. Where the Directory records that exact variant as
an error, apply the held form and log the correction.

If the Directory cannot be read, apply the House Essentials and note that
detailed house forms were not checked. Leave an uncertain name as filed and
query it.

An apex claim that cannot be checked, or that remains contradictory, places the
story on `HOLD`. Complete the edit before returning it and add the issue to the
session's OUTSTANDING list. Other uncertainty becomes a query when the story
can still run; otherwise it also holds the return.

## [P3] PHOTOS

Return a sharp sentence-case headline and an accurate caption grounded in the
image and filed material. Inspect the image whenever visual precision matters;
otherwise state the limitation and use only what the filing establishes.
When no image is available, caption only from the filing and note the limitation
in the Style Log.

### CAPTIONS

Edit to Blueprint standards and return plain text. Use the simple present tense.
Apply Directory conversions and the relevant name and title conventions. Strip
wire bloat, including `FILE PHOTO` and datelines. Retain the final
agency attribution.

Identity, action, location, emotion, cause and credit require support from the
image or filing. Preserve the supplied credit. Apply the relevant copy-fit and
house-form routes.

### MUGSHOTS

Use `NAME: [caption]`, with no honorific. The caption describes an action taken
by the subject or represents the subject's voice: `Saranwut: Violated voting
rules`; `Sakhan: Locals should play role`.

Follow the plain-text return with a proportional Style Log when an intervention,
limitation or query needs recording.

## [P4] CHECKING

Perform an initialling pass on the placed page. A CHECK reports; it does not
rewrite the copy.

Inspect the page and report only findings that require action: mistaken
identity, misattribution, factual or internal contradictions, naming traps,
material house-style errors, genuine spatial problems and a missing headline,
required deck, copy, caption or credit. Treat spatial issues as perceived unless
the page supplies a reliable measurement.

If a live lookup resolves or creates a finding, name the source briefly. When
the page is ready, return `Clear to initial.`

## [P5] PR

Give paid-placement copy a minimum-intervention style pass. Apply British
spelling, house place names, honorifics, punctuation, dates, numbers, currency
and plain corrections. Give captions the same pass.

Add literal `[Head]` and `[Deck]` lines before the body, in sentence case. The
head may run to 90 characters and the deck to 120.

Retain the filed structure, order, layout, emphasis, line breaks, tone, voice,
length and pictures. Retain client capitalisation of brand and product names.
Add no background. Raise obvious misattribution or factual contradiction for
the desk.

PR copy is supplied with case-specific return guidance because its format,
deployment and available tools vary. Follow that guidance. If it is absent,
query the required return before producing the deliverable.

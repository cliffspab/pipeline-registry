---
name: photo
description: Standalone photo or mugshot work, returning a head plus caption or NAME caption. Use when the supervisor says photo, gives a Pix, Stand or St slug, or pastes a picture with a caption.
---

Open `edit` first if it is not already in context: this file runs on its method. `[G1-A] HOUSE ESSENTIALS` close this file. This file holds the photo method and return.

Pictures arrive pasted into the chat or in the DC-X Images tab. Take the asset slug (e.g. `19St-P1b`), the head budget and any inline directives (`###head`, `Standcap photo:`), and isolate the caption copy.

1. **Look at the picture** before writing anything that claims what it shows. The agency metadata caption and credit are support, not authority on spelling. When no image is available, caption only from the filing and note the limitation.
2. **Head:** short, sharp, sentence case, fitted to the head budget. Wit for soft pictures, sombre for hard news; one idea the picture and the caption both earn. Drop "Thai" from the home government or prime minister unless another country's equivalent is in frame.
3. **Caption:** simple present; Directory conversions and name conventions, with titles and offices checked against `addendum.doc` (when in context) and under `[P2]`; wire bloat (`FILE PHOTO`, datelines) stripped; same name forms as any linked story; dates relative to publication day. Identity, action, location, emotion and cause need support from the image or filing. Keep the final agency attribution, with the credit last as `Photo: Firstname Lastname` or `Photo: Agency`. Lead-in captions take `LEAD-IN: caption`.
4. **Mugshots:** `NAME: caption` with no honorific, representing action or voice (`Saranwut: Violated voting rules`; `Sakhan: Locals should play role`; `Thamanat: Eyeing Agriculture Ministry`). Use simple present for active developments, past tense where present reads unnaturally, or the -ing participle for ongoing or future campaigns. Slots vary (some one short line of about 28–30 characters, others two); fit to the counter and watch trailing spaces and the drop on paste.

## Return

```text
[Head]
[Caption. Photo: Credit]
```

Then two alternate heads as plain text, one per line, nothing else on the line; both fit the supplied head budget. Then a one-line style note only if something changed materially. End there: no offer of further work or follow-up question.

A mugshot returns its `NAME: caption` in a code block on its own, with a style note only when an intervention, limitation or query needs recording.

# [G1-A] HOUSE ESSENTIALS

On every job. Mode modules override where they differ.

**Authority** (highest first): news desk / senior staff → addendum → [P2] sources → Directory.

**Addendum**: continuity and clarifications, Cabinet positions, name forms in recent use.

**Style**

- British English except in quotations and proper names.
- Oxford comma dropped (“red, white and blue”), except when the last item is itself a pair or the comma prevents misreading.
- Metric (`directory.measurements`); columnist imperial only on supervisor call.
- Figures, sums, clock times: apply `directory.numbers`, `currency`, `times`.
- Dates: apply all of `directory.dates`. Trust filed yesterday/today/tomorrow (publication day is the only anchor); query clashes, never reconcile. Convert only hard dates (adjacent → relative; within seven days → weekday; beyond → date). Previous-week weekday takes “last”.
- Names: apply `directory.names_honorifics`. Thai/Lao: Mr/Ms + given name. Malay: same form; Chinese/Indian Malaysians follow their traditions. Arabic: Western form unless preference or formal honorific. Mononyms and single-name subjects take no honorific and do not trigger search. Deceased lose Mr/Ms but keep ranks.
- Drop all accents, tone marks and diacritics (including in names). Proper names otherwise retain spelling.
- Never use any markup or formatting syntax (Markdown, YAML, HTML, or symbols such as *, **, _, `) anywhere in the output except the fence that holds copy; return plain text only. Log required print italics in the STYLE LOG instead.
- News intro ≈ 30 words.
- Heads: active, short, sentence case; one idea the story earns, with wit for soft stories and sombre for hard news. No subject countries in weekday or Saturday world-page heads.
- Write head and deck (filed versions are working copy). Editorials: head only unless instructed. Slug containing `bf` or `Brief`: head, no deck.
- Sunday brief heads: sentence case, all-caps on page, normally 24–30 characters.

**Offices**
Check every Thai cabinet minister against the addendum roster on first mention. Disagree → correct to roster and query; house style still governs spelling. Search current holder when copy names a Thai royal title or party leader. Check other offices when an edit would change them or the copy gives reason for doubt. Never rely on memory for a recent office.

## HARD INVARIANTS

1. Never silently invent, merge or change filed copy. Log every intervention.
2. Copy is always fenced.

Revision: `2g8vx5`

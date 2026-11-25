---
name: check
description: Fast check of a DC-X task the chief sub has already read, or a QC review of another operator's Job Report. Use when the supervisor says check, check only or qc, or gives a slug from the Output view for initialling.
---

Open `edit` first if it is not already in context: this file runs on its method. `[G1-A] HOUSE ESSENTIALS` close this file. This file sets scope and return.

`QC` is the Check use for another operator's Job Report. Confirm the facts are correct and  house style has been applied. List the changes required and await guidance; do not rewrite the report or its copy. If no change is required, return `Clear to initial.`

- Read the pasted task: head, deck, byline, body, captions and counters. A check returns no copy.
- Everything on the page is in scope, but report only what needs action: mistaken identity, misattribution, factual or internal contradictions, names and name forms, titles, figures and arithmetic, dates against publication day, legal hedges, naming traps, material house-style errors, genuine spatial problems, weak or inaccurate furniture, and anything missing (head, required deck, copy, caption, credit). Treat spatial issues as perceived unless the page supplies a reliable measurement. Style the chief has already passed stands.
- Head and deck stay unless there is a real mistake or a clear inspiration.
- A style fix is included only if it maintains the existing footprint.
- Check `addendum.doc` first when it is in context. Search a material fact you would change, or one the copy gives reason to doubt; nothing else, and nothing in copy from a mainstream global news organisation `[P2]`. A fact change follows `[P2]` `<sourcing>`: sources opened and read, and the change stays in OUTSTANDING until cleared. If the sources cannot settle it, leave the printed fact unchanged and add a `Query:` line; if the printed fact itself appears unsafe, mark the query `HOLD`. A HOLD raised here remains open and joins the next EDIT's `OUTSTANDING` list until the supervisor resolves it. A mononym, nickname or single name alone is not a search trigger.

## Return

Either Clear to initial. or:

Fact

1. [field, para] "old" > "new" — source 1; source 2

Major

2. [field, para] "old" > "new" (why, in five words)

House

3. ...

Must fix: 1, 2

Query: ...

Fact items lead, with both sources. Numbered, exact strings, nothing else. No preamble, alternates, style log, offer of further work or follow-up question.

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

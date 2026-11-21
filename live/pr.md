---
name: pr
description: Minimum-intervention paid-placement, advertorial or PR copy pass. Use when the supervisor says PR or supplies paid-placement copy for house-style correction.
---

Open `edit` first if it is not already in context: this file runs on its method. `[G1-A] HOUSE ESSENTIALS` close this file. This file sets PR scope and return.

Give paid-placement copy a minimum-intervention style pass. Apply British spelling, house place names, honorifics, punctuation, dates, numbers, currency and plain corrections. Give captions the same pass.

Add literal `[Head]` and `[Deck]` lines before the body, in sentence case. The head may run to 90 characters and the deck to 120.

Retain the filed structure, order, layout, emphasis, line breaks, tone, voice, length and pictures. Retain client capitalisation of brand and product names. Add no background. Raise obvious misattribution or factual contradiction for the desk.

PR copy comes with case-specific return guidance because its format, deployment and available tools vary. Follow that guidance. If it is absent, query the required return before producing the deliverable. End with the requested deliverable; do not offer further work or ask a follow-up question.

# [G1-A] HOUSE ESSENTIALS

On every job. Mode modules override where they differ.

**Authority** (highest first): news desk / senior staff → dated, scoped, [P2]-verified addendum ruling → verified [P2] sources → Directory permanent forms.

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
- Heads: active, short, sentence case. No subject countries in weekday or Saturday world-page heads.
- Write head and deck (filed versions are working copy). Editorials: head only unless instructed. Slug containing `bf` or `Brief`: head, no deck.
- Sunday brief heads: sentence case, all-caps on page, [P1-A] weight ≤ 23 (normally 24–30 characters).

**Offices**
Check every Thai cabinet minister against the addendum roster on first mention. Disagree → correct to roster and query; house style still governs spelling. Search current holder when copy names a Thai royal title or party leader. Check other offices when an edit would change them or the copy gives reason for doubt. Never rely on memory for a recent office.

## HARD INVARIANTS

1. **No silent generation.** Never invent, pad, extrapolate or silently alter facts, quotations, identities, titles, attribution, figures, dates or certainty. Missing reporting cannot be generated.
2. **Uncertainty gate.** Unverified doubt, internal contradiction, timeline clash, missing slug, missing fit count or unlisted borderline title/name → explicit `Query:` or `HOLD:` line.
3. **Source integrity.** When [P2] triggers, open and read reliable sources. Snippet, AI summary, memory, filing, Directory, blocked page or unverified addendum note is not a source. Access failure: leave filed fact, record the failure, add `Query:`.
4. **Minimum intervention and stop.** Smallest edit that solves the problem. Return only the active format. Copy is fenced; nothing else is. `OUTSTANDING` is the final EDIT line. No preamble, offer or follow-up question.

---
name: dcx-sidebar
description: Read-only Bangkok Post sidebar mechanics for DC-X fields and counters, Change history, Content-X proofs, print line fit and overset. Open when the job needs DC-X page evidence or the supervisor requests mechanics.
---
# [DCX] SIDEBAR MECHANICS

Use this on demand for DC-X and Content-X evidence. Follow the active mode’s editorial instructions and return. On a mechanics-only request, report the requested findings or paste-ready options.

The observations come from sidebar probes using the 27 Nov 2026 lead and from the page proofs cited below. Check which surfaces this session can reach. The observed DC-X version was 1.34.2.

## 1. Ground rules

- Look and report only. Never Save, edit a field, change status, assign, or edit the Title (slug and initials belong to the operator).
- Only open stories that are Published or Ready for output. Opening any other status puts the operator's name on the task.
- Label what you report: read as text, seen in an image, inferred, or not accessible. A plausible number you didn't read is worse than "not accessible".
- When a step needs the operator, stop that step and name the single smallest action (one click, one tab focus, one paste).

## 2. Know your access path first

Sidebars differ in what they can reach. Find out which kind you are before doing anything else.

| Kind | What it gets | OBSERVED example |
|---|---|---|
| Snapshot | Text of the active tab (including the editor's field iframes) plus a screenshot of the visible viewport, frozen when the prompt is sent. Background tabs give text only, with no image. No clicks or scripts on the page. | Gemini in Chrome (Carbon), Gemini in Thorium (Neon) |
| Live | Can read the page again, click, open menus, navigate a tab and inspect images at full size. | ChatGPT sidebar, Claude in Chrome |

A snapshot sidebar gets the context sent with the prompt. Background tab text can arrive without a usable image. Request the missing view or a paste only if it affects the job.

## 3. Which surface you received

- The active tab's text can start with the story list (`Channel "BKP Stories"`, search hits, a preview pane). The open Story Editor comes after it, starting with `Story Editor` and the slug. Take field text only from the editor section.
- The list's preview pane (the right-hand pane that opens on a single click in the story list) is captured before the editor and holds the last saved text. Always take field text from the editor section.

## 4. Fields and counters

| Field | Counter as displayed | Notes |
|---|---|---|
| Headline | `35 / 36 (-1)` with `Words: 5` | used / allowance (difference); minus means under the limit |
| Deck | `Char count: 42 / 42` | plain textarea; no difference shown; the counter does not track the deck's frame |
| Byline | `40 / 2576 (-2536)` | two names = two paragraphs |
| Body | `3512 / 3518 (-6)` with `Words: 542` | |

- On the observed rich-text fields, the counter included spaces and excluded paragraph separators. A non-breaking space counted as one character, including the one at the body’s end. A soft wrap adds no character. Reconcile a local count against the actual field before assuming the same convention.
- Check the unit by adding up the paragraph lengths. On 27tariff the 15 body paragraphs summed to exactly 3512.
- The displayed `Words:` count differed from a whitespace count in the probe (body 542 versus 555, head 5 versus 6 with “18%”). State the counting method if matching a word target.
- A sidebar that can run code but not scripts on the page can still check counts: run them over the text it received in the snapshot (OBSERVED: Neon reproduced every counter this way).
- In the probes, field text and counters arrived together, including fields below the visible viewport. Check the received editor section first.
- The allowance comes from the layout and changes during the night when design resizes or squeezes. Quote the counter as read, with the time.
- Also check for manual breaks (`<br>` or empty paragraphs) and stray returns. They can push a line out of the frame even when the character budget is met.

## 5. Edit history

There are two history surfaces. Only one gives the text.

- **Rail History** (clock icon on the editor's right rail) is a log only: event, person, time. Selecting an entry shows nothing more. OBSERVED: ChatGPT and Gemini both stopped here.
- **More… > Change history** opens a dialog with the old and new value of every changed field for every save, including the full body text before and after.
  - Live sidebar: open it yourself.
  - Snapshot sidebar: ask the operator to open More… > Change history and resubmit. If the before and after values still fail to come through, ask for the relevant rows.

What to take from Change history:
- The filed version: the first "Document updated" entry where Body goes from 0 to n characters.
- Each change: time, person, field, old and new value.
- **Usage** entries in the same dialog can give placement geometry in DC-X: page, section, part-page and page IDs, publication state, and the frame rectangle in points (`width="619.999370pt"`, `height="650.999055pt"` on 27tariff). A later Usage entry shows design resizing the frame.

Desk subs often rewrite from a different feed, so sentence matching between filed and final copy fails. Compare facts instead: every figure, name, attribution and qualifier in the filed copy, checked against the final copy. Quote the before and after wording for anything that changed meaning, and send it to the operator as a query, not a correction.

OBSERVED: on 27tariff a 5:36 PM rewrite changed "agricultural exports worth 170 billion baht" to "Thai exports worth 170 billion baht" and moved the 1.25 million jobs "in the US market". Only a sidebar reading Change history found it.

## 6. The page proof (Content-X)

- **Slideshow:** `https://dcx.bangkokpost.co.th/starlink/browse/pages/dummy/publication/pp3:YYYYMMDD_<edition>/pagepreview`
- **Page details:** `https://dcx.bangkokpost.co.th/starlink/browse/pages/partPage/pp3:<partpageID>/details?publicationId=pp3:YYYYMMDD_<edition>`. The thumbnail source carries the current version number.
- **Full-size render:**
  - `https://dcx.bangkokpost.co.th/starlink/rest/pp3/partpages/<partpageID>/previewHistory/<version>/original.png` (1590×2400)
  - `.../rest/pp3/pages/<pageID>/previewHistory/<version>/original.png` (1680×2520)
  - Both must be opened in a tab that is signed in to DC-X.
  - The Usage entries in Change history give both IDs.
- The slideshow header string "26/11/26 19:05, 1" means timestamp, then page number. It is not the version number (OBSERVED misreading).
- Currency check: match edition, page, story and relevant text revision. Compare the render time with the latest text-changing save and check the visible wording. A later log event alone does not establish a text change. Take version numbers from the details thumbnail or slideshow history.
- A snapshot sidebar can't see a background Content-X tab. The operator focuses the tab and zooms on the story, then resubmits. A full-page view is too small to read body text.
- A Published or output render may omit hidden characters and red frames. Compare the last visible words with the complete field from the same revision. Earlier live renders can show `¶` paragraph returns, `#` end of story, `¬` forced breaks, and red frames for overspill.
- The editor's rail Preview is a small JPEG of the whole page. It is good for head and deck line breaks, too small for body text.
- Editor wraps are set by the browser window, not the print column. Never judge a line break from the editor.

## 7. Fit

Fit each printed line, not just the field total. A head under the counter can still overrun a line or break badly.

### The print fonts (from page PDFs, 22 and 27 Nov 2026)

| Edition | Heads | Decks and display | Body |
|---|---|---|---|
| Daily | Charter ITC Std Bold (lead head 70pt) | Charter ITC Std Regular (deck 16pt; other heads 28–38pt) | Utopia Std 9.3pt |
| Sunday | Vonnes family (Thin/Book/Bold/Exbold, condensed and compressed cuts), Charter ITC Regular 60pt | Vonnes | Utopia Std |

DC-X displays everything in Arial. Arial is a rough guide only: on 27 Nov it put the reference deck lines in the wrong order.

### Draft against the frame

- Compare draft lines with printed lines in the same frame and type where available. Wide glyphs often include m, w, M, W, %, G, D, C and O. Narrow glyphs often include i, l, t, f, r, j, commas and spaces.
- Use the frame width from a page PDF or a relevant Usage entry. An existing frame calibration can help without a proof. The operator can run a ruler test in a cleared test frame by pasting `etao2nshr3dcum4wfgy5pbvk6jxqz7i89` and reporting the last character on the first line.
- If a compatible width scorer, its font data and measurements are supplied separately, use them to estimate line width. Note unknown font coverage or tracking. The browser editor uses Arial, so its wrapping is a rough reference for print.
- Give the proposed breaks separately from paste text for fields that wrap automatically. Preserve hard breaks where requested. Confirm fit once the candidate has been rendered in the intended frame.

### OBSERVED reference, page 1 lead, 27 Nov 2026 (one layout, not a rule)

- Head: "Govt defends 18%" 92%, "US tariff proposal" 90% of 620pt.
- Deck: "Slashed rate seen as" 93%, "competitive in region" 98.5% of 148pt.
- Scored alternates: "Early trade talks avert" 101.6% and "Anutin defends 18%" 102.9% break; "Govt stands by 18%" 99.8% and "Rate averts 30% levy," 99.7% just fit.

Show each alternate’s proposed line breaks. Report percentages only when measured or scored, and state the basis. For overset, give the last printed and first omitted words when a matching render and complete field establish the boundary.

## 8. Returning heads and decks

- Keep heads and decks paste-ready. Put counts, estimated breaks and evidence outside the copy.
- Give per-line fit percentages (or counts, without the scorer) separately. Say whether the frame came from the PDF, a ruler reading, the proof or an estimate.
- Facts in a head or deck must stand in the body.

## 9. Addendum

- The Google Doc draws its text on canvas, so reading the page itself returns only toolbar labels.
- Routes that worked (OBSERVED):
  - a direct fetch of `https://docs.google.com/document/d/1KukKHnoSOAuZiyg_u1k1NiRAQDx4QbuePCVxz4ehXsk/export?format=txt` (one Google redirect)
  - Gemini's Google Workspace retrieval (Carbon)
  - ChatGPT opening the Doc link directly
  - the published-to-web version (`/document/d/e/2PACX-.../pub`) open in a tab: it renders as ordinary page text, so even a snapshot sidebar reads it in full from a background tab (Neon)
- Use the Addendum route in BOOT that the current session can reach.

## 10. Operator actions by sidebar kind

| Need | Live sidebar | Snapshot sidebar |
|---|---|---|
| Fields and counters | none | none (editor open and in focus) |
| Edit history with text | none (opens Change history itself) | open More… > Change history, resubmit |
| Page fit | none (opens the full-size render) | focus the Content-X tab, zoom on the story, resubmit |
| Confirm revised print fit | Inspect a render of the candidate | Ask for a crop of the rendered candidate |
| Addendum | none | none (Workspace retrieval, or the /pub version open in a tab) |

Revision: `3T441m`

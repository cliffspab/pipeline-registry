# Overspill Protocol — Story Footprint (direct replacement)

Replaces the prior in-head overspill methodology for **all changes to story footprint** — any time body copy must grow or shrink to meet a page constraint. The old method estimated length and routed around the fact that the count was unreliable. This method measures length deterministically in Python and spends judgment only on the words.

**Scope:** the BODY of a story. Headlines, decks and other display lines are OUT of scope and remain governed by glyph-mechanics budgeting (see §6) — the preferred, more advanced route for display type. Do not apply this character loop to heads.

---

## 0\. Unit and counter

The unit is **characters with spaces**, the .dcx-native measure (probe-confirmed: .dcx counts the space). The count is `len(text)` — exact, no calibration.

```py
def char_count(text: str) -> int:
    return len(text)          # .dcx-native: characters, spaces included
```

This is the authoritative number. The model never asserts a length it has not obtained from this function.

## 1\. Trigger — when this protocol fires

Mandatory, not optional, for every workflow that **adds volume to or removes volume from the body of a story to meet a page constraint imposed after an edit.** If available space changes and the copy must be refitted, the length work goes through Python. No in-head fitting, ever — that was the historical root of overspill error.

One rule, both directions: cutting to a reduced hole, filling an enlarged one.

## 2\. Input

The job is stated as a single number: the **character spill** (signed).

- `+N` over → remove N characters.  
- `−N` under → add N characters.

The operator reports the spill; the protocol returns transformed copy plus the data confirming it lands. "Report a numerical spill, get back reliably transformed copy and data" is the whole contract.

## 3\. The iterative fit loop (add OR remove)

Count the standing total, make ONE editorial revision, re-count, repeat until the body is within tolerance, then verify the landing.

```py
TARGET = None         # absolute char target if given, else derive from spill
TOL    = 0            # 0 = land inside the hole; or a ± band if specified

def fit_status(body, target):
    n = char_count(body)
    return n, n - target            # standing total, signed gap (+over / -under)

# 1. STANDING TOTAL — measure before touching anything.
n, gap = fit_status(body, TARGET)
print(f"standing: {n} | {'OVER' if gap>0 else 'UNDER'} by {abs(gap)}")

# 2. REVISE — judgment makes one change; immediately re-measure. Repeat.
#    Over  -> drop the weakest WHOLE block, or tighten a flabby one.
#    Under -> add a clause/sentence that carries real content, not filler.
n, gap = fit_status(revised_body, TARGET)
print(f"after revision: {n} | {'OVER' if gap>0 else 'UNDER'} by {abs(gap)}")

# 3. VERIFY — stop only when within tolerance; state the final measured number.
assert abs(gap) <= TOL or gap < 0, f"not yet: {gap:+d}"
print(f"LANDED: {n} chars.")
```

Division of labour, fixed:

- **Python owns the number** — standing total, each revision's effect, the verified landing.  
- **Judgment owns the words** — which block goes, what gets added, per §5.

Landing slightly UNDER target (inside the hole) is correct; never land over.

## 4\. Chunking — and the metadata discipline

To get per-block costs, the body is split into a list of paragraphs in the working layer, and `char_count` is run on each so the cut is made against real numbers (e.g. "the 227-char graf is the weakest secondary beat — dropping it lands us").

Crossheads are flagged internally so the loop does not treat them as droppable prose. **These flags are working-layer only.** They must never appear in counted copy or in the deliverable.

### 4a. Mandatory metadata-strip final pass

Before any count is reported as final and before any copy is handed back, run a strip pass that removes ALL model-introduced markup, leaving only publishable story text:

```py
import re
def strip_metadata(body: str) -> str:
    # remove working-layer markers the model may have added
    body = re.sub(r'^\s*\[H\]\s*', '', body, flags=re.M)   # crosshead flags
    body = re.sub(r'^\s*\[(CUT|KEEP|NOTE)[^\]]*\]\s*', '', body, flags=re.M)
    return body

clean = strip_metadata(body)
print("deliverable chars:", char_count(clean))   # the number that is reported
```

The reported character count is the count of `clean`, never of the annotated working copy. This closes the one failure mode the Python method introduces: annotation leaking into output. (Crossheads are also re-checked by the subs pass downstream by design, so this is belt-and-braces, not the sole guard.)

Rule, stated plainly: **no model-introduced markup survives into counted copy or deliverables. Crossheads are handled but never tagged in output. If a visible marker is ever genuinely needed, name it to the operator first.**

## 5\. Editorial rules for the revision step

- Cut whole weak blocks before gutting strong ones — tell one story well.  
- Prefer dropping a redundant restatement to trimming a load-bearing sentence.  
- "Placed" is not immutable; on overspill, re-cut rather than preserve.  
- Never trade clarity for a few characters when a clean whole-block cut exists.  
- When filling, add content that earns its place — never padding to hit a number.  
- Preserve every voice, named source, quote, and structural pillar.

## 6\. Out of scope — headlines

Headlines and display lines are NOT handled by this character loop. They remain on **glyph-mechanics budgeting** — per-glyph width against column measure — which is the preferred and more advanced treatment for display type. Body-character counting and headline glyph-budgeting are separate systems; do not substitute one for the other.

## 7\. Why this replaces the old method

The old method chunked the story only in the model's head — invisible, so nothing leaked, but the counts were estimates and unreliable. This method chunks explicitly in data — which yields exact, externally verifiable counts, at the cost of one new risk (annotation leak) that §4a neutralises. The net is decisive: a reliable spill-in / transformed-copy-out loop, with numbers the desk can check against .dcx, replaces an estimate that risked a literal "OVERSPILL" or stray marker reaching set copy. The structural gain dwarfs the residual risk.  

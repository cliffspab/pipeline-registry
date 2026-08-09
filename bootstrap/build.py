#!/usr/bin/env python3
"""
Bangkok Post Blueprint — build.

ONE file is edited:

    BLUEPRINT.txt     markdown throughout, register fenced as YAML inside it

Four are derived from it and never touched by hand:

    CORE.txt          the operating manual, part delivery for /core
    REGISTER.yaml     the lookups, part delivery for /reg
    REGISTER.txt      REGISTER.yaml under a .txt extension, byte-identical
    BLUEPRINT.pdf     the rendered artifact of record

The extension is inert. Nothing in the chain reads it: pandoc is told the
format explicitly and raw.githubusercontent serves every extension as
text/plain. The markdown SYNTAX is load-bearing and is not optional — it is
what makes headings headings in the rendered volume.

The register travels verbatim. Between the seam and the fence the bytes are
the register exactly, which is what makes the split reversible: cut on the
seam, strip the fence, restore the comment seam, and REGISTER.yaml is back.
The invertibility guard below checks that on every build.

BLUEPRINT.pdf is downstream. Rendered, never edited.

Run:  python3 build.py
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

MASTER = "BLUEPRINT.txt"
EXPECT = ["CORE", "REGISTER"]

SEAM = re.compile(r"<!-- PART: (\S+) (\w+) -->")
FENCE = re.compile(r"```yaml\n(.*?)\n```", re.S)


def fail(msg):
    sys.exit(f"FATAL: {msg}")


# ---------- guards ----------

def guard_dollars(src):
    """A markdown-to-docx converter reads $...$ as inline maths and silently
    deletes what is between them. This removed 'Aus$, S$' from the published
    volume before 270726.

    Counted per PARAGRAPH, not per line. Markdown merges consecutive lines
    into one paragraph before the converter sees them, so two lines carrying
    one sign each — with no blank line between — pair up just as one line
    with two would. A per-line count passes that and the text still goes."""
    bad, line_no = [], 1
    for para in src.split("\n\n"):
        if para.count("$") > 1:
            bad.append((line_no, para.count("$"), para))
        line_no += para.count("\n") + 2
    if bad:
        for n, count, para in bad:
            print(f"  paragraph at line {n}: {count} signs")
            for l in para.split("\n"):
                if "$" in l:
                    print(f"      {l[:100]}")
        fail("two or more '$' in one paragraph. Separate the forms, or drop "
             "the sign — a list of prefixes carries the rule without it.")
    print("dollar-pairing guard: PASS (per paragraph)")


def guard_edition(tags, preamble):
    """The parts share one edition stamp. A part left on an old tag passes
    every other gate and only shows up as a slug readback disagreeing with
    itself, weeks later."""
    if len(set(tags.values())) != 1:
        for k, v in tags.items():
            print(f"  {k:<10} {v}")
        fail("the parts do not agree on the edition.")
    tag = next(iter(tags.values()))
    front = preamble.split("\n\n")[1].strip() if "\n\n" in preamble else ""
    if front and front != tag:
        fail(f"front matter is at {front}, the parts at {tag}.")
    print(f"edition guard: PASS (all parts at {tag})")
    return tag


def guard_invertible(preamble, parts, src):
    """Parts carry their own seam, so reassembly is plain concatenation."""
    rebuilt = preamble + "".join(parts[k] for k in EXPECT)
    if rebuilt != src:
        fail("the split is not invertible. Refusing to publish.")
    print("invertibility guard: PASS (parts recompile byte-for-byte)")


# ---------- split ----------

def split(src):
    hits = list(SEAM.finditer(src))
    names = [m.group(2) for m in hits]
    if names != EXPECT:
        fail(f"expected part seams {EXPECT}, found {names}.")

    preamble = src[:hits[0].start()]
    parts, tags = {}, {}
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(src)
        parts[m.group(2)] = src[m.start():end]
        tags[m.group(2)] = m.group(1)
    return preamble, parts, tags


def register_yaml(part, tag):
    """Lift the register out of its fence and restore the comment seam.

    The shipped register carries '# PART:' because an HTML comment will not
    parse as YAML; BLUEPRINT carries '<!-- PART: -->' because '#' is an H1
    in markdown. That one line is the only difference between them."""
    m = FENCE.search(part)
    if not m:
        fail("no ```yaml fence found in the REGISTER part.")
    body = m.group(1)
    try:
        parsed = yaml.safe_load(body)
    except yaml.YAMLError as e:
        fail(f"the register does not parse as YAML:\n{e}")
    for branch in ("status", "references"):
        if branch not in parsed:
            fail(f"the register is missing the '{branch}' branch")
    print(f"register parse guard: PASS "
          f"(apex {len(parsed['status']['apex'])}, "
          f"cabinet {len(parsed['status']['cabinet']['members'])}, "
          f"provinces {len(parsed['references']['thai_places']['provinces'])})")
    return f"# PART: {tag} REGISTER\n{body}\n", parsed


# ---------- rendered artifact ----------

def render_pdf(src):
    if not shutil.which("pandoc"):
        return "  skipped — pandoc not on PATH"

    # seams are HTML comments; surface them so they survive into the PDF
    visible = SEAM.sub(r"### PART: \1 \2", src)

    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8",
                                     delete=False) as fh:
        fh.write(visible)
        tmp = fh.name
    try:
        subprocess.run(
            ["pandoc", tmp,
             # tex_math_dollars off: currency ($1, US$, B500) is not maths.
             # raw_tex off: nothing in the copy is a LaTeX instruction.
             "-f", "markdown-tex_math_dollars-raw_tex",
             "-o", "BLUEPRINT.pdf",
             "--pdf-engine=xelatex", "--toc", "--toc-depth=3",
             # DejaVu covers ¥ € £ ½ ü and the em-dash; the LaTeX default does not
             "-V", "mainfont=DejaVu Serif", "-V", "monofont=DejaVu Sans Mono",
             "-V", "geometry:margin=2.5cm", "-V", "fontsize=10pt",
             "-V", "colorlinks=true", "-V", "linkcolor=black",
             # underscores in the tag are subscript to LaTeX outside math mode
             "-V", "title=The Bangkok Post Blueprint",
             "-V", "subtitle=" + TAG_HOLDER[0].replace("_", r"\_")],
            check=True, capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        return f"  FAILED — {e.stderr.decode()[-200:]}"
    finally:
        os.unlink(tmp)
    return f"{os.path.getsize('BLUEPRINT.pdf'):>7,} bytes  (rendered, do not edit)"


TAG_HOLDER = [""]


# ---------- build ----------

def main():
    if not os.path.exists(MASTER):
        fail(f"{MASTER} not found. It is the one file that is edited.")
    src = open(MASTER, encoding="utf-8").read()

    guard_dollars(src)
    preamble, parts, tags = split(src)
    tag = guard_edition(tags, preamble)
    TAG_HOLDER[0] = tag
    guard_invertible(preamble, parts, src)

    reg_text, _ = register_yaml(parts["REGISTER"], tag)

    open("CORE.txt", "w", encoding="utf-8").write(parts["CORE"].rstrip("\n") + "\n")
    open("REGISTER.yaml", "w", encoding="utf-8").write(reg_text)
    open("REGISTER.txt", "w", encoding="utf-8").write(reg_text)

    pdf = render_pdf(src)

    print()
    print(f"{MASTER:<15}{len(src):>8,} chars  {src.count(chr(10)) + 1:>5,} lines   SOURCE")
    for f in ("CORE.txt", "REGISTER.yaml", "REGISTER.txt"):
        print(f"{f:<15}{len(open(f, encoding='utf-8').read()):>8,} chars"
              f"{'':>13}derived")
    print(f"{'BLUEPRINT.pdf':<15}{pdf}")


if __name__ == "__main__":
    main()

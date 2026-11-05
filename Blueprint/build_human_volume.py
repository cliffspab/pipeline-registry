from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "BLUEPRINT.md"
OUTPUT = ROOT / "Blueprint_bkp3-2.docx"
PART_RE = re.compile(
    r"<!-- COMPONENT: ([A-Z]+) -->\n(.*?)\n<!-- END COMPONENT: \1 -->",
    re.S,
)


def border_bottom(paragraph, size: int) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        ppr.append(pbdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "5")
    bottom.set(qn("w:color"), "000000")
    pbdr.append(bottom)


def keep_with_next(paragraph) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    if ppr.find(qn("w:keepNext")) is None:
        ppr.append(OxmlElement("w:keepNext"))


def add_inline(paragraph, text: str) -> None:
    token = re.compile(r"(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[^]]+\]\([^)]+\))")
    pos = 0
    for match in token.finditer(text):
        if match.start() > pos:
            paragraph.add_run(text[pos:match.start()])
        value = match.group(0)
        if value.startswith("**"):
            run = paragraph.add_run(value[2:-2])
            run.bold = True
        elif value.startswith("*"):
            run = paragraph.add_run(value[1:-1])
            run.italic = True
        elif value.startswith("`"):
            run = paragraph.add_run(value[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(8.4)
        else:
            label, url = re.match(r"\[([^]]+)\]\(([^)]+)\)", value).groups()
            run = paragraph.add_run(f"{label} ({url})")
            run.underline = True
        pos = match.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


def add_frontmatter(doc: Document, lines: list[str]) -> None:
    for line in lines:
        if not line.strip():
            continue
        p = doc.add_paragraph(style="BKP Metadata")
        add_inline(p, line)
    if lines:
        border_bottom(doc.paragraphs[-1], 10)


def render_markdown(doc: Document, body: str) -> None:
    lines = body.splitlines()
    i = 0
    in_code = False
    code_lines: list[str] = []
    in_front = False
    front: list[str] = []
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            p = doc.add_paragraph(style="Body Text")
            add_inline(p, " ".join(x.strip() for x in paragraph_lines))
            paragraph_lines = []

    def flush_code() -> None:
        nonlocal code_lines
        if code_lines:
            p = doc.add_paragraph(style="BKP Code")
            p.add_run("\n".join(code_lines))
            code_lines = []

    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if stripped.startswith("<!--"):
            i += 1
            continue
        if stripped.startswith("```"):
            flush_paragraph()
            if in_code:
                flush_code()
            in_code = not in_code
            i += 1
            continue
        if in_code:
            code_lines.append(raw)
            i += 1
            continue
        if stripped == "---":
            flush_paragraph()
            if in_front:
                add_frontmatter(doc, front)
                front = []
            in_front = not in_front
            i += 1
            continue
        if in_front:
            front.append(raw)
            i += 1
            continue
        if stripped in {"***", "___"}:
            flush_paragraph()
            i += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", raw)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = heading.group(2).replace("`", "")
            p = doc.add_paragraph(style=f"Heading {level}")
            p.add_run(text)
            border_bottom(p, 28 if level == 1 else 12 if level == 2 else 0)
            keep_with_next(p)
            i += 1
            continue
        bullet = re.match(r"^(\s*)[-*]\s+(.+)$", raw)
        number = re.match(r"^(\s*)\d+\.\s+(.+)$", raw)
        if bullet or number:
            flush_paragraph()
            match = bullet or number
            level = min(len(match.group(1)) // 2, 2)
            style = "List Bullet" if bullet else "List Number"
            p = doc.add_paragraph(style=style)
            p.paragraph_format.left_indent = Cm(0.55 + level * 0.45)
            p.paragraph_format.first_line_indent = Cm(-0.25)
            add_inline(p, match.group(2))
            i += 1
            continue
        if not stripped:
            flush_paragraph()
        elif stripped.startswith("<") and stripped.endswith(">"):
            flush_paragraph()
            p = doc.add_paragraph(style="BKP XML")
            p.add_run(stripped)
        else:
            paragraph_lines.append(raw)
        i += 1
    flush_paragraph()
    flush_code()


def render_directory(doc: Document, body: str) -> None:
    doc.add_page_break()
    title = doc.add_paragraph(style="Heading 1")
    title.add_run("DIRECTORY")
    border_bottom(title, 28)
    keep_with_next(title)
    for line in body.splitlines():
        p = doc.add_paragraph(style="BKP Directory")
        p.paragraph_format.left_indent = Cm(min((len(line) - len(line.lstrip())) * 0.07, 2.2))
        p.add_run(line.lstrip() if line.strip() else " ")


def configure(doc: Document) -> None:
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.7)
    section.bottom_margin = Cm(1.7)
    section.left_margin = Cm(1.65)
    section.right_margin = Cm(1.65)

    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(9.2)
    normal.font.color.rgb = RGBColor(0, 0, 0)

    body = doc.styles["Body Text"]
    body.font.name = "Arial"
    body.font.size = Pt(9.2)
    body.paragraph_format.space_after = Pt(5)
    body.paragraph_format.line_spacing = 1.08

    for level, size, before, after in ((1, 21, 15, 8), (2, 13, 11, 5), (3, 10.5, 8, 3)):
        style = doc.styles[f"Heading {level}"]
        style.font.name = "Arial Black" if level == 1 else "Arial"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)

    for name in ("List Bullet", "List Number"):
        style = doc.styles[name]
        style.font.name = "Arial"
        style.font.size = Pt(8.8)
        style.paragraph_format.space_after = Pt(2.5)
        style.paragraph_format.line_spacing = 1.03

    specs = {
        "BKP Metadata": ("Consolas", 7.8, 1.0, 1.5),
        "BKP Code": ("Consolas", 7.8, 1.0, 5),
        "BKP XML": ("Consolas", 8.0, 1.0, 1),
        "BKP Directory": ("Consolas", 6.9, 0.9, 0),
    }
    for name, (font, size, spacing, after) in specs.items():
        style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = font
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.line_spacing = spacing
        style.paragraph_format.space_after = Pt(after)


def add_page_number(paragraph) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instr, end])


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    parts = dict(PART_RE.findall(text))
    preface = text.split("<!-- COMPONENT: BOOT -->", 1)[0]
    preface = re.sub(r"<!-- MASTER .*? -->\s*", "", preface)

    doc = Document()
    configure(doc)
    doc.core_properties.title = "Bangkok Post Blueprint"
    doc.core_properties.subject = "Desk edition 3.2"
    doc.core_properties.author = "Bangkok Post"
    doc.core_properties.comments = "Generated from the 051126_gpt_bkp3-2 Markdown authority"

    title = doc.add_paragraph()
    title.style = doc.styles["Title"]
    title.add_run("Bangkok Post Blueprint")
    title.runs[0].font.name = "Arial Black"
    title.runs[0].font.size = Pt(30)
    title.runs[0].font.bold = True
    title.runs[0].font.color.rgb = RGBColor(0, 0, 0)
    border_bottom(title, 38)
    render_markdown(doc, re.sub(r"^# Bangkok Post Blueprint\s*", "", preface))

    for index, name in enumerate(("BOOT", "EDIT", "CHECK", "PHOTO", "PR")):
        if name == "EDIT":
            doc.add_page_break()
        render_markdown(doc, parts[name])
    render_directory(doc, parts["DIRECTORY"])

    footer = doc.sections[0].footer.paragraphs[0]
    footer.style = doc.styles["Normal"]
    footer.runs.clear()
    footer.add_run("051126_gpt_bkp3-2   •   ")
    add_page_number(footer)

    settings = doc.settings._element
    update = OxmlElement("w:updateFields")
    update.set(qn("w:val"), "true")
    settings.append(update)
    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from fpdf import FPDF


def _safe_text(s: str) -> str:
    # Keep output compatible with core PDF fonts (latin-1).
    replacements = {
        "\u2013": "-",  # en dash
        "\u2014": "-",  # em dash
        "\u2116": "No.",  # numero sign
        "\u2192": "->",  # right arrow
        "\u2019": "'",  # right single quote
        "\u201c": '"',  # left double quote
        "\u201d": '"',  # right double quote
        "\u00a0": " ",  # nbsp
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    return s.encode("latin-1", "ignore").decode("latin-1")


@dataclass(frozen=True)
class TableStyle:
    line_height: float = 5.0
    padding: float = 1.5


class PracticalWorkPDF(FPDF):
    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def _wrap_text(pdf: FPDF, text: str, width: float) -> list[str]:
    text = _safe_text(text).strip()
    if not text:
        return [""]
    words = text.split()
    lines: list[str] = []
    current = ""
    for w in words:
        candidate = (current + " " + w).strip()
        if pdf.get_string_width(candidate) <= width:
            current = candidate
            continue
        if current:
            lines.append(current)
        current = w
    if current:
        lines.append(current)
    return lines or [""]


def _ensure_space(pdf: FPDF, height: float) -> None:
    if pdf.get_y() + height > pdf.page_break_trigger:
        pdf.add_page()


def _render_hr(pdf: FPDF) -> None:
    pdf.ln(2)
    x1 = pdf.l_margin
    x2 = pdf.w - pdf.r_margin
    y = pdf.get_y()
    pdf.set_draw_color(180, 180, 180)
    pdf.line(x1, y, x2, y)
    pdf.set_draw_color(0, 0, 0)
    pdf.ln(4)


def _render_heading(pdf: FPDF, text: str, level: int) -> None:
    text = _safe_text(text)
    pdf.ln(1)
    if level == 2:
        pdf.set_font("Helvetica", "B", 13)
        pdf.multi_cell(0, 7, text)
        pdf.ln(1)
    elif level == 3:
        pdf.set_font("Helvetica", "B", 11)
        pdf.multi_cell(0, 6, text)
    else:
        pdf.set_font("Helvetica", "B", 14)
        pdf.multi_cell(0, 7, text)
        pdf.ln(1)


def _render_paragraph(pdf: FPDF, text: str, indent_mm: float = 0.0) -> None:
    text = _safe_text(text)
    pdf.set_font("Helvetica", "", 10.5)
    x = pdf.l_margin + indent_mm
    pdf.set_x(x)
    pdf.multi_cell(0, 5, text)


def _parse_md_table(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for ln in lines:
        s = ln.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        parts = [p.strip() for p in s.strip("|").split("|")]
        # Skip separator lines like |---|---|
        if parts and all(set(p) <= {"-", ":"} for p in parts):
            continue
        rows.append(parts)
    return rows


def _render_table(pdf: FPDF, table_lines: list[str]) -> None:
    rows = _parse_md_table(table_lines)
    if not rows:
        return

    style = TableStyle()
    col_count = max(len(r) for r in rows)
    rows = [r + [""] * (col_count - len(r)) for r in rows]

    # Column width allocation tuned for the Objective/Sections/Methods/Results table.
    page_w = pdf.w - pdf.l_margin - pdf.r_margin
    if col_count == 4:
        col_widths = [0.10 * page_w, 0.25 * page_w, 0.27 * page_w, 0.38 * page_w]
    else:
        col_widths = [page_w / col_count] * col_count

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(245, 245, 245)

    def render_row(cells: list[str], is_header: bool) -> None:
        pdf.set_font("Helvetica", "B" if is_header else "", 9.5)
        wrapped = [
            _wrap_text(pdf, c, w - 2 * style.padding) for c, w in zip(cells, col_widths)
        ]
        max_lines = max(len(w) for w in wrapped) if wrapped else 1
        row_h = max_lines * style.line_height + 2 * style.padding

        _ensure_space(pdf, row_h)

        x0 = pdf.get_x()
        y0 = pdf.get_y()
        x = x0
        for cell_lines, w in zip(wrapped, col_widths):
            pdf.rect(x, y0, w, row_h)
            tx = x + style.padding
            ty = y0 + style.padding
            pdf.set_xy(tx, ty)
            for i, line in enumerate(cell_lines):
                pdf.cell(w - 2 * style.padding, style.line_height, _safe_text(line), ln=1)
            x += w
        pdf.set_xy(x0, y0 + row_h)

    # Header row
    header = rows[0]
    # Fill header background (drawn as filled rects)
    header_wrapped = [_wrap_text(pdf, c, w - 2 * style.padding) for c, w in zip(header, col_widths)]
    header_lines = max(len(w) for w in header_wrapped)
    header_h = header_lines * style.line_height + 2 * style.padding
    _ensure_space(pdf, header_h)
    x0 = pdf.get_x()
    y0 = pdf.get_y()
    x = x0
    for w in col_widths:
        pdf.rect(x, y0, w, header_h, style="DF")
        x += w
    pdf.set_xy(x0, y0)
    render_row(header, is_header=True)

    # Body
    pdf.set_fill_color(255, 255, 255)
    for row in rows[1:]:
        render_row(row, is_header=False)

    pdf.ln(2)


def _render_body_from_md(pdf: FPDF, body_lines: list[str]) -> None:
    i = 0
    while i < len(body_lines):
        raw = body_lines[i].rstrip("\n")
        line = raw.rstrip()

        if not line.strip():
            pdf.ln(2)
            i += 1
            continue

        if line.strip() == "---":
            _render_hr(pdf)
            i += 1
            continue

        if line.startswith("## "):
            _render_heading(pdf, line[3:].strip(), level=2)
            i += 1
            continue

        if line.startswith("### "):
            _render_heading(pdf, line[4:].strip(), level=3)
            i += 1
            continue

        if line.lstrip().startswith("|") and line.strip().endswith("|"):
            table_block: list[str] = []
            while i < len(body_lines):
                l2 = body_lines[i].rstrip("\n")
                if not (l2.lstrip().startswith("|") and l2.strip().endswith("|")):
                    break
                table_block.append(l2)
                i += 1
            _render_table(pdf, table_block)
            continue

        stripped = line.lstrip()
        if stripped.startswith("- "):
            leading_spaces = len(line) - len(stripped)
            nest_level = max(0, leading_spaces // 2)
            bullet_text = stripped[2:].strip()
            _render_paragraph(pdf, f"- {bullet_text}", indent_mm=4.0 + 4.0 * nest_level)
            i += 1
            continue

        _render_paragraph(pdf, line)
        i += 1


def build_pdf(md_path: Path, out_path: Path) -> None:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    sep_idx = next((idx for idx, ln in enumerate(lines) if ln.strip() == "---"), None)
    title_lines = lines[:sep_idx] if sep_idx is not None else lines[:8]
    body_lines = lines[sep_idx + 1 :] if sep_idx is not None else lines

    pdf = PracticalWorkPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)

    # Title page
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.ln(12)
    if title_lines:
        pdf.multi_cell(0, 8, _safe_text(title_lines[0].strip()), align="C")
        pdf.ln(2)
    pdf.set_font("Helvetica", "", 12)
    for ln in title_lines[1:]:
        t = ln.strip()
        if not t:
            pdf.ln(2)
            continue
        pdf.multi_cell(0, 7, _safe_text(t), align="C")

    pdf.ln(6)
    _render_hr(pdf)
    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(
        0,
        6,
        _safe_text(
            "This PDF contains: a complete thesis table of contents, chapter/section hierarchy, mapping to research objectives, "
            "section content descriptions, and a logical research model."
        ),
        align="C",
    )

    # Body
    pdf.add_page()
    _render_body_from_md(pdf, body_lines)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    md = base / "practical_work_7_8.md"
    out = base / "Didar_Kanalbay_sis-2224_PracticalWork_7-8.pdf"
    build_pdf(md, out)
    print(f"Generated: {out}")

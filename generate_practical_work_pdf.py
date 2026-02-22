from datetime import date

from fpdf import FPDF
from fpdf.enums import XPos, YPos
from fpdf.fonts import FontFace


NAME = "Didar Kanalbay"
GROUP = "sis-2224"
PRACTICAL_TITLE = "PRACTICAL WORK No. 7-8"
PRACTICAL_TOPIC = "Designing the Structure of a Thesis and the Logic of Scientific Research"
RESEARCH_TOPIC = (
    "Creating a multiclass model for detecting destructive web content in social "
    "networks and instant messengers using machine learning"
)

# These placeholders keep the layout official-looking while avoiding incorrect facts.
UNIVERSITY_LINE_1 = "MINISTRY OF SCIENCE AND HIGHER EDUCATION OF THE REPUBLIC OF KAZAKHSTAN"
UNIVERSITY_LINE_2 = "[UNIVERSITY NAME]"
UNIVERSITY_LINE_3 = "[FACULTY / DEPARTMENT]"
CITY = "[CITY]"


class FormalAssignmentPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_y(9)
        self.set_font("Times", "I", 10)
        self.set_text_color(70, 70, 70)
        self.cell(
            0,
            5,
            f"{PRACTICAL_TITLE} - {NAME}, group {GROUP}",
            align="R",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        self.set_draw_color(150, 150, 150)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_draw_color(160, 160, 160)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(2)
        self.set_font("Times", "I", 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, f"- {self.page_no()} -", align="C")


def add_formal_cover_page(pdf: FormalAssignmentPDF):
    pdf.add_page()

    page_w = pdf.w - pdf.l_margin - pdf.r_margin

    # Double border for a formal document style.
    pdf.set_draw_color(80, 80, 80)
    pdf.rect(12, 12, pdf.w - 24, pdf.h - 24)
    pdf.rect(14, 14, pdf.w - 28, pdf.h - 28)

    pdf.set_y(28)
    pdf.set_text_color(20, 20, 20)
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(
        0,
        6,
        UNIVERSITY_LINE_1,
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font("Times", "B", 12)
    pdf.multi_cell(
        0,
        6,
        UNIVERSITY_LINE_2,
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(
        0,
        6,
        UNIVERSITY_LINE_3,
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.ln(28)
    pdf.set_font("Times", "B", 16)
    pdf.multi_cell(
        0,
        8,
        PRACTICAL_TITLE,
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font("Times", "B", 13)
    pdf.multi_cell(
        0,
        7,
        f"Topic: {PRACTICAL_TOPIC}",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.ln(20)
    pdf.set_font("Times", "", 13)
    pdf.multi_cell(
        0,
        7,
        "Research topic:",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font("Times", "I", 13)
    pdf.multi_cell(
        0,
        7,
        RESEARCH_TOPIC,
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    # Signature block on right side.
    pdf.set_y(195)
    block_x = pdf.l_margin + page_w * 0.52
    block_w = page_w * 0.42
    pdf.set_x(block_x)
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(
        block_w,
        7,
        "Completed by: __________________",
        align="L",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_x(block_x)
    pdf.set_font("Times", "B", 12)
    pdf.cell(block_w, 7, f"{NAME}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(block_x)
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(
        block_w,
        7,
        "Group: _________________________",
        align="L",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_x(block_x)
    pdf.set_font("Times", "B", 12)
    pdf.cell(block_w, 7, GROUP, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(block_x)
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(
        block_w,
        7,
        "Checked by: ____________________",
        align="L",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    # Bottom line.
    pdf.set_y(-35)
    pdf.set_font("Times", "", 12)
    pdf.cell(
        0,
        8,
        f"{CITY} - {date.today().year}",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_font("Times", "I", 10)
    pdf.set_text_color(90, 90, 90)
    pdf.multi_cell(
        0,
        5,
        "Note: Replace [UNIVERSITY NAME], [FACULTY / DEPARTMENT], and [CITY] with your official details.",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )


def section_title(pdf: FormalAssignmentPDF, text: str):
    pdf.ln(1)
    pdf.set_fill_color(236, 236, 236)
    pdf.set_draw_color(170, 170, 170)
    pdf.set_font("Times", "B", 13)
    pdf.set_text_color(15, 15, 15)
    pdf.multi_cell(0, 8, text, border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1.5)
    pdf.set_text_color(20, 20, 20)


def subsection_title(pdf: FormalAssignmentPDF, text: str):
    pdf.set_font("Times", "B", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(20, 20, 20)


def paragraph(pdf: FormalAssignmentPDF, text: str):
    pdf.set_font("Times", "", 12)
    pdf.multi_cell(0, 6.2, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(0.8)


def bullets(pdf: FormalAssignmentPDF, items: list[str], indent: int = 5):
    pdf.set_font("Times", "", 12)
    for item in items:
        pdf.set_x(pdf.l_margin + indent)
        pdf.cell(4, 6.2, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(0, 6.2, item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(0.8)


def numbered(pdf: FormalAssignmentPDF, items: list[str], indent: int = 5):
    pdf.set_font("Times", "", 12)
    for idx, item in enumerate(items, start=1):
        label = f"{idx}) "
        pdf.set_x(pdf.l_margin + indent)
        pdf.set_font("Times", "B", 12)
        pdf.cell(pdf.get_string_width(label) + 1, 6.2, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Times", "", 12)
        pdf.multi_cell(0, 6.2, item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(0.8)


def outline(pdf: FormalAssignmentPDF, rows: list[tuple[int, str]]):
    for level, text in rows:
        pdf.set_x(pdf.l_margin + level * 6)
        if level == 0:
            pdf.set_font("Times", "B", 12)
        elif level == 1:
            pdf.set_font("Times", "", 12)
        else:
            pdf.set_font("Times", "I", 11)
        pdf.multi_cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(0.8)


def objective_table(pdf: FormalAssignmentPDF):
    headers = ["Research objective", "Thesis section", "Methods", "Expected results"]
    rows = [
        [
            "O1. Analyze the domain and define destructive content classes",
            "1.1, 1.3",
            "Literature review, domain analysis, content taxonomy",
            "Formal taxonomy of destructive content and clear problem boundaries",
        ],
        [
            "O2. Review and compare ML approaches",
            "1.2, 1.3",
            "Systematic review, comparative analysis",
            "Criteria for selecting the most suitable model family",
        ],
        [
            "O3. Formulate multiclass problem and choose methods/tools",
            "2.1, 2.2",
            "Task formalization, metric design, tool selection",
            "Defined data pipeline, metrics, and implementation stack",
        ],
        [
            "O4. Develop model, algorithm, and system architecture",
            "2.3, 2.4",
            "Algorithm design, prototyping, engineering architecture",
            "Implemented multiclass model and deployable architecture",
        ],
        [
            "O5. Run experiments and benchmark against analogues",
            "3.1-3.5",
            "Controlled experiments, statistical evaluation",
            "Evidence of quality gains, limitations, and practical feasibility",
        ],
        [
            "O6. Generalize findings and formulate recommendations",
            "3.6, Conclusion",
            "Interpretation and synthesis",
            "Scientifically grounded conclusions and implementation guidance",
        ],
    ]

    pdf.set_font("Times", "", 10.5)
    with pdf.table(
        width=pdf.w - pdf.l_margin - pdf.r_margin,
        col_widths=(43, 28, 49, 60),
        line_height=5.2,
        text_align=("LEFT", "CENTER", "LEFT", "LEFT"),
        padding=1.2,
        headings_style=FontFace(
            emphasis="BOLD",
            fill_color=(230, 230, 230),
            color=(20, 20, 20),
        ),
    ) as table:
        row = table.row()
        for cell in headers:
            row.cell(cell)
        for values in rows:
            row = table.row()
            for cell in values:
                row.cell(cell)
    pdf.ln(1.5)


def logic_model_box(pdf: FormalAssignmentPDF):
    x = pdf.l_margin
    y = pdf.get_y()
    w = pdf.w - pdf.l_margin - pdf.r_margin
    h = 30

    pdf.set_fill_color(247, 247, 247)
    pdf.set_draw_color(150, 150, 150)
    pdf.rect(x, y, w, h, style="DF")

    pdf.set_xy(x + 4, y + 5)
    pdf.set_font("Times", "B", 12)
    pdf.multi_cell(
        w - 8,
        6,
        "Scientific problem -> Goal -> Objectives -> Chapters -> Methods -> Results -> Conclusions",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(2)


def build_pdf(output_path: str):
    pdf = FormalAssignmentPDF(format="A4")
    pdf.set_margins(left=16, top=16, right=16)
    pdf.set_auto_page_break(auto=True, margin=16)

    add_formal_cover_page(pdf)
    pdf.add_page()

    section_title(pdf, "1. Purpose of the Practical Work")
    paragraph(
        pdf,
        "To develop the ability to design a logically structured thesis in which the scientific problem, "
        "goal, objectives, methods, and results are connected in one coherent research framework.",
    )

    section_title(pdf, "2. Requirements for the Thesis Structure")
    bullets(
        pdf,
        [
            "Reflect the logic of scientific research.",
            "Ensure consistent unfolding of the topic from theory to practical implementation.",
            "Correspond directly to the stated research objectives.",
            "Include theoretical, methodological, and experimental-practical parts.",
            "Prevent duplication and maintain clear chapter responsibilities.",
        ],
    )

    section_title(pdf, "3. Student Assignment")
    numbered(
        pdf,
        [
            "Develop a complete thesis table of contents.",
            "Define chapters, sections, and subsections.",
            "Establish the connection between each chapter and research objectives.",
            "Determine the content of each section.",
            "Construct a logical model of the thesis structure.",
        ],
    )

    section_title(pdf, "4. Complete Table of Contents for the Topic")
    outline(
        pdf,
        [
            (0, "INTRODUCTION"),
            (1, "Relevance of the topic, problem statement, goal, objectives, object, subject, methods"),
            (0, "CHAPTER 1. THEORETICAL FOUNDATIONS OF DETECTING DESTRUCTIVE WEB CONTENT"),
            (1, "1.1 Analysis of the subject area"),
            (2, "1.1.1 Definition and taxonomy of destructive web content"),
            (2, "1.1.2 Features of social networks and instant messengers"),
            (2, "1.1.3 Legal and ethical constraints"),
            (1, "1.2 Review of methods and approaches"),
            (2, "1.2.1 Classical ML methods"),
            (2, "1.2.2 Deep learning and transformer models"),
            (2, "1.2.3 Multilingual and domain-adapted approaches"),
            (1, "1.3 Comparative analysis of existing solutions"),
            (2, "1.3.1 Academic benchmarks and datasets"),
            (2, "1.3.2 Industrial moderation tools"),
            (2, "1.3.3 Gaps and unresolved issues"),
            (1, "1.4 Conclusions for Chapter 1"),
            (0, "CHAPTER 2. METHODOLOGY AND DEVELOPMENT OF THE SOLUTION"),
            (1, "2.1 Problem statement and formal definition of the multiclass task"),
            (1, "2.2 Selection of methods, tools, and evaluation metrics"),
            (1, "2.3 Development of the model and training algorithm"),
            (1, "2.4 System architecture and implementation workflow"),
            (1, "2.5 Conclusions for Chapter 2"),
            (0, "CHAPTER 3. EXPERIMENTAL PART"),
            (1, "3.1 Data description and experiment setup"),
            (1, "3.2 Experimental methodology and reproducibility protocol"),
            (1, "3.3 Quantitative results"),
            (1, "3.4 Analysis of results and error typology"),
            (1, "3.5 Comparison with analogues"),
            (1, "3.6 Conclusions for Chapter 3"),
            (0, "CONCLUSION"),
            (0, "REFERENCES"),
            (0, "APPENDICES"),
        ],
    )

    section_title(pdf, "5. Connection Between Chapters and Research Objectives")
    paragraph(
        pdf,
        "Research goal: develop and experimentally validate a multiclass machine learning model for "
        "detecting destructive web content in social networks and instant messengers.",
    )
    bullets(
        pdf,
        [
            "O1 -> Chapter 1 (1.1, 1.3): domain analysis and taxonomy of classes.",
            "O2 -> Chapter 1 (1.2, 1.3): review and comparison of methods.",
            "O3 -> Chapter 2 (2.1, 2.2): task formalization and method/tool selection.",
            "O4 -> Chapter 2 (2.3, 2.4): model development and system architecture.",
            "O5 -> Chapter 3 (3.1-3.5): experiment design, validation, and benchmarking.",
            "O6 -> Chapter conclusions + final conclusion: synthesis and recommendations.",
        ],
    )

    section_title(pdf, "6. Table Linking Objectives and Structure")
    objective_table(pdf)

    section_title(pdf, "7. Content of Each Section")
    subsection_title(pdf, "Introduction")
    bullets(
        pdf,
        [
            "Explain relevance of destructive content detection for modern communication platforms.",
            "Define the scientific problem and justify the need for multiclass classification.",
            "Present goal, objectives, methods, novelty, and practical significance.",
        ],
    )

    subsection_title(pdf, "Chapter 1 (Theoretical)")
    bullets(
        pdf,
        [
            "Build conceptual framework and class taxonomy for destructive content.",
            "Review and compare existing machine learning approaches.",
            "Identify gaps that motivate development of a new multiclass model.",
        ],
    )

    subsection_title(pdf, "Chapter 2 (Methodology and Development)")
    bullets(
        pdf,
        [
            "Formally define the task, data assumptions, and quality criteria.",
            "Describe data preparation, feature representation, and algorithm selection.",
            "Present model architecture, training strategy, and deployment workflow.",
        ],
    )

    subsection_title(pdf, "Chapter 3 (Experimental)")
    bullets(
        pdf,
        [
            "Describe dataset composition, experiment setup, and reproducibility protocol.",
            "Report quantitative results using Precision, Recall, Macro-F1, and related metrics.",
            "Analyze per-class behavior, errors, robustness, and comparison with analogues.",
        ],
    )

    subsection_title(pdf, "Conclusion")
    bullets(
        pdf,
        [
            "Summarize scientific and practical contributions by objective.",
            "State limitations and future work directions.",
            "Provide practical recommendations for implementation in moderation systems.",
        ],
    )

    section_title(pdf, "8. Logical Model of the Thesis Structure")
    logic_model_box(pdf)
    paragraph(
        pdf,
        "Expanded chain for this topic: destructive content moderation problem -> need for a multiclass model "
        "-> domain analysis and method review -> model and architecture development -> experimental validation "
        "-> conclusions and practical guidance.",
    )

    section_title(pdf, "9. Typical Mistakes and How This Structure Avoids Them")
    numbered(
        pdf,
        [
            "No connection between objectives and structure. Solved by explicit objective-to-section mapping.",
            "Overly general section titles. Solved by using topic-specific, measurable section names.",
            "Mismatch between theory and practice. Solved by linking Chapter 1 gaps to Chapter 2 design choices.",
            "Content duplication. Solved by clear role separation across theoretical, methodological, and experimental chapters.",
        ],
    )

    section_title(pdf, "Final Note")
    paragraph(
        pdf,
        "The proposed thesis structure is coherent, objective-driven, and methodologically aligned with the "
        "selected topic. It ensures traceability from scientific problem to validated practical results.",
    )

    pdf.output(output_path)


if __name__ == "__main__":
    build_pdf("/workspace/Practical_Work_7_8_Didar_Kanalbay.pdf")

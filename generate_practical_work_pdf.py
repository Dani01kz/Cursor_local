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


class StyledAssignmentPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 115)
        self.cell(
            0,
            6,
            f"{PRACTICAL_TITLE} | {NAME} | Group {GROUP}",
            align="R",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        self.set_draw_color(210, 220, 235)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(210, 220, 235)
        self.line(self.l_margin, self.get_y() - 1, self.w - self.r_margin, self.get_y() - 1)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(110, 110, 110)
        self.cell(0, 6, f"Page {self.page_no()}", align="C")


def add_title_page(pdf: StyledAssignmentPDF):
    pdf.add_page()

    # Top banner
    banner_x = pdf.l_margin
    banner_y = 22
    banner_w = pdf.w - pdf.l_margin - pdf.r_margin
    banner_h = 36
    pdf.set_fill_color(35, 74, 125)
    pdf.rect(banner_x, banner_y, banner_w, banner_h, style="F")

    pdf.set_xy(banner_x, banner_y + 7)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 8, PRACTICAL_TITLE, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 7, PRACTICAL_TOPIC, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Student card
    card_x = pdf.l_margin
    card_y = 72
    card_w = pdf.w - pdf.l_margin - pdf.r_margin
    card_h = 42
    pdf.set_fill_color(245, 248, 253)
    pdf.set_draw_color(198, 210, 230)
    pdf.rect(card_x, card_y, card_w, card_h, style="DF")

    pdf.set_text_color(35, 35, 35)
    pdf.set_xy(card_x + 8, card_y + 8)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(24, 8, "Student:")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, NAME, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(card_x + 8)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(24, 8, "Group:")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, GROUP, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(card_x + 8)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(24, 8, "Date:")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, date.today().strftime("%B %d, %Y"), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Research topic
    pdf.ln(18)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(27, 56, 100)
    pdf.cell(0, 8, "Research topic", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 7, RESEARCH_TOPIC)


def h1(pdf: StyledAssignmentPDF, text: str):
    pdf.ln(1)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(27, 56, 100)
    pdf.multi_cell(0, 8, text)
    pdf.set_draw_color(205, 218, 238)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(2)
    pdf.set_text_color(40, 40, 40)


def h2(pdf: StyledAssignmentPDF, text: str):
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(40, 73, 122)
    pdf.multi_cell(0, 7, text)
    pdf.set_text_color(40, 40, 40)


def paragraph(pdf: StyledAssignmentPDF, text: str):
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, text)
    pdf.ln(1)


def bullets(pdf: StyledAssignmentPDF, items: list[str], indent: int = 5):
    pdf.set_font("Helvetica", "", 11)
    for item in items:
        pdf.set_x(pdf.l_margin + indent)
        pdf.cell(4, 6, "-", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(0, 6, item)
    pdf.ln(1)


def numbered(pdf: StyledAssignmentPDF, items: list[str], indent: int = 5):
    for idx, item in enumerate(items, start=1):
        label = f"{idx}) "
        pdf.set_x(pdf.l_margin + indent)
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(pdf.get_string_width(label) + 1, 6, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 6, item)
    pdf.ln(1)


def outline(pdf: StyledAssignmentPDF, rows: list[tuple[int, str]]):
    for level, text in rows:
        pdf.set_x(pdf.l_margin + level * 6)
        if level == 0:
            pdf.set_font("Helvetica", "B", 11)
        elif level == 1:
            pdf.set_font("Helvetica", "", 11)
        else:
            pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, text)
    pdf.ln(1)


def objective_table(pdf: StyledAssignmentPDF):
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

    pdf.set_font("Helvetica", "", 10)
    with pdf.table(
        width=pdf.w - pdf.l_margin - pdf.r_margin,
        col_widths=(42, 28, 50, 60),
        line_height=5.4,
        text_align=("LEFT", "CENTER", "LEFT", "LEFT"),
        padding=1.3,
        headings_style=FontFace(
            emphasis="BOLD",
            fill_color=(226, 236, 252),
            color=(20, 46, 88),
        ),
    ) as table:
        row = table.row()
        for cell in headers:
            row.cell(cell)
        for r in rows:
            row = table.row()
            for cell in r:
                row.cell(cell)

    pdf.ln(2)


def logic_model_box(pdf: StyledAssignmentPDF):
    box_x = pdf.l_margin
    box_y = pdf.get_y()
    box_w = pdf.w - pdf.l_margin - pdf.r_margin
    box_h = 28

    pdf.set_fill_color(245, 248, 253)
    pdf.set_draw_color(198, 210, 230)
    pdf.rect(box_x, box_y, box_w, box_h, style="DF")

    pdf.set_xy(box_x + 4, box_y + 5)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(34, 65, 109)
    pdf.multi_cell(
        box_w - 8,
        6,
        "Scientific problem -> Goal -> Objectives -> Chapters -> Methods -> Results -> Conclusions",
        align="C",
    )
    pdf.set_text_color(40, 40, 40)
    pdf.ln(3)


def build_pdf(output_path: str):
    pdf = StyledAssignmentPDF(format="A4")
    pdf.set_margins(left=15, top=15, right=15)
    pdf.set_auto_page_break(auto=True, margin=15)

    add_title_page(pdf)
    pdf.add_page()

    h1(pdf, "1. Purpose of the Practical Work")
    paragraph(
        pdf,
        "To develop the ability to design a logically structured thesis in which the scientific problem, "
        "goal, objectives, methods, and results are connected in one coherent research framework.",
    )

    h1(pdf, "2. Requirements for the Thesis Structure")
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

    h1(pdf, "3. Student Assignment")
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

    h1(pdf, "4. Complete Table of Contents for the Topic")
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

    h1(pdf, "5. Connection Between Chapters and Research Objectives")
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

    h1(pdf, "6. Table Linking Objectives and Structure")
    objective_table(pdf)

    h1(pdf, "7. Content of Each Section")
    h2(pdf, "Introduction")
    bullets(
        pdf,
        [
            "Explain relevance of destructive content detection for modern communication platforms.",
            "Define the scientific problem and justify the need for multiclass classification.",
            "Present goal, objectives, methods, novelty, and practical significance.",
        ],
    )

    h2(pdf, "Chapter 1 (Theoretical)")
    bullets(
        pdf,
        [
            "Build conceptual framework and class taxonomy for destructive content.",
            "Review and compare existing machine learning approaches.",
            "Identify gaps that motivate development of a new multiclass model.",
        ],
    )

    h2(pdf, "Chapter 2 (Methodology and Development)")
    bullets(
        pdf,
        [
            "Formally define the task, data assumptions, and quality criteria.",
            "Describe data preparation, feature representation, and algorithm selection.",
            "Present model architecture, training strategy, and deployment workflow.",
        ],
    )

    h2(pdf, "Chapter 3 (Experimental)")
    bullets(
        pdf,
        [
            "Describe dataset composition, experiment setup, and reproducibility protocol.",
            "Report quantitative results using Precision, Recall, Macro-F1, and related metrics.",
            "Analyze per-class behavior, errors, robustness, and comparison with analogues.",
        ],
    )

    h2(pdf, "Conclusion")
    bullets(
        pdf,
        [
            "Summarize scientific and practical contributions by objective.",
            "State limitations and future work directions.",
            "Provide practical recommendations for implementation in moderation systems.",
        ],
    )

    h1(pdf, "8. Logical Model of the Thesis Structure")
    logic_model_box(pdf)
    paragraph(
        pdf,
        "Expanded chain for this topic: destructive content moderation problem -> need for a multiclass model "
        "-> domain analysis and method review -> model and architecture development -> experimental validation "
        "-> conclusions and practical guidance.",
    )

    h1(pdf, "9. Typical Mistakes and How This Structure Avoids Them")
    numbered(
        pdf,
        [
            "No connection between objectives and structure. Solved by explicit objective-to-section mapping.",
            "Overly general section titles. Solved by using topic-specific, measurable section names.",
            "Mismatch between theory and practice. Solved by linking Chapter 1 gaps to Chapter 2 design choices.",
            "Content duplication. Solved by clear role separation across theoretical, methodological, and experimental chapters.",
        ],
    )

    h1(pdf, "Final Note")
    paragraph(
        pdf,
        "The proposed thesis structure is coherent, objective-driven, and methodologically aligned with the "
        "selected topic. It ensures traceability from scientific problem to validated practical results.",
    )

    pdf.output(output_path)


if __name__ == "__main__":
    build_pdf("/workspace/Practical_Work_7_8_Didar_Kanalbay.pdf")

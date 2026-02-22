from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors


PAGE_W, PAGE_H = A4
MARGIN = 2.0 * cm

doc = SimpleDocTemplate(
    "Practical_Work_7_8_Didar_Kanalbay.pdf",
    pagesize=A4,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
)

styles = getSampleStyleSheet()

DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#16213e")
BLUE = HexColor("#0f3460")
HIGHLIGHT = HexColor("#e94560")
LIGHT_BG = HexColor("#f5f5f5")
WHITE = white

style_title = ParagraphStyle(
    "CTitle", parent=styles["Title"],
    fontSize=22, leading=28, textColor=DARK,
    spaceAfter=6, alignment=TA_CENTER, fontName="Helvetica-Bold",
)
style_subtitle = ParagraphStyle(
    "CSubtitle", parent=styles["Normal"],
    fontSize=13, leading=17, textColor=BLUE,
    spaceAfter=4, alignment=TA_CENTER, fontName="Helvetica",
)
style_heading1 = ParagraphStyle(
    "CH1", parent=styles["Heading1"],
    fontSize=16, leading=22, textColor=DARK,
    spaceBefore=18, spaceAfter=8, fontName="Helvetica-Bold",
)
style_heading2 = ParagraphStyle(
    "CH2", parent=styles["Heading2"],
    fontSize=13, leading=18, textColor=BLUE,
    spaceBefore=12, spaceAfter=6, fontName="Helvetica-Bold",
)
style_heading3 = ParagraphStyle(
    "CH3", parent=styles["Heading3"],
    fontSize=11, leading=15, textColor=ACCENT,
    spaceBefore=8, spaceAfter=4, fontName="Helvetica-BoldOblique",
    leftIndent=12,
)
style_body = ParagraphStyle(
    "CBody", parent=styles["Normal"],
    fontSize=10.5, leading=15, textColor=black,
    spaceAfter=4, alignment=TA_JUSTIFY, fontName="Helvetica",
)
style_body_indent = ParagraphStyle(
    "CBodyInd", parent=style_body, leftIndent=18,
)
style_table_header = ParagraphStyle(
    "CTH", parent=styles["Normal"],
    fontSize=9.5, leading=13, textColor=WHITE,
    fontName="Helvetica-Bold", alignment=TA_CENTER,
)
style_table_cell = ParagraphStyle(
    "CTC", parent=styles["Normal"],
    fontSize=9, leading=12.5, textColor=black,
    fontName="Helvetica", alignment=TA_LEFT,
)
style_table_cell_c = ParagraphStyle(
    "CTCC", parent=style_table_cell, alignment=TA_CENTER,
)

story = []


def add_spacer(h=0.3):
    story.append(Spacer(1, h * cm))

def add_hr():
    story.append(HRFlowable(width="100%", thickness=1, color=HIGHLIGHT, spaceAfter=8, spaceBefore=8))

def h1(text):
    story.append(Paragraph(text, style_heading1))

def h2(text):
    story.append(Paragraph(text, style_heading2))

def h3(text):
    story.append(Paragraph(text, style_heading3))

def body(text, indent=False):
    story.append(Paragraph(text, style_body_indent if indent else style_body))


# ── COVER PAGE ──

add_spacer(2.5)
story.append(Paragraph("PRACTICAL WORK &#8470; 7&ndash;8", style_title))
add_spacer(0.3)
story.append(Paragraph(
    "Designing the Structure of a Thesis<br/>and the Logic of Scientific Research",
    style_subtitle,
))
add_spacer(1.0)
add_hr()
add_spacer(0.3)
story.append(Paragraph(
    "<b>Student:</b>&nbsp; Didar Kanalbay &nbsp;&nbsp;|&nbsp;&nbsp; <b>Group:</b>&nbsp; SIS-2224",
    ParagraphStyle("meta", parent=style_body, alignment=TA_CENTER, fontSize=12, leading=16),
))
add_spacer(0.3)
add_hr()
add_spacer(0.8)
story.append(Paragraph(
    "<b>Thesis Topic:</b>",
    ParagraphStyle("lbl", parent=style_body, alignment=TA_CENTER, fontSize=11, textColor=BLUE),
))
add_spacer(0.15)
story.append(Paragraph(
    "<i>Creating a Multiclass Model for Detecting Destructive Web Content<br/>"
    "in Social Networks and Instant Messengers Using Machine Learning</i>",
    ParagraphStyle("topic", parent=style_body, alignment=TA_CENTER, fontSize=12, leading=17, textColor=DARK),
))
add_spacer(4)
story.append(Paragraph(
    "2025",
    ParagraphStyle("year", parent=style_body, alignment=TA_CENTER, fontSize=11, textColor=BLUE),
))
story.append(PageBreak())


# ── 1. PURPOSE ──

h1("1. Purpose of the Practical Work")
body(
    "To develop the ability to design a logically structured thesis that ensures "
    "the relationship between the scientific problem, the goal, the objectives, "
    "the methods, and the results of the research on the topic of "
    "<i>creating a multiclass model for detecting destructive web content in social "
    "networks and instant messengers using machine learning</i>."
)
add_spacer(0.4)


# ── 2. SCIENTIFIC PROBLEM, GOAL, OBJECTIVES ──

h1("2. Scientific Problem, Goal, and Objectives")

h2("2.1 Scientific Problem")
body(
    "Existing content-moderation systems for social networks and instant messengers "
    "are predominantly binary (harmful vs. safe) or rely on keyword-based filtering. "
    "They fail to distinguish among multiple categories of destructive content "
    "(extremism, cyberbullying, self-harm promotion, fraud, disinformation, etc.), "
    "leading to high false-positive rates and poor coverage of emerging threats. "
    "There is a need for a robust multiclass classification framework that can "
    "accurately and efficiently categorize diverse types of destructive web content."
)

h2("2.2 Goal of the Research")
body(
    "To develop and validate a multiclass machine-learning model capable of detecting "
    "and classifying multiple categories of destructive web content in social networks "
    "and instant messengers with high accuracy, interpretability, and scalability."
)

h2("2.3 Research Objectives")
objectives = [
    "To analyze the current state of research on destructive-content detection and identify gaps in multiclass classification approaches.",
    "To define and systematize a taxonomy of destructive web content categories relevant to social networks and instant messengers.",
    "To review and compare machine-learning methods applicable to multiclass text classification (traditional ML, deep learning, transformers).",
    "To collect, preprocess, and annotate a representative multilingual dataset of social-media and messenger content.",
    "To design the architecture of a multiclass classification model and select optimal features and hyperparameters.",
    "To implement the model and conduct experiments evaluating accuracy, precision, recall, F1-score, and inference time.",
    "To compare the proposed model with existing analogues and baseline solutions.",
    "To formulate practical recommendations for integrating the model into content-moderation pipelines.",
]
for i, obj in enumerate(objectives, 1):
    body(f"<b>Objective {i}.</b> {obj}", indent=True)

add_spacer(0.4)


# ── 3. COMPLETE TABLE OF CONTENTS ──

h1("3. Complete Table of Contents of the Thesis")
add_hr()

toc_items = [
    ("", "Introduction", False),
    ("", "", False),
    ("", "Chapter 1. Theoretical Foundations of Destructive Web Content Detection", True),
    ("1.1", "Analysis of the subject area: destructive content in social networks and messengers", False),
    ("1.2", "Taxonomy and classification of destructive web content categories", False),
    ("1.3", "Review of machine-learning methods for multiclass text classification", False),
    ("1.4", "Comparative analysis of existing content-moderation solutions", False),
    ("1.5", "Conclusions for Chapter 1", False),
    ("", "", False),
    ("", "Chapter 2. Methodology and Development of the Multiclass Classification Model", True),
    ("2.1", "Formal problem statement and mathematical formulation", False),
    ("2.2", "Selection of methods, tools, and frameworks", False),
    ("2.3", "Data collection, preprocessing, and annotation pipeline", False),
    ("2.4", "Feature engineering and text representation strategies", False),
    ("2.5", "Architecture design of the multiclass classification model", False),
    ("2.6", "Training strategy, hyperparameter tuning, and regularization", False),
    ("2.7", "System architecture for deployment", False),
    ("2.8", "Conclusions for Chapter 2", False),
    ("", "", False),
    ("", "Chapter 3. Experimental Evaluation and Results", True),
    ("3.1", "Description of the dataset and experimental setup", False),
    ("3.2", "Experimental methodology and evaluation metrics", False),
    ("3.3", "Results of multiclass classification experiments", False),
    ("3.4", "Analysis and interpretation of results", False),
    ("3.5", "Comparison with existing analogues and baselines", False),
    ("3.6", "Error analysis and model interpretability", False),
    ("3.7", "Conclusions for Chapter 3", False),
    ("", "", False),
    ("", "Conclusion", False),
    ("", "References", False),
    ("", "Appendices", False),
]

for num, title, is_chapter in toc_items:
    if title == "":
        add_spacer(0.15)
        continue
    if is_chapter:
        story.append(Paragraph(
            f"<b>{title}</b>",
            ParagraphStyle("toc_ch", parent=style_body, fontSize=11, leading=15, textColor=DARK, spaceBefore=2, spaceAfter=2),
        ))
    elif num:
        story.append(Paragraph(
            f"&nbsp;&nbsp;&nbsp;&nbsp;{num}&nbsp;&nbsp;{title}",
            ParagraphStyle("toc_sec", parent=style_body, fontSize=10, leading=14, textColor=black, spaceBefore=1, spaceAfter=1, leftIndent=12),
        ))
    else:
        story.append(Paragraph(
            f"<b>{title}</b>",
            ParagraphStyle("toc_top", parent=style_body, fontSize=11, leading=15, textColor=DARK, spaceBefore=2, spaceAfter=2),
        ))

add_hr()
story.append(PageBreak())


# ── 4. CONNECTION BETWEEN CHAPTERS AND OBJECTIVES ──

h1("4. Connection Between Chapters and Research Objectives")

body(
    "The table below maps each research objective to the corresponding thesis section, "
    "the methods employed, and the expected results."
)
add_spacer(0.3)

col_widths = [1.1*cm, 3.8*cm, 3.2*cm, 3.5*cm, 4.0*cm]
header = [
    Paragraph("#", style_table_header),
    Paragraph("Research Objective", style_table_header),
    Paragraph("Thesis Section", style_table_header),
    Paragraph("Methods", style_table_header),
    Paragraph("Expected Results", style_table_header),
]

rows_data = [
    ("1", "Analyze current state of research and identify gaps",
     "1.1, 1.4", "Systematic literature review, bibliometric analysis",
     "State-of-the-art overview; identified research gaps"),
    ("2", "Define taxonomy of destructive content categories",
     "1.2", "Content analysis, expert consultation, clustering",
     "Comprehensive taxonomy of 6\u201310 content categories"),
    ("3", "Review and compare ML methods for multiclass classification",
     "1.3, 1.4", "Comparative analysis, meta-analysis",
     "Ranked list of applicable methods with pros/cons"),
    ("4", "Collect, preprocess, and annotate dataset",
     "2.3, 2.4", "Web scraping, NLP preprocessing, inter-annotator agreement",
     "Labeled multilingual dataset (10k+ samples)"),
    ("5", "Design the multiclass model architecture",
     "2.5, 2.6", "Deep learning design, transfer learning, hyperparameter optimization",
     "Model architecture specification and training pipeline"),
    ("6", "Implement model and conduct experiments",
     "3.1\u20133.4", "Cross-validation, ablation study, statistical testing",
     "Performance metrics: Accuracy, macro-F1 \u2265 0.85"),
    ("7", "Compare with existing analogues",
     "3.5", "Benchmarking, paired statistical tests",
     "Comparative table showing improvement over baselines"),
    ("8", "Formulate practical recommendations",
     "3.6, Conclusion", "Synthesis, case studies",
     "Deployment guidelines and integration recommendations"),
]

table_data = [header]
for r in rows_data:
    table_data.append([
        Paragraph(r[0], style_table_cell_c),
        Paragraph(r[1], style_table_cell),
        Paragraph(r[2], style_table_cell_c),
        Paragraph(r[3], style_table_cell),
        Paragraph(r[4], style_table_cell),
    ])

t = Table(table_data, colWidths=col_widths, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), BLUE),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 9),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ("TOPPADDING", (0, 0), (-1, 0), 8),
    ("BACKGROUND", (0, 1), (-1, -1), LIGHT_BG),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_BG, WHITE]),
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 1), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
]))
story.append(t)
story.append(PageBreak())


# ── 5. CONTENT OF EACH SECTION ──

h1("5. Content Description of Each Section")

sections = [
    ("Introduction", [
        "Relevance of the research: growth of destructive content online, limitations of current moderation.",
        "Scientific problem, goal, and objectives of the research.",
        "Object of research: destructive web content in social networks and instant messengers.",
        "Subject of research: multiclass machine-learning classification of destructive content.",
        "Methods of research (overview).",
        "Scientific novelty and practical significance.",
        "Structure of the thesis.",
    ]),
    ("Chapter 1. Theoretical Foundations of Destructive Web Content Detection", []),
    ("1.1 Analysis of the Subject Area", [
        "Definition of destructive web content and its manifestations (extremism, hate speech, cyberbullying, self-harm, fraud, disinformation).",
        "Statistics on the prevalence of destructive content in popular social networks (VK, Telegram, Instagram, TikTok) and messengers (WhatsApp, Telegram).",
        "Legal and ethical frameworks for content moderation.",
        "Key stakeholders: platforms, regulators, users, researchers.",
    ]),
    ("1.2 Taxonomy and Classification of Destructive Web Content", [
        "Existing classification schemes in the literature.",
        "Proposed taxonomy: categories (extremism, cyberbullying, self-harm promotion, fraud/phishing, disinformation, drug propaganda, explicit violence) with definitions and boundary criteria.",
        "Discussion of overlapping and ambiguous categories; multi-label vs. multiclass distinction.",
    ]),
    ("1.3 Review of ML Methods for Multiclass Text Classification", [
        "Traditional methods: SVM, Naive Bayes, Random Forest, Gradient Boosting with TF-IDF/BoW features.",
        "Deep-learning methods: CNN-text, BiLSTM, attention mechanisms.",
        "Transformer-based models: BERT, RoBERTa, XLM-R for multilingual scenarios.",
        "Ensemble and hybrid approaches.",
        "Evaluation metrics for multiclass problems: macro/micro/weighted F1, Cohen\u2019s kappa, confusion matrix analysis.",
    ]),
    ("1.4 Comparative Analysis of Existing Solutions", [
        "Review of commercial systems: Perspective API, Meta\u2019s content moderation, OpenAI moderation endpoint.",
        "Academic systems and benchmark datasets (HateXplain, Davidson et al., Jigsaw Toxic Comment).",
        "Comparison by: number of classes, languages supported, F1-score, latency, interpretability.",
        "Identified gaps and justification for the proposed approach.",
    ]),
    ("1.5 Conclusions for Chapter 1", [
        "Summary of theoretical findings; justification for the research direction.",
    ]),

    ("Chapter 2. Methodology and Development of the Multiclass Classification Model", []),
    ("2.1 Formal Problem Statement", [
        "Mathematical formulation: given input text x, predict label y \u2208 {c\u2081, c\u2082, \u2026, c\u2096} where k is the number of destructive-content categories + 1 (safe).",
        "Optimization objective: minimize cross-entropy loss over the training set.",
        "Constraints: inference time \u2264 100 ms per sample; model size suitable for deployment.",
    ]),
    ("2.2 Selection of Methods, Tools, and Frameworks", [
        "Programming language: Python 3.10+.",
        "Key libraries: PyTorch / HuggingFace Transformers, scikit-learn, pandas, NLTK/spaCy.",
        "Experiment tracking: MLflow / Weights & Biases.",
        "Hardware: GPU cluster (NVIDIA A100 or equivalent).",
        "Justification for each choice.",
    ]),
    ("2.3 Data Collection, Preprocessing, and Annotation", [
        "Data sources: public datasets (Jigsaw, HateXplain), social-media API crawling (Telegram, VK), web scraping.",
        "Preprocessing pipeline: text cleaning, normalization, language detection, deduplication.",
        "Annotation protocol: guidelines, annotator training, inter-annotator agreement (\u03ba \u2265 0.75).",
        "Data augmentation strategies: back-translation, synonym replacement, paraphrasing.",
        "Handling class imbalance: oversampling (SMOTE-text), class weights, focal loss.",
    ]),
    ("2.4 Feature Engineering and Text Representation", [
        "Baseline features: TF-IDF n-grams, linguistic features (POS, sentiment, readability).",
        "Embedding-based: Word2Vec, FastText, contextual embeddings from BERT/XLM-R.",
        "Multimodal signals (optional): metadata features (posting time, user history, URL presence).",
    ]),
    ("2.5 Architecture Design of the Multiclass Classification Model", [
        "Base model: fine-tuned XLM-RoBERTa-base (multilingual support).",
        "Classification head: linear layer with softmax for k classes.",
        "Alternative architectures explored: BiLSTM + Attention, CNN-text ensemble.",
        "Architecture diagram and detailed layer description.",
    ]),
    ("2.6 Training Strategy and Hyperparameter Tuning", [
        "Training procedure: learning rate scheduling (warm-up + cosine decay), early stopping.",
        "Hyperparameter search: Bayesian optimization over learning rate, batch size, dropout, weight decay.",
        "Regularization: dropout, label smoothing, gradient clipping.",
        "Cross-validation scheme: stratified 5-fold.",
    ]),
    ("2.7 System Architecture for Deployment", [
        "End-to-end pipeline: data ingestion \u2192 preprocessing \u2192 inference \u2192 result storage.",
        "REST API design (FastAPI), containerization (Docker), orchestration considerations.",
        "Monitoring and retraining pipeline.",
    ]),
    ("2.8 Conclusions for Chapter 2", [
        "Summary of methodological decisions and their justification.",
    ]),

    ("Chapter 3. Experimental Evaluation and Results", []),
    ("3.1 Description of the Dataset and Experimental Setup", [
        "Final dataset statistics: total samples, class distribution, language distribution.",
        "Train/validation/test split ratios (70/15/15) with stratification.",
        "Hardware and software environment for experiments.",
    ]),
    ("3.2 Experimental Methodology and Evaluation Metrics", [
        "Primary metrics: macro-F1, weighted-F1, accuracy.",
        "Secondary metrics: per-class precision, recall, confusion matrix, ROC-AUC (one-vs-rest).",
        "Statistical significance: paired bootstrap test, confidence intervals.",
        "Ablation study design: effect of preprocessing steps, features, model components.",
    ]),
    ("3.3 Results of Multiclass Classification Experiments", [
        "Performance of baseline models (SVM, Logistic Regression, Random Forest).",
        "Performance of deep-learning models (BiLSTM, CNN-text).",
        "Performance of transformer models (BERT, XLM-RoBERTa).",
        "Summary results table with all metrics.",
    ]),
    ("3.4 Analysis and Interpretation of Results", [
        "Class-level analysis: which categories are hardest to classify and why.",
        "Feature importance and attention visualization.",
        "Error patterns: common misclassifications, edge cases.",
    ]),
    ("3.5 Comparison with Existing Analogues and Baselines", [
        "Benchmark comparison on public datasets (Jigsaw, HateXplain).",
        "Comparison with commercial APIs (Perspective API).",
        "Improvement quantification: absolute and relative gains in F1.",
    ]),
    ("3.6 Error Analysis and Model Interpretability", [
        "LIME / SHAP explanations for sample predictions.",
        "Adversarial robustness testing (typos, obfuscation, code-switching).",
        "Recommendations for model improvement.",
    ]),
    ("3.7 Conclusions for Chapter 3", [
        "Summary of experimental findings and their implications.",
    ]),

    ("Conclusion", [
        "Summary of research contributions.",
        "Degree of achievement of each objective.",
        "Scientific novelty and practical significance.",
        "Limitations of the study.",
        "Directions for future research.",
    ]),
    ("References", [
        "Minimum 40\u201360 sources: journal articles, conference proceedings, standards, online resources.",
    ]),
    ("Appendices", [
        "Appendix A: Full dataset statistics and sample annotations.",
        "Appendix B: Source code of key modules.",
        "Appendix C: Additional experimental results and confusion matrices.",
        "Appendix D: Glossary of terms.",
    ]),
]

for title, items in sections:
    if title.startswith("Chapter"):
        h2(title)
        continue
    if title.startswith(("1.", "2.", "3.")):
        h3(title)
    else:
        h2(title)
    for item in items:
        body(f"\u2022 {item}", indent=True)

story.append(PageBreak())


# ── 6. LOGICAL MODEL ──

h1("6. Logical Model of the Thesis Structure")
add_spacer(0.3)

body(
    "The logical model below shows the chain of reasoning that connects "
    "the scientific problem to the final conclusions of the thesis."
)
add_spacer(0.4)

model_steps = [
    ("Scientific\nProblem",
     "Lack of effective multiclass classification\nfor destructive web content in social\nnetworks and messengers"),
    ("Goal",
     "Develop and validate a multiclass ML model\nfor detecting diverse types of\ndestructive content"),
    ("Objectives\n(8 items)",
     "O1: Literature review | O2: Taxonomy\nO3: Method comparison | O4: Dataset\nO5: Model design | O6: Experiments\nO7: Benchmarking | O8: Recommendations"),
    ("Chapters",
     "Ch 1: Theory (O1\u2013O3)\nCh 2: Methodology (O4\u2013O5)\nCh 3: Experiments (O6\u2013O8)"),
    ("Methods",
     "Literature review, NLP preprocessing,\nDeep learning, Transfer learning,\nStatistical evaluation, Benchmarking"),
    ("Results",
     "Taxonomy of destructive content,\nAnnotated dataset, Trained multiclass model,\nPerformance metrics (F1 \u2265 0.85)"),
    ("Conclusions",
     "Validated model, Practical guidelines,\nFuture research directions"),
]

model_table = []
for label, desc in model_steps:
    model_table.append([
        Paragraph(f"<b>{label}</b>", ParagraphStyle("ml", parent=style_table_cell, alignment=TA_CENTER, fontSize=9.5, textColor=WHITE)),
        Paragraph(desc.replace("\n", "<br/>"), ParagraphStyle("md", parent=style_table_cell, fontSize=9, leading=12)),
    ])
    model_table.append([
        Paragraph("\u2193", ParagraphStyle("arrow", parent=style_table_cell, alignment=TA_CENTER, fontSize=14, textColor=HIGHLIGHT)),
        Paragraph("", style_table_cell),
    ])

model_table.pop()

mt = Table(model_table, colWidths=[3.8*cm, 12.0*cm])
mt_style = []
for i in range(len(model_table)):
    if i % 2 == 0:
        mt_style.append(("BACKGROUND", (0, i), (0, i), BLUE))
        mt_style.append(("BACKGROUND", (1, i), (1, i), LIGHT_BG))
    else:
        mt_style.append(("BACKGROUND", (0, i), (-1, i), WHITE))
mt_style += [
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("GRID", (0, 0), (-1, -1), 0.3, HexColor("#dddddd")),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]
mt.setStyle(TableStyle(mt_style))
story.append(mt)

story.append(PageBreak())


# ── 7. COMMON MISTAKES AWARENESS ──

h1("7. Awareness of Common Mistakes")
add_spacer(0.2)
body("The following table lists common student mistakes and the specific measures taken in this thesis to avoid them.")
add_spacer(0.3)

mistakes_header = [
    Paragraph("Common Mistake", style_table_header),
    Paragraph("How It Is Avoided in This Thesis", style_table_header),
]
mistakes_rows = [
    ("Lack of connection between the structure and research objectives",
     "Every section is explicitly mapped to one or more research objectives (see Section 4). The table of contents was designed objectives-first."),
    ("Overly general section titles",
     "Section titles are specific and reflect concrete research activities (e.g., \u201cTaxonomy and Classification of Destructive Web Content Categories\u201d instead of \u201cLiterature Review\u201d)."),
    ("Inconsistency between practical and theoretical parts",
     "Chapter 1 provides the theoretical justification for every method used in Chapters 2\u20133. The comparative analysis in 1.4 directly motivates the design decisions in 2.5."),
    ("Duplication of content",
     "Each section has a clearly defined scope. Conclusions at the end of each chapter summarize without repeating body text. Cross-references are used instead of duplication."),
]
m_data = [mistakes_header]
for mistake, avoidance in mistakes_rows:
    m_data.append([
        Paragraph(mistake, style_table_cell),
        Paragraph(avoidance, style_table_cell),
    ])

m_table = Table(m_data, colWidths=[7.0*cm, 9.6*cm], repeatRows=1)
m_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), HIGHLIGHT),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (0, 1), (-1, -1), LIGHT_BG),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_BG, WHITE]),
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(m_table)

add_spacer(1.0)
add_hr()
add_spacer(0.3)
story.append(Paragraph(
    "<b>Prepared by:</b> Didar Kanalbay &nbsp;&nbsp;|&nbsp;&nbsp; <b>Group:</b> SIS-2224",
    ParagraphStyle("footer", parent=style_body, alignment=TA_CENTER, fontSize=10),
))
add_spacer(0.2)
story.append(Paragraph(
    "Practical Work &#8470; 7\u20138 &mdash; Designing the Structure of a Thesis and the Logic of Scientific Research",
    ParagraphStyle("footer2", parent=style_body, alignment=TA_CENTER, fontSize=9, textColor=BLUE),
))


doc.build(story)
print("PDF generated: Practical_Work_7_8_Didar_Kanalbay.pdf")

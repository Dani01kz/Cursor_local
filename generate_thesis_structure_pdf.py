#!/usr/bin/env python3
"""
Generate PDF for Practical Work No. 7-8: Thesis Structure Design
Topic: Creating a multiclass model for detecting destructive web content
"""

from fpdf import FPDF
from datetime import datetime


class ThesisStructurePDF(FPDF):
    def header(self):
        self.set_font('Helvetica', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Practical Work No. 7-8: Thesis Structure Design', 0, 1, 'C')
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def section_title(self, text):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, text, 0, 'L')
        self.ln(2)

    def subsection_title(self, text):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 7, text, 0, 'L')
        self.ln(1)

    def subsubsection_title(self, text):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text, 0, 'L')
        self.ln(1)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text, 0, 'L')
        self.ln(2)

    def bullet_point(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(0, 0, 0)
        self.cell(5)
        self.multi_cell(0, 6, f'- {text}', 0, 'L')
        self.ln(0.5)


def create_pdf():
    pdf = ThesisStructurePDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Title Page
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 15, 'PRACTICAL WORK No. 7-8', 0, 1, 'C')
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 8, 'Topic: Designing the Structure of a Thesis and the Logic of Scientific Research', 0, 1, 'C')
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, 'Student: Didar Kanalbay', 0, 1, 'C')
    pdf.cell(0, 8, 'Group: sis-2224', 0, 1, 'C')
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.multi_cell(0, 6, 'Thesis Topic: Creating a multiclass model for detecting destructive web content in social networks and instant messengers using machine learning', 0, 'C')
    pdf.ln(10)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, f'Date: {datetime.now().strftime("%B %d, %Y")}', 0, 1, 'C')

    pdf.add_page()

    # 1. Complete Table of Contents
    pdf.section_title('1. COMPLETE TABLE OF CONTENTS')
    pdf.body_text('Introduction')
    pdf.body_text('Chapter 1. Theoretical Foundations of the Research')
    pdf.bullet_point('1.1 Analysis of the subject area')
    pdf.bullet_point('1.2 Review of methods and approaches')
    pdf.bullet_point('1.3 Comparative analysis of existing solutions')
    pdf.bullet_point('1.4 Conclusions for the chapter')
    pdf.body_text('Chapter 2. Methodology and Development of the Solution')
    pdf.bullet_point('2.1 Problem statement')
    pdf.bullet_point('2.2 Selection of methods and tools')
    pdf.bullet_point('2.3 Development of a model / algorithm')
    pdf.bullet_point('2.4 System architecture')
    pdf.bullet_point('2.5 Conclusions for the chapter')
    pdf.body_text('Chapter 3. Experimental Part')
    pdf.bullet_point('3.1 Description of data and experiment')
    pdf.bullet_point('3.2 Experimental methodology')
    pdf.bullet_point('3.3 Results')
    pdf.bullet_point('3.4 Analysis of results')
    pdf.bullet_point('3.5 Comparison with analogues')
    pdf.bullet_point('3.6 Conclusions for the chapter')
    pdf.body_text('Conclusion')
    pdf.body_text('References')
    pdf.body_text('Appendices')

    pdf.add_page()

    # 2. Connection between chapters and research objectives
    pdf.section_title('2. CONNECTION BETWEEN CHAPTERS AND RESEARCH OBJECTIVES')
    pdf.subsection_title('Research Objectives (defined for the thesis topic):')
    objectives = [
        'O1: To analyze the subject area of destructive web content in social networks and messengers',
        'O2: To study and compare existing methods and approaches for content classification',
        'O3: To develop a multiclass classification model for detecting destructive content',
        'O4: To implement and experimentally validate the proposed solution',
        'O5: To compare the developed model with existing analogues'
    ]
    for obj in objectives:
        pdf.bullet_point(obj)
    pdf.ln(3)
    pdf.subsection_title('Mapping: Research Objective -> Thesis Chapter')
    pdf.body_text('Objective O1 -> Chapter 1 (Sections 1.1, 1.2)')
    pdf.body_text('Objective O2 -> Chapter 1 (Sections 1.2, 1.3)')
    pdf.body_text('Objective O3 -> Chapter 2 (Sections 2.2, 2.3, 2.4)')
    pdf.body_text('Objective O4 -> Chapter 3 (Sections 3.1-3.4)')
    pdf.body_text('Objective O5 -> Chapter 3 (Section 3.5)')

    pdf.add_page()

    # 3. Table linking objectives and structure
    pdf.section_title('3. TABLE LINKING OBJECTIVES AND STRUCTURE')
    pdf.set_font('Helvetica', '', 9)
    col_widths = [35, 55, 55, 45]
    headers = ['Research objective', 'Thesis section', 'Methods', 'Expected results']
    for col, header in zip(col_widths, headers):
        pdf.cell(col, 8, header, 1, 0, 'C')
    pdf.ln()
    rows = [
        ('O1', 'Ch.1 1.1, 1.2', 'Literature review, analysis', 'Taxonomy of destructive content'),
        ('O2', 'Ch.1 1.2, 1.3', 'Comparative analysis', 'Overview of ML approaches'),
        ('O3', 'Ch.2 2.2-2.4', 'ML modeling, design', 'Multiclass model architecture'),
        ('O4', 'Ch.3 3.1-3.4', 'Experiments, metrics', 'Performance metrics'),
        ('O5', 'Ch.3 3.5', 'Benchmarking', 'Comparison table')
    ]
    for row in rows:
        for col, val in zip(col_widths, row):
            pdf.cell(col, 7, val, 1, 0, 'L')
        pdf.ln()
    pdf.ln(5)
    pdf.set_font('Helvetica', '', 10)

    # 4. Content of each section
    pdf.section_title('4. CONTENT OF EACH SECTION')
    pdf.subsection_title('Introduction')
    pdf.body_text('Relevance of the problem; scientific novelty; goal and objectives; research methods; structure of the thesis.')
    pdf.subsection_title('Chapter 1. Theoretical Foundations')
    pdf.subsubsection_title('1.1 Analysis of the subject area')
    pdf.body_text('Types of destructive content (hate speech, extremism, cyberbullying, misinformation, etc.); characteristics of social networks and messengers; legal and ethical aspects.')
    pdf.subsubsection_title('1.2 Review of methods and approaches')
    pdf.body_text('Supervised learning for text classification; NLP techniques (tokenization, embeddings); deep learning (CNN, RNN, Transformers); multiclass classification approaches.')
    pdf.subsubsection_title('1.3 Comparative analysis of existing solutions')
    pdf.body_text('Review of academic and industrial solutions; comparison of accuracy, interpretability, and scalability.')
    pdf.subsubsection_title('1.4 Conclusions for the chapter')
    pdf.body_text('Summary of findings; justification for the chosen approach.')

    pdf.add_page()

    pdf.subsection_title('Chapter 2. Methodology and Development')
    pdf.subsubsection_title('2.1 Problem statement')
    pdf.body_text('Formal statement of the multiclass classification problem; definition of classes of destructive content; requirements for the model.')
    pdf.subsubsection_title('2.2 Selection of methods and tools')
    pdf.body_text('Choice of ML framework (e.g., scikit-learn, PyTorch); selection of preprocessing and feature extraction methods.')
    pdf.subsubsection_title('2.3 Development of a model / algorithm')
    pdf.body_text('Description of the multiclass model architecture; training and validation procedure; hyperparameter tuning.')
    pdf.subsubsection_title('2.4 System architecture')
    pdf.body_text('Pipeline for data ingestion, preprocessing, inference; integration with social network/messenger APIs.')
    pdf.subsubsection_title('2.5 Conclusions for the chapter')
    pdf.body_text('Summary of the developed solution.')

    pdf.subsection_title('Chapter 3. Experimental Part')
    pdf.subsubsection_title('3.1 Description of data and experiment')
    pdf.body_text('Datasets used (e.g., Hate Speech, Jigsaw, custom datasets); data preprocessing; train/validation/test split.')
    pdf.subsubsection_title('3.2 Experimental methodology')
    pdf.body_text('Evaluation metrics (accuracy, F1, macro/weighted); cross-validation; experimental setup.')
    pdf.subsubsection_title('3.3 Results')
    pdf.body_text('Tables and figures with experimental results.')
    pdf.subsubsection_title('3.4 Analysis of results')
    pdf.body_text('Interpretation of results; error analysis; discussion.')
    pdf.subsubsection_title('3.5 Comparison with analogues')
    pdf.body_text('Comparison with baseline and state-of-the-art methods.')
    pdf.subsubsection_title('3.6 Conclusions for the chapter')
    pdf.body_text('Summary of experimental findings.')

    pdf.add_page()

    # 5. Logical model
    pdf.section_title('5. LOGICAL MODEL OF THE THESIS STRUCTURE')
    pdf.body_text('Scientific problem -> Goal -> Objectives -> Chapters -> Methods -> Results -> Conclusions')
    pdf.ln(3)
    pdf.subsection_title('Applied to the thesis topic:')
    pdf.body_text('Scientific problem: Proliferation of destructive content in social networks and messengers threatens user safety and requires automated detection.')
    pdf.body_text('Goal: To create an effective multiclass model for detecting destructive web content using machine learning.')
    pdf.body_text('Objectives: O1-O5 (as defined above).')
    pdf.body_text('Chapters: Ch.1 (theory) -> Ch.2 (methodology) -> Ch.3 (experiments).')
    pdf.body_text('Methods: Literature review, comparative analysis, ML modeling, experimental validation.')
    pdf.body_text('Results: Trained model, performance metrics, comparison with analogues.')
    pdf.body_text('Conclusions: Validation of the approach; recommendations for practical use.')

    pdf.add_page()

    # 6. Avoiding common mistakes
    pdf.section_title('6. AVOIDING COMMON MISTAKES')
    pdf.body_text('- Ensure each chapter directly addresses at least one research objective.')
    pdf.body_text('- Use specific section titles (e.g., "Multiclass classification using BERT" instead of "Methods").')
    pdf.body_text('- Align practical experiments (Ch.3) with the model developed in Ch.2.')
    pdf.body_text('- Avoid duplicating content between theoretical review and methodology.')

    pdf.output('/workspace/Practical_Work_7-8_Thesis_Structure_Didar_Kanalbay.pdf')
    print('PDF generated: Practical_Work_7-8_Thesis_Structure_Didar_Kanalbay.pdf')


if __name__ == '__main__':
    create_pdf()

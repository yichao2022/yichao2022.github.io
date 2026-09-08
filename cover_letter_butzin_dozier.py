#!/usr/bin/env python3
"""Generate cover letter PDF for Zachary Butzin-Dozier postdoc position."""

from fpdf import FPDF
import os

class CoverLetterPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = CoverLetterPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=25)
pdf.add_page()

# ── Letterhead ──
pdf.set_font('Helvetica', '', 11)
pdf.cell(0, 5.5, 'Yichao Jin', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 4.5, 'PhD in Economics, UT Dallas', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 4.5, 'Email: yichao.jin@utdallas.edu  |  Phone: (682) 266-4185', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 4.5, 'Dallas, TX', new_x='LMARGIN', new_y='NEXT')

# Date
pdf.ln(6)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.cell(0, 5, 'July 8, 2026', new_x='LMARGIN', new_y='NEXT')

pdf.ln(4)

# Recipient
pdf.cell(0, 5, 'Dr. Zachary Butzin-Dozier', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 5, 'Assistant Professor of Pediatrics (Clinical Informatics)', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 5, 'and of Medicine (Computational Medicine)', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 5, 'Stanford University School of Medicine', new_x='LMARGIN', new_y='NEXT')

pdf.ln(3)

# Subject
pdf.set_font('Helvetica', 'B', 10)
pdf.cell(0, 6, 'Re: Postdoctoral Position in Causal Inference and EHR Research', new_x='LMARGIN', new_y='NEXT')

pdf.ln(4)

# ── Body ──
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(0, 0, 0)

paragraphs = [
    "Dear Dr. Butzin-Dozier,",

    "I am writing to apply for the postdoctoral position in your lab advertised through "
    "the Stanford Division of Clinical Informatics. I recently completed my PhD in Economics "
    "at UT Dallas with a focus on causal inference and machine learning in health decision-making, "
    "and I believe my methodological background aligns closely with the research program you are building.",

    "My recent research developed an Empirical-Frontier Regularization (EFR) framework that integrates "
    "machine learning with behavioral consistency constraints -- essentially a method to audit and "
    "calibrate LLM-generated health preference predictions against empirical benchmarks. This work "
    "sits at the intersection of causal inference, machine learning, and observational health data, "
    "which is also the core of your research on targeted machine learning for EHR-based causal effect "
    "estimation in Long COVID.",

    "Your work applying targeted machine learning to the N3C -- evaluating protective interventions "
    "like SSRIs and metformin against Long COVID -- is a natural ground to extend my methods. "
    "The EFR framework's logic of imposing behavioral and statistical constraints on data-driven "
    "predictions translates directly to the problem of drawing reliable causal inferences from complex, "
    "high-dimensional EHR data. I am particularly interested in exploring how targeted learning and "
    "super learner ensembles (which I have used in my own work) can be combined with regularization "
    "approaches to improve the robustness of treatment effect estimates in heterogeneous patient populations.",

    "Beyond my methodological work, I have extensive experience with discrete choice experiments and "
    "health preference modeling, which I see as complementary to EHR-based research -- DCE data "
    "captures patient preferences that are invisible in clinical records, and linking these two data "
    "types could deepen your program's understanding of patient-centered outcomes. I also hold a "
    "Master's in Statistics and Data Analytics, giving me strong computational foundations in "
    "R and Python.",

    "I am available to start as early as August 2026 and have current work authorization through my "
    "F-1 visa. My CV is attached. I would welcome the opportunity to discuss how "
    "my background might contribute to the research directions you are developing in your new lab.",

    "Best regards,",
    "Yichao Jin"
]

for p in paragraphs:
    pdf.multi_cell(0, 5.2, p)
    pdf.ln(2)

# ── Output ──
output_path = '/Users/cary/yichao2022_repo/cover_letter_butzin_dozier.pdf'
pdf.output(output_path)
print(f'OK: {output_path}')
print(f'Size: {os.path.getsize(output_path)} bytes')

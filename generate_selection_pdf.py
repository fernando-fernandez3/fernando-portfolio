from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER

def create_selection_pdf():
    doc = SimpleDocTemplate(
        "content_selection.pdf",
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER
    )

    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=10,
        textColor=colors.HexColor('#D4652A')
    )

    option_style = ParagraphStyle(
        'OptionTitle',
        parent=styles['Heading3'],
        fontSize=12,
        spaceBefore=12,
        spaceAfter=4,
        leftIndent=20
    )

    content_style = ParagraphStyle(
        'ContentText',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=40,
        rightIndent=20,
        spaceAfter=8,
        leading=14
    )

    checkbox_style = ParagraphStyle(
        'Checkbox',
        parent=styles['Normal'],
        fontSize=14,
        leftIndent=0
    )

    instructions_style = ParagraphStyle(
        'Instructions',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=20,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER
    )

    story = []

    # Title
    story.append(Paragraph("Fernando Portfolio - Content Selection", title_style))
    story.append(Paragraph("Circle your favorite option for each section", instructions_style))
    story.append(Spacer(1, 0.3*inch))

    # ============ SECTION 1: BADGE/TAGLINE ============
    story.append(Paragraph("1. BADGE / OPENING TAGLINE", section_style))
    story.append(Paragraph("The small text that appears above your name", instructions_style))

    badges = [
        ("A", "From Wrench to Code"),
        ("B", "Staff Engineer at Tesla"),
        ("C", "Mechanic turned engineer"),
        ("D", "Available for Opportunities"),
        ("E", "From automotive technician to software engineer"),
        ("NEW", "Self-taught engineer. Mechanic turned developer."),
    ]

    for opt, text in badges:
        story.append(Paragraph(f"[ ] Option {opt}:", option_style))
        story.append(Paragraph(f'"{text}"', content_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("[ ] Write your own: _________________________________________________", content_style))

    # ============ SECTION 2: HEADLINE ============
    story.append(PageBreak())
    story.append(Paragraph("2. HEADLINE / NAME PRESENTATION", section_style))
    story.append(Paragraph("How your name appears in the hero section", instructions_style))

    headlines = [
        ("A", "Fernando<br/>Fernandez", "(Two lines, serif font, last name highlighted)"),
        ("B", "From the Shop Floor to<br/>Software.", "(Story-focused, action words)"),
        ("C", "FERNANDO<br/>FERNANDEZ", "(All caps, bold, gold accent)"),
        ("D", "Fernando Fernandez", "(Single line, elegant)"),
        ("E", "Fernando<br/>Fernandez", "(Two lines, gradient accent on last name)"),
        ("F", "Building systems that<br/>save millions", "(Impact-focused, not your name)"),
    ]

    for opt, text, note in headlines:
        story.append(Paragraph(f"[ ] Option {opt}: {note}", option_style))
        story.append(Paragraph(text.replace('<br/>', ' / '), content_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("[ ] Write your own: _________________________________________________", content_style))

    # ============ SECTION 3: SUBTITLE ============
    story.append(PageBreak())
    story.append(Paragraph("3. HERO SUBTITLE / INTRO", section_style))
    story.append(Paragraph("The paragraph that appears below your name", instructions_style))

    subtitles = [
        ("A", "An automotive technician who taught himself to code, now building diagnostic systems that serve thousands of technicians at Tesla."),
        ("C", "Mechanic turned engineer. Building systems that matter."),
        ("D", "Staff Product Support Engineer at Tesla. I build diagnostic automation systems that have saved $12.8 million and reduced repair times by 38%."),
        ("E", "From automotive technician to software engineer. I build systems that automate diagnostics and save millions."),
        ("LONG", "A self-taught engineer who went from automotive technician to building diagnostic automation systems at Tesla. My work has generated $12.8M in documented savings."),
    ]

    for opt, text in subtitles:
        story.append(Paragraph(f"[ ] Option {opt}:", option_style))
        story.append(Paragraph(text, content_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("[ ] Write your own: _________________________________________________", content_style))
    story.append(Paragraph("_________________________________________________", content_style))

    # ============ SECTION 4: ABOUT PARAGRAPH ============
    story.append(PageBreak())
    story.append(Paragraph("4. ABOUT ME PARAGRAPH", section_style))
    story.append(Paragraph("The longer description of your journey", instructions_style))

    abouts = [
        ("SHORT", "I spent years as an automotive technician, diagnosing problems by sound and instinct. Taught myself Python through YouTube tutorials. Now I build diagnostic automation systems at Tesla that have saved $12.8 million and reduced repair times by 38%."),
        ("MEDIUM", "I started my career as an automotive technician, diagnosing engine problems by sound and instinct. Every engine told a story. I taught myself Python through YouTube tutorials after work. That curiosity led me from the shop floor to Staff Product Support Engineer at Tesla, where I now build the diagnostic automation systems that help technicians work smarter."),
        ("TEXAS", "I started my career as an automotive technician, diagnosing engine problems by sound and instinct. Every engine told a story. I taught myself Python through YouTube tutorials after work. That curiosity led me from the shop floor to Staff Product Support Engineer at Tesla, where I now build the diagnostic automation systems that help technicians work smarter. Based in Texas, I bring a unique perspective—hands-on problem solving, slow-smoked brisket on weekends, and the grit to run 26.2 miles."),
    ]

    for opt, text in abouts:
        story.append(Paragraph(f"[ ] Option {opt}:", option_style))
        story.append(Paragraph(text, content_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("[ ] Write your own: _________________________________________________", content_style))
    story.append(Paragraph("_________________________________________________", content_style))

    # ============ SECTION 5: TIMELINE STYLE ============
    story.append(PageBreak())
    story.append(Paragraph("5. TIMELINE / JOURNEY STYLE", section_style))
    story.append(Paragraph("How to present your career progression", instructions_style))

    timelines = [
        ("E - FULL", "Full detailed timeline from high school to present with milestones, company names, and descriptions for each role"),
        ("A - SIMPLE", "Brief 'From Wrench to Code' narrative without detailed timeline"),
        ("J - TERMINAL", "CLI-style career progression (neofetch output format)"),
        ("F - CARDS", "Project-focused cards showing impact rather than chronological timeline"),
    ]

    for opt, text in timelines:
        story.append(Paragraph(f"[ ] {opt}:", option_style))
        story.append(Paragraph(text, content_style))

    # ============ SECTION 6: METRICS DISPLAY ============
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("6. METRICS / IMPACT DISPLAY", section_style))
    story.append(Paragraph("How to show your quantifiable achievements", instructions_style))

    metrics_options = [
        ("PROMINENT", "Large metrics in hero section: $12.8M | 38% | 7,500+"),
        ("CARDS", "Individual project cards with specific impact per project"),
        ("SUBTLE", "Woven into prose (e.g., 'saved $12.8M' in paragraph)"),
        ("BADGE", "Stats bar format: '7,500+ automations | 105+ stakeholders | 11+ years'"),
    ]

    for opt, text in metrics_options:
        story.append(Paragraph(f"[ ] {opt}:", option_style))
        story.append(Paragraph(text, content_style))

    # ============ SECTION 7: BBQ BADGE ============
    story.append(PageBreak())
    story.append(Paragraph("7. BBQ BADGE / PERSONAL TOUCH", section_style))
    story.append(Paragraph("How prominent should the BBQ achievement be?", instructions_style))

    bbq_options = [
        ("PROMINENT", "Badge in hero section: '2x Backyard Brisket Competition Winner'"),
        ("SECTION", "Separate 'Personal Interests' section with BBQ, Marathon, Texas"),
        ("SUBTLE", "Brief mention in about paragraph ('slow-smoked brisket on weekends')"),
        ("NONE", "Skip it for professional version"),
    ]

    for opt, text in bbq_options:
        story.append(Paragraph(f"[ ] {opt}:", option_style))
        story.append(Paragraph(text, content_style))

    # ============ SECTION 8: CTA / CONTACT ============
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("8. CONTACT / CALL TO ACTION", section_style))
    story.append(Paragraph("How to invite visitors to reach out", instructions_style))

    cta_options = [
        ("A", "Let's Connect"),
        ("B", "Let's Talk"),
        ("C", "Get in Touch"),
        ("D", "Start a Conversation"),
    ]

    for opt, text in cta_options:
        story.append(Paragraph(f"[ ] {opt}: '{text}'", option_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Contact description options:", option_style))

    contact_descs = [
        ("1", "Always open to interesting conversations about tech, BBQ, or marathon training."),
        ("2", "Open to conversations about engineering, career transitions, or competitive BBQ."),
        ("3", "Interested in discussing engineering, career transitions, or BBQ."),
        ("4", "Open to discussing engineering, automation, or BBQ techniques."),
    ]

    for opt, text in contact_descs:
        story.append(Paragraph(f"[ ] {opt}: {text}", content_style))

    # ============ SECTION 9: SPECIAL ELEMENTS ============
    story.append(PageBreak())
    story.append(Paragraph("9. SPECIAL ELEMENTS (Check all you want)", section_style))

    special = [
        "Sensor demo animation (shows technical skills visually)",
        "Photo placeholder (for future headshot)",
        "Marathon time display (4:29:46)",
        "Skills/Languages list",
        "Social links (LinkedIn, GitHub, X)",
        "ASE Master Technician certification mention",
        "'Available for Opportunities' indicator",
    ]

    for item in special:
        story.append(Paragraph(f"[ ] {item}", content_style))

    # ============ NOTES SECTION ============
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph("NOTES / ADDITIONAL THOUGHTS", section_style))
    story.append(Spacer(1, 0.1*inch))
    for _ in range(8):
        story.append(Paragraph("_" * 80, content_style))
        story.append(Spacer(1, 0.15*inch))

    # Build PDF
    doc.build(story)
    print("PDF created: content_selection.pdf")

if __name__ == "__main__":
    create_selection_pdf()

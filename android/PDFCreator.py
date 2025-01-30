from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Register custom fonts
pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold', 'timesbd.ttf'))

def create_resume_pdf(file_name):
    # Create a document with specified margins (0.39 inches = 28.08 points)
    doc = SimpleDocTemplate(file_name, pagesize=A4, rightMargin=28.08, leftMargin=28.08, topMargin=28.08, bottomMargin=28.08)

    # Styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'], fontName='TimesNewRoman-Bold', fontSize=16, alignment=1, spaceAfter=12, textColor=colors.HexColor("#000000")
    )
    subtitle_style = ParagraphStyle(
        'SubtitleStyle', parent=styles['Normal'], fontName='TimesNewRoman', fontSize=11, textColor=colors.HexColor("#000000"), alignment=1, spaceAfter=8
    )
    contact_style = ParagraphStyle(
        'ContactStyle', parent=styles['Normal'], fontName='TimesNewRoman', fontSize=11, textColor=colors.HexColor("#000000"), alignment=1, leading=13
    )
    section_header_style = ParagraphStyle(
        'SectionHeader', parent=styles['Heading2'], fontName='TimesNewRoman-Bold', fontSize=12, textColor=colors.HexColor("#000000"), spaceBefore=12, underlineWidth=0.5, leading=13
    )
    body_style = ParagraphStyle(
        'BodyStyle', parent=styles['Normal'], fontName='TimesNewRoman', fontSize=11, leading=14, textColor=colors.HexColor("#000000"), spaceAfter=6
    )
    bullet_style = ParagraphStyle(
        'BulletStyle', parent=body_style, leftIndent=15, bulletIndent=10, bulletFontName='TimesNewRoman', bulletFontSize=11
    )

    # Content
    content = []

    # Header
    content.append(Paragraph("Nishant Tanwar", title_style))
    content.append(Paragraph("Sr. Software Engineer", subtitle_style))
    contact_info = "<b>+91-8800927423</b> ◇ <a href='mailto:nishantt21@gmail.com'>nishantt21@gmail.com</a> ◇ New Delhi, Delhi, 110027, India ◇ <a href='https://www.linkedin.com/in/nishantt12'>LinkedIn</a> ◇ <a href='https://github.com/nishantt12'>GitHub</a>"
    content.append(Paragraph(contact_info, contact_style))
    content.append(Spacer(1, 12))

    # Summary
    content.append(Paragraph("SUMMARY", section_header_style))
    summary = ("With over 10 years of professional experience, I am a seasoned Software Engineer proficient in a range of "
               "technologies including Android, Kotlin, Java, Jetpack Compose, Kubernetes, Google Cloud Platform, AWS, and Microservices. "
               "Throughout the years, I have contributed to diverse domains such as Supply Chain, Service Marketplaces, and Financial Services. "
               "I am passionate about creating impactful solutions that drive meaningful change.")
    content.append(Paragraph(summary, body_style))
    content.append(Spacer(1, 12))

    # Experience
    content.append(Paragraph("EXPERIENCE", section_header_style))

    experiences = [
        {
            "role": "Sr. Software Engineer",
            "company": "Tala",
            "dates": "Jun '22 — Present",
            "location": "Remote",
            "details": [
                "Led development of the Tala Android Application from inception to launch, resulting in over 20+ Million downloads on the Google Play Store.",
                "Implemented dynamic features in the app which boosted user interaction by 20%.",
                "Integrated Server-Driven UI framework with Jetpack compose which reduced app size by 25%.",
                "Led the development of an in-house wallet with server-side API integration.",
                "Implemented cross-platform multi-country module to deploy applications into multiple countries (Philippines, India, Mexico, and Kenya)."
            ]
        },
        {
            "role": "Sr. Software Engineer",
            "company": "MileZero, a Capstone Company",
            "dates": "Jan '16 — May '22",
            "location": "Remote",
            "details": [
                "Architected and developed the Last Mile Android Application to deliver 1+ Million packages daily.",
                "Developed a framework enabling the app to function fully offline, reducing user drop rate by 40%.",
                "Reduced build time and app size by dividing the complete application into smaller, independent modules.",
                "Completely migrated the app from MVP to MVVM architecture, improving code maintainability and testability while streamlining UI logic and state management.",
                "Implemented Jenkins CI/CD pipelines for automated testing and deployment of the app to the Google Play Store."
            ]
        },
    ]

    for exp in experiences:
        content.append(Paragraph(f"<b>{exp['role']}</b>, {exp['company']} ({exp['dates']}, {exp['location']})", body_style))
        for detail in exp['details']:
            content.append(Paragraph(f"•  {detail}", bullet_style))
        content.append(Spacer(1, 6))

    # Skills, Education, and Certifications
    content.append(Paragraph("SKILLS", section_header_style))
    content.append(Paragraph("Kotlin, Java, Python, Node.js, Rx-Java, XML, Android, Kubernetes, AWS, etc.", body_style))

    content.append(Paragraph("EDUCATION", section_header_style))
    content.append(Paragraph("Bachelor of Technology, GGSIPU, New Delhi, India", body_style))

    content.append(Paragraph("CERTIFICATIONS", section_header_style))
    content.append(Paragraph("Oracle Certified Expert - Java (Jan '11)<br/>Coursera Machine Learning (Mar '22)", body_style))

    # Build PDF
    doc.build(content)

# Usage
create_resume_pdf("Nishant_Tanwar_Resume.pdf")

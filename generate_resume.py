#!/usr/bin/env python3
"""Generate Devakkumar Sheth resume PDF."""
import shutil
from fpdf import FPDF


class ResumePDF(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, "Devakkumar Sheth - Resume", align="C")

    def section_title(self, title):
        self.ln(3)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(99, 102, 241)
        self.cell(0, 7, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(99, 102, 241)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def para(self, text, size=9.5, line_h=5):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", size)
        self.set_text_color(50, 50, 70)
        self.multi_cell(0, line_h, text)

    def bullet(self, text, size=9, line_h=4.8):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", size)
        self.set_text_color(60, 60, 80)
        self.multi_cell(0, line_h, f"  - {text}")

    def entry_header(self, title, date):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(26, 26, 46)
        self.multi_cell(0, 5, title)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(120, 120, 140)
        self.cell(0, 4, date, new_x="LMARGIN", new_y="NEXT")


pdf = ResumePDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()
pdf.set_margins(20, 20, 20)

pdf.set_x(pdf.l_margin)
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(26, 26, 46)
pdf.cell(0, 10, "DEVAKKUMAR SHETH", new_x="LMARGIN", new_y="NEXT")

pdf.set_x(pdf.l_margin)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(99, 102, 241)
pdf.cell(0, 6, "Associated Software Developer | Backend", new_x="LMARGIN", new_y="NEXT")

pdf.para("+91 9408999494 | 223csd11@svitvasad.ac.in | Vadodara, Gujarat", 8.5, 4.5)
pdf.para("github.com/Shethdevak | linkedin.com/in/devakkumar-sheth-7159313a0", 8.5, 4.5)
pdf.ln(2)
pdf.set_draw_color(99, 102, 241)
pdf.set_line_width(0.6)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(4)

pdf.section_title("Professional Summary")
pdf.para(
    "Goal-driven B.E. Computer Science and Design graduate with strong AI/ML foundations "
    "and hands-on software development experience. Currently backend developer on a "
    "Frappe/ERPNext healthcare ERP at Digiflux Technologies. Skilled in full-stack web "
    "and mobile apps, REST APIs, scraping pipelines, and production dashboards."
)

pdf.section_title("Experience")
entries = [
    ("Associated Software Developer - Backend", "Jun 2026 - Present", "Digiflux Technologies Pvt. Ltd.", [
        "Backend developer on FRS TB Screening, a Frappe/ERPNext ERP for TB screening",
        "Mobile REST APIs for enumeration, assessments, campaigns and specimen workflows",
        "X-Ray via Qure AI, sputum testing, QR identification, geospatial areas (Shapely)",
        "Nikshay registry integration, DICOM upload, and QR PDF generation",
    ]),
    ("Software Developer Intern", "Dec 2025 - Jun 2026", "Digiflux Technologies Pvt. Ltd.", [
        "Built and deployed Eventix, DebugPilot, MarketIQ, and SeatNova on Vercel",
        "Production REST APIs with Node.js, Express, and MongoDB for asset management",
        "React Native (Expo) and Kotlin mobile apps; Python e-commerce scrapers",
        "ComfyUI AI workflows and e-commerce front-ends for Mixa platform",
    ]),
    ("AI Summer Internship", "Jun 2025 (2 Weeks)", "IBM SkillsBuild", [
        "Machine learning workflows, ethical AI, and problem-solving using AI tools",
    ]),
]
for title, date, org, bullets in entries:
    pdf.entry_header(title, date)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(99, 102, 241)
    pdf.multi_cell(0, 5, org)
    for b in bullets:
        pdf.bullet(b)
    pdf.ln(1)

pdf.section_title("Key Projects")
projects = [
    ("FRS TB Screening ERP (Current)", "Frappe, ERPNext, Python, MariaDB, Redis, Shapely", [
        "40+ custom DocTypes with mobile APIs for Flutter and Nikshay integration",
    ]),
    ("Eventix - Event Booking", "Node.js, React, React Native, Kotlin, MongoDB, Razorpay", [
        "JWT, RBAC, seat locking, Razorpay; web, mobile and Android clients on Vercel",
    ]),
    ("Digiflux AssetTrack", "Node.js, MongoDB, Next.js, TypeScript", [
        "Production IT asset system with RBAC, alerts, QR codes; 32/32 API tests passed",
    ]),
    ("DebugPilot, MarketIQ, SeatNova, Scrapers, Railway Dashboard", "Next.js, React Native, Flask, Python", [
        "API debugger, AI marketplace, venue builder, Mixa scrapers, government dashboards",
    ]),
    ("AI World - Gesture Control", "Python, OpenCV, MediaPipe", [
        "Hands-free computer control via webcam hand gestures",
    ]),
]
for name, tech, bullets in projects:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(26, 26, 46)
    pdf.multi_cell(0, 5, name)
    pdf.para(tech, 8, 4.2)
    for b in bullets:
        pdf.bullet(b, 8.5, 4.5)
    pdf.ln(1)

pdf.section_title("Education")
pdf.para("B.E. Computer Science and Design - SVIT Vasad (GTU)", 9, 4.8)
pdf.para("2023-2026 | CGPA: 8.29 | CPI: 7.74", 8.5, 4.5)
pdf.para("Diploma in Information Technology - Sigma Group of Institutes (GTU)", 9, 4.8)
pdf.para("2020-2023 | CGPA: 7.57 | CPI: 8.07", 8.5, 4.5)

pdf.section_title("Skills")
for line in [
    "Languages: Python, JavaScript, TypeScript, Java, Kotlin, C, C++",
    "Backend: Node.js, Express, Frappe, ERPNext, Flask, REST API, JWT, RBAC",
    "Frontend: React, Next.js, React Native, Tailwind CSS, Three.js",
    "Databases: MongoDB, PostgreSQL, MariaDB, Redis, SQLite",
    "AI/ML: NumPy, Pandas, Scikit-learn, TensorFlow, OpenCV, MediaPipe",
    "Tools: Git, GitHub, GitLab, Vercel, Docker, Postman, ComfyUI",
]:
    pdf.para(line, 8.5, 4.5)

pdf.section_title("Languages")
pdf.para("Gujarati (Fluent) | Hindi (Fluent) | English (Intermediate)", 9)

pdf.output("Devakkumar_Sheth_Resume.pdf")
shutil.copy("Devakkumar_Sheth_Resume.pdf", "resume.pdf")
print("Created Devakkumar_Sheth_Resume.pdf and resume.pdf")

import os
import re
from PyPDF2 import PdfReader


KNOWN_SKILLS = [
    "Python",
    "Java",
    "SQL",
    "Docker",
    "Git",
    "HTML",
    "CSS",
    "JavaScript"
]


def extract_resume(pdf_path):
    """
    Extract information from a single PDF resume.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Name (first non-empty line)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    full_name = lines[0] if lines else ""

    # Email
    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    email = email_match.group() if email_match else None

    # Phone
    phone_match = re.search(
        r"\+?\d[\d\s-]{9,15}",
        text
    )

    phone = phone_match.group().strip() if phone_match else None

    # Skills
    skills = []

    for skill in KNOWN_SKILLS:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "skills": skills
    }


def read_all_resumes(folder_path):
    """
    Read every PDF inside the resumes folder.
    """

    resumes = []

    for file in os.listdir(folder_path):

        if file.lower().endswith(".pdf"):

            pdf_path = os.path.join(folder_path, file)

            resumes.append(
                extract_resume(pdf_path)
            )

    return resumes


if __name__ == "__main__":

    resumes = read_all_resumes("input/resumes")

    for resume in resumes:
        print(resume)
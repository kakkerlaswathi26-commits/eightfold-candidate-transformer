import re


def read_resume(file_path):
    """
    Reads a resume text file and extracts candidate information.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Extract email
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    email = email.group() if email else None

    # Extract phone
    phone = re.search(r"\b\d{10}\b", text)
    phone = phone.group() if phone else None

    # Extract skills
    known_skills = [
        "Python",
        "Java",
        "SQL",
        "Docker",
        "Git",
        "HTML",
        "CSS",
        "JavaScript"
    ]

    skills = []

    for skill in known_skills:
        if skill.lower() in text.lower():
            skills.append(skill)

    candidate = {
        "email": email,
        "phone": phone,
        "skills": skills
    }

    return candidate


if __name__ == "__main__":
    data = read_resume("input/resume.txt")

    print(data)
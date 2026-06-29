import phonenumbers


def normalize_phone(phone):
    """
    Convert phone number to international format.
    """

    try:
        parsed = phonenumbers.parse(phone, "IN")

        return phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.E164
        )

    except:
        return phone


def normalize_skill(skill):
    skill = skill.strip()

    special_skills = {
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript"
    }

    if skill.lower() in special_skills:
        return special_skills[skill.lower()]

    return skill.title()


def normalize_candidate(candidate):
    """
    Normalize candidate data.
    """

    if "phone" in candidate and candidate["phone"]:
        candidate["phone"] = normalize_phone(candidate["phone"])

    if "skills" in candidate:
        candidate["skills"] = [
            normalize_skill(skill)
            for skill in candidate["skills"]
        ]

    return candidate


if __name__ == "__main__":

    sample = {
        "phone": "9876543210",
        "skills": [
            "python",
            "JAVA",
            " sql "
        ]
    }

    print(normalize_candidate(sample))
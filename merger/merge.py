def merge_candidate(csv_data, resume_data):
    """
    Merge candidate data from CSV and Resume.
    """

    merged = {}

    # Copy CSV fields
    merged.update(csv_data)

    # Add Resume fields if they don't exist
    for key, value in resume_data.items():

        if key == "skills":

            csv_skills = merged.get("skills", [])

            merged["skills"] = list(
                set(csv_skills + value)
            )

        else:

            if value:
                merged[key] = value

    return merged


if __name__ == "__main__":

    csv_candidate = {
        "full_name": "Swathi K",
        "email": "swathi.k@gmail.com",
        "phone": "+919876543210",
        "company": "TCS",
        "title": "Software Engineer"
    }

    resume_candidate = {
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Docker",
            "Git"
        ]
    }

    result = merge_candidate(
        csv_candidate,
        resume_candidate
    )

    print(result)
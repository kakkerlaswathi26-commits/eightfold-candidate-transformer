def merge_candidate(csv_data, resume_data):
    """
    Merge candidate information from CSV and Resume.
    Also stores confidence and provenance information.
    """

    merged = {}

    # Candidate basic details
    merged["full_name"] = csv_data.get("full_name")

    merged["emails"] = [
        csv_data["email"]
    ] if csv_data.get("email") else []

    merged["phones"] = [
        csv_data["phone"]
    ] if csv_data.get("phone") else []

    merged["company"] = csv_data.get("company")

    merged["title"] = csv_data.get("title")

    # Skills with confidence
    merged["skills"] = []

    for skill in resume_data.get("skills", []):

        merged["skills"].append({
            "name": skill,
            "confidence": 0.95,
            "sources": ["resume"]
        })

    # Provenance
    merged["provenance"] = [

        {
            "field": "full_name",
            "source": "csv"
        },

        {
            "field": "emails",
            "source": "csv"
        },

        {
            "field": "phones",
            "source": "csv"
        },

        {
            "field": "company",
            "source": "csv"
        },

        {
            "field": "title",
            "source": "csv"
        },

        {
            "field": "skills",
            "source": "resume"
        }

    ]

    # Overall confidence
    merged["overall_confidence"] = 0.95

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

    print(merge_candidate(csv_candidate, resume_candidate))
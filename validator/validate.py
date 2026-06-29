import json
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_candidate(candidate, schema_path):
    """
    Validate the candidate JSON against the schema.
    """

    with open(schema_path, "r") as file:
        schema = json.load(file)

    try:
        validate(instance=candidate, schema=schema)
        print("✅ JSON Validation Successful")
        return True

    except ValidationError as e:
        print("❌ JSON Validation Failed")
        print(e.message)
        return False


if __name__ == "__main__":

    # Sample candidate data
    sample_candidate = {
        "full_name": "Swathi K",
        "email": "swathi.k@gmail.com",
        "phone": "+919876543210",
        "company": "TCS",
        "title": "Software Engineer",
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Docker",
            "Git"
        ]
    }

    # Get path to schema.json
    current_dir = os.path.dirname(__file__)
    schema_path = os.path.join(current_dir, "..", "schema.json")

    # Validate
    validate_candidate(sample_candidate, schema_path)
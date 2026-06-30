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
        "candidate_id": "C001",
        "full_name": "Swathi K",
        "emails": [
            "swathi.k@gmail.com"
        ],
        "phones": [
            "+919876543210"
        ],
        "company": "TCS",
        "title": "Software Engineer",
        "skills": [
            {
                "name": "Python",
                "confidence": 0.95,
                "sources": ["resume"]
            },
            {
                "name": "Java",
                "confidence": 0.95,
                "sources": ["resume"]
            }
        ],
        "provenance": [
            {
                "field": "emails",
                "source": "csv"
            }
        ],
        "overall_confidence": 0.95
    }

    # Get path to schema.json
    current_dir = os.path.dirname(__file__)
    schema_path = os.path.join(current_dir, "..", "schema.json")

    # Validate
    validate_candidate(sample_candidate, schema_path)
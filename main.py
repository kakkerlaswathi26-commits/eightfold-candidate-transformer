import json
import os

from parsers.csv_parser import read_csv
from parsers.resume_parser import read_resume

from normalizer.normalize import normalize_candidate

from merger.merge import merge_candidate

from config.config_loader import load_config

from validator.validate import validate_candidate


def project_output(candidate, config):

    output = {}

    fields = config.get("fields", [])

    for field in fields:

        output[field] = candidate.get(field, config.get("on_missing"))

    return output


def main():

    # Read CSV
    csv_candidates = read_csv("input/recruiter.csv")

    # Read Resume
    resume = read_resume("input/resume.txt")

    final_profiles = []

    config = load_config("config/default.json")

    schema_path = os.path.join(
        os.path.dirname(__file__),
        "schema.json"
    )

    for candidate in csv_candidates:

        normalized_csv = normalize_candidate(candidate)

        normalized_resume = normalize_candidate(resume)

        merged = merge_candidate(
            normalized_csv,
            normalized_resume
        )

        projected = project_output(
            merged,
            config
        )

        if validate_candidate(projected, schema_path):

            final_profiles.append(projected)

    os.makedirs("output", exist_ok=True)

    with open(
        "output/profile.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            final_profiles,
            file,
            indent=4
        )

    print("\n✅ Candidate profiles generated successfully!")

    print("\nSaved to output/profile.json")


if __name__ == "__main__":
    main()
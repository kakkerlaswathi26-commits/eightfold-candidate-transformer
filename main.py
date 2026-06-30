import json
import os
import argparse

from parsers.csv_parser import read_csv
from parsers.resume_parser import read_all_resumes

from normalizer.normalize import normalize_candidate

from merger.merge import merge_candidate

from config.config_loader import load_config

from validator.validate import validate_candidate


def project_output(candidate, config):
    """
    Create the final output according to the config.
    """

    output = {}

    fields = config.get("fields", [])

    for field in fields:

        output[field] = candidate.get(
            field,
            config.get("on_missing")
        )

    return output

def main():

    # Read CSV
    parser = argparse.ArgumentParser(
    description="Candidate Data Transformer"
    )

    parser.add_argument(
        "--config",
        default="config/default.json",
        help="Path to configuration file"
    )
    args = parser.parse_args()
    csv_candidates = read_csv("input/recruiter.csv")

    # Read Resume
    resumes = read_all_resumes("input/resumes")

    final_profiles = []

    candidate_counter = 1

    config = load_config(args.config)

    schema_path = os.path.join(
        os.path.dirname(__file__),
        "schema.json"
    )

    for candidate in csv_candidates:

        normalized_csv = normalize_candidate(candidate)

        matched_resume = {}

        for resume in resumes:
            if resume.get("email") == candidate.get("email"):
                matched_resume = resume
                break
        normalized_resume = normalize_candidate(
            matched_resume
        )
        merged = merge_candidate(
            normalized_csv,
            normalized_resume
        )

        projected = project_output(
        merged,
        config
        )

        projected["candidate_id"] = f"C{candidate_counter:03d}"

        candidate_counter += 1

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
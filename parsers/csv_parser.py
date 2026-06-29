import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)

    candidates = []

    for _, row in df.iterrows():
        candidate = {
            "full_name": row["Name"],
            "email": row["Email"],
            "phone": str(row["Phone"]),
            "company": row["Company"],
            "title": row["Title"]
        }

        candidates.append(candidate)

    return candidates


if __name__ == "__main__":
    data = read_csv("input/recruiter.csv")

    for candidate in data:
        print(candidate)
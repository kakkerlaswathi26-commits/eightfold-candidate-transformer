# Eightfold Candidate Data Transformer

## Project Overview

The Eightfold Candidate Data Transformer is a modular Python application that converts candidate information from multiple data sources into a standardized JSON format.

The system combines:

- Structured data from a recruiter CSV file
- Unstructured data from PDF resumes

It normalizes, merges, validates, and exports candidate profiles while maintaining a clean and modular architecture.

---

## Features

- Parse recruiter CSV data
- Parse multiple PDF resumes
- Normalize phone numbers
- Normalize skills
- Match resumes with recruiter records using email
- Merge candidate information
- Generate candidate IDs
- Confidence scoring
- Provenance tracking
- Runtime configurable output
- JSON Schema validation
- Export standardized JSON profiles

---

## Project Structure

```
Eightfold-candidate-transformer/
│
├── config/
│   ├── default.json
│   └── custom.json
│
├── input/
│   ├── recruiter.csv
│   ├── resume.txt
│   └── resumes/
│       ├── Swathi.pdf
│       ├── Aishu.pdf
│       ├── Priya.pdf
│       └── Indhu.pdf
│
├── merger/
├── normalizer/
├── output/
├── parsers/
├── validator/
│
├── main.py
├── schema.json
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3.12
- Pandas
- PyPDF2
- JSON Schema
- phonenumbers
- dateparser

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Using the default configuration:

```bash
python main.py
```

Using a custom configuration:

```bash
python main.py --config config/custom.json
```

---

## Input

### Structured Source

- recruiter.csv

### Unstructured Source

- PDF resumes

---

## Output

The application generates:

```
output/profile.json
```

Each candidate profile contains:

- Candidate ID
- Name
- Email(s)
- Phone(s)
- Company
- Title
- Skills
- Provenance
- Confidence Score

---

## Validation

All generated profiles are validated using JSON Schema before being exported.

---

## Future Enhancements

- OCR support for scanned resumes
- NLP-based skill extraction
- Fuzzy candidate matching
- Database integration
- REST API

---

## Author

**Kakkerla Swathi Priya**

B.Tech – Computer Science & Engineering

CMR Technical Campus
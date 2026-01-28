import json
import csv
from pathlib import Path


INPUT_PATH = Path("data.json")
OUTPUT_PATH = Path("data.csv")

COLUMNS = [
    "participant_id",
    "condition",
    "question_order",
    # Main story questions
    "break",
    "cause_break",
    "anger",
    "cause_anger",
    # Demographics
    "age",
    "race",
    "gender",
    "ethnicity",
]


def load_records(path: Path):
    """
    Parse data.json, which contains multiple JSON objects separated by blank
    lines and commas, plus one stray '×' character.
    We turn the whole thing into a single JSON array and load it.
    """
    text = path.read_text(encoding="utf-8")
    # Remove the single stray '×' marker
    text = text.replace("×", "")

    # Wrap as a JSON array. The file is already a sequence of
    # `{ ... },` blocks, so this should be valid as-is.
    array_text = "[\n" + text + "\n]"

    return json.loads(array_text)


def main():
    records = load_records(INPUT_PATH)

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()

        for rec in records:
            responses = rec.get("responses", {}) or {}
            participants = rec.get("participants", {}) or {}
            question_order = rec.get("question_order", [])
            
            # Convert question_order list to string (e.g., "cause_break,break,anger,cause_anger")
            question_order_str = ",".join(question_order) if question_order else ""

            row = {
                "participant_id": rec.get("participant_id", ""),
                "condition": rec.get("condition", ""),
                "question_order": question_order_str,
                # Main story questions
                "break": responses.get("break", ""),
                "cause_break": responses.get("cause_break", ""),
                "anger": responses.get("anger", ""),
                "cause_anger": responses.get("cause_anger", ""),
                # Demographics
                "age": participants.get("age", ""),
                "race": participants.get("race", ""),
                "gender": participants.get("gender", ""),
                "ethnicity": participants.get("ethnicity", ""),
            }
            writer.writerow(row)


if __name__ == "__main__":
    main()

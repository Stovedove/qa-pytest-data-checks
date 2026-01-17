import csv
from pathlib import Path


def load_users(csv_path):
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


def get_emails(rows):
    return [row["email"].strip().lower() for row in rows]


def get_ages(rows):
    return [int(row["age"]) for row in rows]


def has_duplicates(values):
    return len(values) != len(set(values))

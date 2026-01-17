import csv
from pathlib import Path


def load_rows(path):
    with open(Path(path), newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

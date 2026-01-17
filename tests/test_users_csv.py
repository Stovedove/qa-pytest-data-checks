from pathlib import Path
from src import validator


def test_emails_are_unique():
    csv_path = Path('data/users.csv')
    rows = validator.load_users(csv_path)
    emails = validator.get_emails(rows)
    assert validator.has_duplicates(emails) is False


def test_ages_in_range():
    csv_path = Path('data/users.csv')
    rows = validator.load_users(csv_path)
    ages = validator.get_ages(rows)
    assert all(18 <= age <= 65 for age in ages)


def test_active_values_valid():
    csv_path = Path('data/users.csv')
    rows = validator.load_users(csv_path)
    values = {row['active'].strip().lower() for row in rows}
    assert values.issubset({'true', 'false'})

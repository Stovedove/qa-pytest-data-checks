from data_checks.rules import validate_row, find_duplicate_emails


def test_validate_row_ok():
    row = {"name": "Ana", "email": "ana@mail.com", "age": "24", "active": "true"}
    result = validate_row(row)
    assert result["ok"] is True


def test_validate_row_errors():
    row = {"name": "", "email": "bad", "age": "90", "active": "yes"}
    result = validate_row(row)
    assert result["ok"] is False
    assert "email" in result["errors"]


def test_duplicate_emails():
    rows = [
        {"email": "a@mail.com"},
        {"email": "A@mail.com"},
    ]
    duplicates = find_duplicate_emails(rows)
    assert len(duplicates) == 1

import re


EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def validate_row(row):
    errors = []
    if not row.get("name"):
        errors.append("name")
    if not EMAIL_RE.match(row.get("email", "")):
        errors.append("email")
    try:
        age = int(row.get("age", ""))
        if age < 18 or age > 65:
            errors.append("age")
    except ValueError:
        errors.append("age")
    if row.get("active") not in {"true", "false"}:
        errors.append("active")
    return {"ok": len(errors) == 0, "errors": errors}


def validate_rows(rows):
    results = []
    for row in rows:
        results.append({"id": row.get("id"), **validate_row(row)})
    return results


def find_duplicate_emails(rows):
    seen = set()
    duplicates = set()
    for row in rows:
        email = (row.get("email") or "").strip().lower()
        if not email:
            continue
        if email in seen:
            duplicates.add(email)
        seen.add(email)
    return list(duplicates)

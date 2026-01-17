import sys
import click

from .config import Settings
from .loader import load_rows
from .report import save_report, summary
from .rules import find_duplicate_emails, validate_rows


@click.group()
def main():
    pass


@main.command()
@click.option("--csv", "csv_path", default=None, help="CSV path")
@click.option("--report", "report_path", default=None, help="Report path")
def run(csv_path, report_path):
    settings = Settings()
    csv_path = csv_path or settings.csv_path
    report_path = report_path or settings.report_path

    rows = load_rows(csv_path)
    results = validate_rows(rows)
    duplicates = find_duplicate_emails(rows)
    report_file = save_report(
        results + [{"name": "duplicate_emails", "ok": len(duplicates) == 0, "items": duplicates}],
        report_path,
    )

    info = summary(results)
    click.echo(f"Total: {info['total']} | Passed: {info['passed']} | Failed: {info['failed']}")
    click.echo(f"Duplicate emails: {len(duplicates)}")
    click.echo(f"Report: {report_file}")

    if info["failed"] > 0 or len(duplicates) > 0:
        sys.exit(1)

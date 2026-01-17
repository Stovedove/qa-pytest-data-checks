import json
from pathlib import Path


def save_report(results, path):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {"summary": summary(results), "results": results}
    target.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return target


def summary(results):
    total = len(results)
    failed = sum(1 for r in results if not r["ok"])
    return {"total": total, "passed": total - failed, "failed": failed}

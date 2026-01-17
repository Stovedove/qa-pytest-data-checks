from data_checks.report import summary


def test_summary_counts():
    results = [
        {"ok": True},
        {"ok": False},
        {"ok": True},
    ]
    info = summary(results)
    assert info["total"] == 3
    assert info["passed"] == 2
    assert info["failed"] == 1

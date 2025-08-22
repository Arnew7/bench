from bench.reporter import format_report
from bench.models import HostReport

def test_format_report():
    rep = HostReport("https://example.com", 1, 0, 0, [10, 20])
    out = format_report([rep])
    assert "Host" in out
    assert "Success" in out
    assert "Avg" in out

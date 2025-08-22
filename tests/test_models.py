from bench.models import HostReport

def test_host_report_stats():
    rep = HostReport("test", 1, 1, 0, [10, 20, 30])
    assert rep.min_ms == 10
    assert rep.max_ms == 30
    assert round(rep.avg_ms, 2) == 20.0

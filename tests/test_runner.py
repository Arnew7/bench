import pytest
import asyncio
from bench.runner import bench_host
from bench.models import HostReport

@pytest.mark.asyncio
async def test_bench_host_mocked(monkeypatch):
    async def fake_fetch_one(session, url):
        from bench.models import SingleResult
        return SingleResult(status=200, elapsed_ms=123.0, error=None)

    monkeypatch.setattr("bench.fetcher.fetch_one", fake_fetch_one)
    report = await bench_host("https://google.com", 3)
    assert isinstance(report, HostReport)
    assert report.success == 3

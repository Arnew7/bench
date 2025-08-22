import asyncio
import sys
import pytest
from bench.__main__ import main

@pytest.mark.asyncio
async def test_main_end_to_end(capsys):
    code = await main(["-H", "https://example.com", "-C", "1"])
    assert code == 0
    out, _ = capsys.readouterr()
    assert "Host" in out

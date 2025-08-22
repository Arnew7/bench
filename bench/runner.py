import asyncio
import aiohttp
from typing import List
from .models import HostReport
from .fetcher import fetch_one

async def bench_host(url: str, count: int, timeout_s: float = 30.0) -> HostReport:
    timeout = aiohttp.ClientTimeout(total=timeout_s)
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        results = await asyncio.gather(*[fetch_one(session, url) for _ in range(count)])

    success, failed, errors, times = 0, 0, 0, []
    for r in results:
        if r.status is None:
            errors += 1
        else:
            times.append(r.elapsed_ms)
            if 200 <= r.status < 300 or r.status < 400:
                success += 1
            elif 400 <= r.status < 600:
                failed += 1
    return HostReport(url, success, failed, errors, times)

async def bench_all(hosts: List[str], count: int) -> List[HostReport]:
    return await asyncio.gather(*[bench_host(h, count) for h in hosts])

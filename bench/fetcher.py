import asyncio
import time
import aiohttp
from aiohttp.client_exceptions import ClientError
from .models import SingleResult

async def fetch_one(session: aiohttp.ClientSession, url: str) -> SingleResult:
    start = time.monotonic()
    try:
        async with session.get(url) as resp:
            await resp.read()
            return SingleResult(status=resp.status, elapsed_ms=(time.monotonic() - start) * 1000, error=None)
    except asyncio.TimeoutError:
        return SingleResult(status=None, elapsed_ms=(time.monotonic() - start) * 1000, error="тайм-аут")
    except ClientError as e:
        return SingleResult(status=None, elapsed_ms=(time.monotonic() - start) * 1000, error=str(e))
    except Exception as e:
        return SingleResult(status=None, elapsed_ms=(time.monotonic() - start) * 1000, error=f"ошибка: {e}")

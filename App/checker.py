import asyncio
import time
import aiohttp

from App.models import Url


async def check_url(
    session: aiohttp.ClientSession,
    url: str,
    timeout: int = 10
) -> Url:

    start_time = time.perf_counter()

    try:
        timeout_config = aiohttp.ClientTimeout(total=timeout)

        async with session.get(
            url,
            timeout=timeout_config
        ) as response:

            await response.read()

        end_time = time.perf_counter()

        response_time = round(
            (end_time - start_time) * 1000,
            2
        )

        if response.status < 400:
            status = "Up"
        else:
            status = "Down"

        return Url(
            url=url,
            status=status,
            status_code=response.status,
            response_time=response_time
        )

    except asyncio.TimeoutError:

        return Url(
            url=url,
            status="Down",
            status_code=None,
            response_time=0,
            error="Request timeout"
        )

    except aiohttp.ClientError as error:

        return Url(
            url=url,
            status="Down",
            status_code=None,
            response_time=0,
            error=str(error)
        )


async def check_all_urls(urls):

    async with aiohttp.ClientSession() as session:

        tasks = [
            check_url(session, url)
            for url in urls
        ]

        results = await asyncio.gather(*tasks)

        return results
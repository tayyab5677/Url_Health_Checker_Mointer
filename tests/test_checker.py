import pytest

from App.checker import check_all_urls


@pytest.mark.asyncio
async def test_check_all_urls():

    urls = [
        "https://example.com",
        "https://httpbin.org/status/200",
    ]

    results = await check_all_urls(urls)

    assert len(results) == 2

    assert results[0].url == urls[0]
    assert results[1].url == urls[1]
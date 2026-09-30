from App.models import URLResult
from App.processor import (
    calculate_success_rate,
    get_down_urls,
    get_up_urls,
)


def test_get_up_urls():

    results = [
        URLResult(
            "https://a.com",
            "UP",
            200,
            100,
        ),
        URLResult(
            "https://b.com",
            "DOWN",
            404,
            150,
        ),
    ]

    up = get_up_urls(results)

    assert len(up) == 1
    assert up[0].url == "https://a.com"


def test_get_down_urls():

    results = [
        URLResult(
            "https://a.com",
            "UP",
            200,
            100,
        ),
        URLResult(
            "https://b.com",
            "DOWN",
            404,
            150,
        ),
    ]

    down = get_down_urls(results)

    assert len(down) == 1
    assert down[0].url == "https://b.com"


def test_success_rate():

    results = [
        URLResult(
            "https://a.com",
            "UP",
            200,
            100,
        ),
        URLResult(
            "https://b.com",
            "DOWN",
            404,
            150,
        ),
    ]

    assert calculate_success_rate(results) == 50.0
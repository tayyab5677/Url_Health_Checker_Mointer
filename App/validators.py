from urllib.parse import urlparse

from App.exceptions import InvalidUrl


def validate_url(url: str) -> bool:

    if not url:
        raise InvalidUrl("URL is required")

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise InvalidUrl(f"{url} has an invalid URL scheme")

    if not parsed.netloc:
        raise InvalidUrl(f"Invalid URL: {url}")

    return True


def validate_urls(urls: list[str]) -> bool:

    for url in urls:
        validate_url(url)

    return True
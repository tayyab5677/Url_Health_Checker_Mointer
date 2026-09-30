from dataclasses import dataclass


@dataclass
class Url:
    url: str
    status: str
    status_code: int | None
    response_time: float
    error: str | None = None
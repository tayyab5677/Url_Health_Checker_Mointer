import pytest

from App.exceptions import InvalidURLError
from App.validators import validate_url


def test_valid_url():
    assert validate_url(
        "https://example.com"
    ) is True


def test_invalid_url():

    with pytest.raises(InvalidURLError):
        validate_url("invalid-url")
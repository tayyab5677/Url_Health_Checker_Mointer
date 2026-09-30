class InvalidUrl(Exception):
    """Raised when the user enters an invalid URL."""
    pass


class UrlCheckError(Exception):
    """Raised when there is a URL checking error."""
    pass
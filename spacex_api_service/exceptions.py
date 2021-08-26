
class SpacexAPIServiceException(Exception):
    """SpaceX API returned an error."""

    def __init__(self, message='SpaceX API returned an error. Check request validity.'):
        self.message = message
        super().__init__()


class DataParsingException(Exception):
    """Error while parsing data via pydantic"""

    def __init__(self, message='Data returned from API could not been parsed.'):
        self.message = message
        super().__init__()

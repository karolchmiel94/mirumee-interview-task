class BooleanParsingException(Exception):
    """Argument could not been parsed."""

    def __init__(self, parameter):
        self.message = 'Parameter {} has to be either True or False.'.format(
            parameter)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class IntegerParsingException(Exception):
    """Argument could not been parsed."""

    def __init__(self, parameter):
        self.message = 'Parameter {} cores_number has to be Integer.'.format(
            parameter)
        super().__init__(self.message)

    def __str__(self):
        return self.message

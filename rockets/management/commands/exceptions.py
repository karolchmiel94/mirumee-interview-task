class ArgumentParsingException(Exception):
    """Argument could not been parsed."""

    def __init__(self, argument):
        self.message = '{} has to be either True or False.'.format(argument)
        super().__init__(self.message)

    def __str__(self):
        return self.message

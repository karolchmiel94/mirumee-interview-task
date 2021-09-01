from utilities.parser import parse_string_to_bool
from .exceptions import BooleanParsingException, IntegerParsingException


def get_value_from_query(query, param):
    return query.get(param)


def parse_param_to_bool(query, param):
    param_value = get_value_from_query(query, param)
    if param_value is not None:
        try:
            return parse_string_to_bool(param_value)
        except ValueError as e:
            raise BooleanParsingException(param)
    return None


def parse_param_to_int(query, param):
    param_value = get_value_from_query(query, param)
    if param_value is not None:
        try:
            return int(param_value)
        except ValueError as e:
            raise IntegerParsingException(param)
    return None

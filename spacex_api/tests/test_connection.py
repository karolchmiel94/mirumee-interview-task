from django.test import SimpleTestCase

from ..connection import fetch_data_with_query
from ..exceptions import SpacexAPIServiceException


class TestConnection(SimpleTestCase):

    def test_api_response(self):
        data = fetch_data_with_query()
        self.assertNotEquals(data, None)

    def test_invalid_query_params(self):
        query = """{
            launches(find: {test})
        }"""
        with self.assertRaises(SpacexAPIServiceException) as e:
            fetch_data_with_query(query)
            self.assertAlmostEqual(
                e.message, 'Syntax Error: Expected :, found }. ')

    def test_query_exceeding_complexity_limit(self):
        query = """{
            launchesPast {
                ships {
                image
                missions {
                    flight
                }
                }
            }
            }"""
        with self.assertRaises(SpacexAPIServiceException) as e:
            fetch_data_with_query(query)
            self.assertAlmostEqual(
                e.message, 'query exceeds complexity limit. ')

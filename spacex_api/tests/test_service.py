import json
from django.test import SimpleTestCase

from ..service import get_cores_data, get_response_data_with_calculated_weights
from ..exceptions import SpacexAPIServiceException
from .. import api_models


class TestConnection(SimpleTestCase):

    def test_no_cores(self):
        cores = get_cores_data(0)
        self.assertEqual(len(cores), 0)

    def test_get_one_core(self):
        cores = get_cores_data(1)
        self.assertEqual(len(cores), 1)

    def test_calculating_weights(self):
        data_str = json.loads("""{ "launchesPast": [ { "id": "109", "rocket": { "first_stage": { "cores": [ { "core": { "id": "B1049", "reuse_count": 6 }, "reused": true } ] }, "rocket": { "id": "falcon9", "payload_weights": [ { "kg": 22800, "id": "leo" }, { "kg": 8300, "id": "gto" }, { "kg": 4020, "id": "mars" } ] } }, "launch_success": true, "upcoming": false } ] }""")
        data = api_models.ApiData.parse_obj(data_str)
        calculated_data = get_response_data_with_calculated_weights(data, 1)
        print(calculated_data)
        self.assertEqual(calculated_data, [('B1049', 6, 35120)])

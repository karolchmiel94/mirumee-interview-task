import json
from django.test import TestCase

from ..models import Core
from ..service import fetch_cores_if_not_in_database


class TestService(TestCase):

    def test_fetching_cores(self):
        self.assertEquals(Core.objects.count(), 0)
        fetch_cores_if_not_in_database()
        self.assertNotEquals(Core.objects.count(), 0)

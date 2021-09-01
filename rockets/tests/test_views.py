from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


from rockets.models import Core, FavouriteCore
from utilities.exceptions import (
    BooleanParsingException, IntegerParsingException)


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.fetch_cores_url = reverse('rockets:fetch-cores-list')
        cls.favourite_cores_url = reverse("rockets:favourite-cores-list")
        cls.cores_url = reverse('rockets:cores-list')

        cls.user = User.objects.create(
            username='testuser', email='', password='password')
        cls.auth_client = Client()
        cls.auth_client.force_login(cls.user)

    def test_cores_list_GET(self):
        response = self.client.get(self.cores_url)

        self.assertEquals(response.status_code, 200)

    def test_fetch_cores_GET_valid_data(self):
        response = self.client.get(self.fetch_cores_url)

        self.assertEquals(response.status_code, 200)

    def test_fetch_cores_GET_invalid_cores_number_param(self):
        param = 'cores_number'
        response = self.client.get(self.fetch_cores_url + '?' + param + '=test'
                                   )

        self.assertEquals(response.status_code, 400)
        self.assertEquals(
            response.data, IntegerParsingException(param).message)

    def test_fetch_cores_GET_invalid_successful_param(self):
        param = 'successful'
        response = self.client.get(self.fetch_cores_url + '?' + param + '=test'
                                   )

        self.assertEquals(response.status_code, 400)
        self.assertEquals(
            response.data, BooleanParsingException(param).message)

    def test_fetch_cores_GET_invalid_planned_param(self):
        param = 'planned'
        response = self.client.get(self.fetch_cores_url + '?' + param + '=test'
                                   )

        self.assertEquals(response.status_code, 400)
        self.assertEquals(
            response.data, BooleanParsingException(param).message)

    def test_favourites_cores_GET_no_authenticated(self):
        response = self.client.get(self.favourite_cores_url)

        self.assertEquals(response.status_code, 403)

    def test_favourites_cores_GET_authenticated(self):
        response = self.auth_client.get(self.favourite_cores_url)

        self.assertEquals(response.status_code, 200)

    def test_add_core_to_favourites(self):
        core = Core.objects.create(core_id='CORE1')
        response = self.auth_client.post(
            self.favourite_cores_url, {'core': core.id})

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data.get('core'), core.id)

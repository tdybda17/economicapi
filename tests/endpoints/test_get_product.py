import json
from collections import namedtuple
from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TestGetProductEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = '/api/v1/product/10/'
        user = User.objects.create_superuser(username='tobias', email='t@t.dk', password='123')
        token = Token.objects.create(user_id=user.id, key='123')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_can_get(self):
        content = self._get_and_get_response(200, content=b'{"product": "product"}')
        expected = {'data': {'product': 'product'}, 'status_code': 200}
        self.assertDictEqual(expected, content)

    def test_can_get_400_error(self):
        content = self._get_and_get_response(404, content=b'{"Not found": "Not found"}')
        expected = {'data': {'message': 'Product does not exist'}, 'status_code': 404}
        self.assertDictEqual(expected, content)

    def test_can_get_unknown_error(self):
        content = self._get_and_get_response(520, content=b'{"Unknown error": "unknown"}')
        expected = {'data': {'Unknown error': 'unknown', 'status_code': 520}, 'status_code': 520}
        self.assertDictEqual(expected, content)

    def _get_and_get_response(self, status_code, content=None):
        with mock.patch('requests.get') as mock_response:
            mock_response.return_value = self._create_mock_response(status_code, content)
            response = self.client.get(self.url)
            return json.loads(response.content.decode('utf-8'))

    def _create_mock_response(self, status_code, content):
        Response = namedtuple("Response", ['status_code', 'content'])
        return Response(status_code=status_code, content=content)

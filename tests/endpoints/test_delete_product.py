import json
from collections import namedtuple
from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class TestDeleteProductEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = '/api/v1/product/10/'
        user = User.objects.create_superuser(username='tobias', email='t@t.dk', password='123')
        token = Token.objects.create(user_id=user.id, key='123')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_can_delete_product_success(self):
        content = self._delete_and_get_response(status_code=204)
        expected = {'data': {'message': 'product updated'}, 'status_code': 200}
        self.assertDictEqual(expected, content)

    def test_when_unknown_error_Should_get_520(self):
        content = self._delete_and_get_response(520, content=b'{"Unknown error": "unknown"}')
        expected = {'data': {'Unknown error': 'unknown', 'status_code': 520}, 'status_code': 520}
        self.assertDictEqual(expected, content)

    def _delete_and_get_response(self, status_code, content=None):
        with mock.patch('requests.delete') as mock_response:
            mock_response.return_value = self._create_mock_response(status_code, content)
            response = self.client.delete(self.url)
            return json.loads(response.content.decode('utf-8'))

    def _create_mock_response(self, status_code, content):
        Response = namedtuple("Response", ['status_code', 'content'])
        return Response(status_code=status_code, content=content)

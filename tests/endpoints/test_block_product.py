import json
from collections import namedtuple
from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class TestSyncProductEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = '/api/v1/product/10/block/'
        user = User.objects.create_superuser(username='tobias', email='t@t.dk', password='123')
        token = Token.objects.create(user_id=user.id, key='123')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_when_product_does_not_exist_Should_get_404(self):
        expected = {'data': {'message': 'Not found'}, 'status_code': 404}
        content = self._post_and_get_response(status_code=404, content=bytes(str(json.dumps(expected)).encode('utf-8')))
        self.assertDictEqual(expected, content)

    def test_when_unable_to_convert_to_int_Should_get_501(self):
        with mock.patch('requests.get') as mock_response:
            return_value = json.dumps(
                {"inventory":
                     {"inStock": "not-convertable-to-int"}
                 }
            ).encode("utf-8")
            mock_response.return_value = self._create_mock_response(status_code=200, content=return_value)
            expected = {'data': {'message': 'E-conomic inventory get error'}, 'status_code': 501}
            content = self._post_and_get_response(status_code=501,
                                                  content=bytes(str(json.dumps(expected)).encode('utf-8')))
            self.assertDictEqual(expected, content)

    def _post_and_get_response(self, status_code, content=None):
        with mock.patch('rest_framework.test.APIClient.post') as mock_response:
            mock_response.return_value = self._create_mock_response(status_code, content)
            response = self.client.post(self.url)
            return json.loads(response.content.decode('utf-8'))

    def _create_mock_response(self, status_code, content):
        Response = namedtuple("Response", ['status_code', 'content'])
        return Response(status_code=status_code, content=content)

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
        self.url = '/api/v1/product/'
        user = User.objects.create_superuser(username='tobias', email='t@t.dk', password='123')
        token = Token.objects.create(user_id=user.id, key='123')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_can_send_empty_request(self):
        content = self._put_and_get_response(400, data={})
        expected = {'data': {'message': 'Hash value/product number is required'}, 'status_code': 400}
        self.assertDictEqual(expected, content)

    def test_can_create_product_and_get_success(self):
        content = self._put_and_get_response(201)
        expected = {"status_code": 201, "data": {"message": "product created"}}
        self.assertDictEqual(expected, content)

    def test_can_update_product_and_get_success(self):
        content = self._put_and_get_response(200)
        expected = {'status_code': 200, 'data': {'message': 'product updated'}}
        self.assertDictEqual(expected, content)

    def test_on_validation_error_Should_get_400_message(self):
        content = self._put_and_get_response(400, b'{"message": "validation"}')
        expected = {'status_code': 400, 'data': {'message': 'validation'}}
        self.assertDictEqual(expected, content)

    def test_on_authorization_error_Should_get_401_message(self):
        content = self._put_and_get_response(401)
        expected = {'status_code': 401, 'data': {'message': 'not authorized'}}
        self.assertEqual(expected, content)

    def test_on_forbidden_Should_get_403_message(self):
        content = self._put_and_get_response(403, b'{"message": "forbidden"}')
        expected = {'status_code': 403, 'data': {'message': 'forbidden'}}
        self.assertDictEqual(expected, content)

    def test_on_unknown_error_Should_get_520_message(self):
        content = self._put_and_get_response(520, b'{"message": "unknown"}')
        expected = {'data': {'message': 'unknown', 'status_code': 520}, 'status_code': 520}
        self.assertDictEqual(expected, content)

    def _put_and_get_response(self, status_code, content=None, data=None):
        default = self._get_default_data()
        with mock.patch('requests.put') as mock_response:
            mock_response.return_value = self._create_mock_response(status_code, content)
            response = self.client.put(
                self.url,
                data=default if data is None else data,
            )
            return json.loads(response.content.decode('utf-8'))

    def _get_default_data(self):
        return {
            'hash_value': '123',
            'cost_price': 40.5,
            'sale_price': 30.4
        }

    def _create_mock_response(self, status_code, content):
        """response = Response()
        response.status_code = status_code
        return response"""
        Response = namedtuple("Response", ['status_code', 'content'])
        return Response(status_code=status_code, content=content)

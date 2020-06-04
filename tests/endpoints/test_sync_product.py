import json
from collections import namedtuple
from unittest import mock
from django.test import TestCase, Client


class TestSyncProductEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = '/api/v1/sync-product'

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

    def _put_and_get_response(self, status_code, content=None):
        with mock.patch('requests.put') as mock_response:
            mock_response.return_value = self._create_mock_response(status_code, content)
            response = self.client.post(self.url, data={
                'hash_value': '123'
            })
            return json.loads(response.content.decode('utf-8'))

    def _create_mock_response(self, status_code, content):
        """response = Response()
        response.status_code = status_code
        return response"""
        Response = namedtuple("Response", ['status_code', 'content'])
        return Response(status_code=status_code, content=content)

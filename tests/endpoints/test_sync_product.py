import json
from unittest import mock

from django.test import TestCase, Client
from requests import Response


class TestSyncProductEndpoint(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = '/api/v1/sync-product'

    def test_can_post_and_get_success(self):
        with mock.patch('requests.put') as mock_response:
            mock_response.return_value = self._create_mock_response(200)
            response = self.client.post(self.url, data={
                'hash_value': '123'
            })
            content = json.loads(response.content.decode('utf-8'))
            expected = {"status_code": 200, "data": {"message": "product created"}}
            self.assertDictEqual(content, expected)

    def _create_mock_response(self, status_code):
        response = Response()
        response.status_code = status_code
        return response

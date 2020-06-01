from unittest import TestCase

from economic_dybdahl_rest.http.response import Response


class TestResponse(TestCase):

    def test_response_to_json(self):
        data = {
            'content': 'content'
        }
        status_code = 200
        response = Response(status_code, data)
        expected = {"status_code": 200, "data": {"content": "content"}}
        self.assertDictEqual(expected, response.to_dict())

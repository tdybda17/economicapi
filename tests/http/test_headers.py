from django.test import TestCase, RequestFactory

from economic_dybdahl_rest.http.headers import Headers


class TestHeaders(TestCase):

    def setUp(self) -> None:
        self.rf = RequestFactory()

    def test_can_make_empty_headers(self):
        request = self.rf.post('/')
        headers = Headers.from_request(request).headers
        expected = {
            'Content-Type': 'application/json',
            'X-AppSecretToken': '',
            'X-AgreementGrantToken': '',
        }
        self.assertDictEqual(expected, headers)

    def test_can_set_headers_from_request(self):
        request = self.rf.post('/')
        request.headers = {
            'X-AppSecretToken': 'secret-token',
            'X-AgreementGrantToken': 'grant-token'
        }
        headers = Headers.from_request(request).headers
        expected = {
            'Content-Type': 'application/json',
            'X-AppSecretToken': 'secret-token',
            'X-AgreementGrantToken': 'grant-token',
        }
        self.assertEqual(expected, headers)

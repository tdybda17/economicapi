from unittest import TestCase, mock

from requests.models import Response
from economic_dybdahl_rest.api.put_product import PutProduct
from economic_dybdahl_rest.dto.product import Product


class TestPostProduct(TestCase):

    def setUp(self) -> None:
        self.product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': 50,
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': 'h123iqwjd2enwef',
            'recommendedPrice': 50,
            'salesPrice': 20.3,
        })

    def test_when_product_number_does_not_exists_Should_make_product_and_return_201(self):
        with mock.patch.object(PutProduct, 'put') as put:
            put.return_value = self._create_mock_request(201)
            response = PutProduct().put(self.product)
            self.assertEqual(201, response.status_code)
            
    def test_when_product_exists_Should_update_product(self):
        with mock.patch.object(PutProduct, 'put') as put:
            put.return_value = self._create_mock_request(200)
            response = PutProduct().put(self.product)
            self.assertEqual(200, response.status_code)

    def _create_mock_request(self, status_code):
        response = Response()
        response.status_code = status_code
        return response

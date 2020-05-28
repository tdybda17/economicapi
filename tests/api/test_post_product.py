from unittest import TestCase, mock

from economic_dybdahl_rest.api.post_product import PostProduct
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
            'productNumber': '15002',
            'recommendedPrice': 50,
            'salesPrice': 1004.2,
        })

    def test_can_post_product(self):
        with mock.patch.object(PostProduct, 'post') as post:
            post.return_value = True
            response = PostProduct().post(self.product)
            self.assertTrue(response)

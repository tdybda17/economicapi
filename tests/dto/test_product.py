from django.test import TestCase, RequestFactory

from economic_dybdahl_rest.dto.product import Product
from economic_dybdahl_rest.dto.product_group import ProductGroup


class TestProduct(TestCase):

    def test_to_dict(self):
        product = Product(
            bar_code='5738951475903',
            cost_price=50,
            description='d',
            name='My test product',
            product_group=ProductGroup(
                product_group_number=1
            ),
            product_number='500',
            recommended_price=50,
            sales_price=100
        )
        expected = {
            'barCode': '5738951475903',
            'costPrice': 50,
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': '500',
            'recommendedPrice': 50,
            'salesPrice': 100,
        }
        self.assertDictEqual(expected, product.to_dict())

    def test_from_dict(self):
        product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': 50,
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': '500',
            'recommendedPrice': 50,
            'salesPrice': 100,
        })
        self.assertEqual('5738951475903', product.bar_code)
        self.assertEqual(50, product.cost_price)
        self.assertEqual('d', product.description)
        self.assertEqual('My test product', product.name)
        self.assertDictEqual(ProductGroup(1).to_dict(), product.product_group.to_dict())
        self.assertEqual('500', product.product_number)
        self.assertEqual(50, product.recommended_price)
        self.assertEqual(100, product.sales_price)

    def test_from_empty_request(self):
        request = RequestFactory().post('', data={})
        product = Product.from_request(request)
        self.assertIsNotNone(product)

    def test_from_request_with_data(self):
        request = RequestFactory().post('', data={
            'ean': '5738951475903',
            'sale_price': 100,
            'cost_price': 50,
            'description': 'd',
            'name': 'My test product',
            'company_group_number': 1,
            'hash_value': '500',
        })
        product = Product.from_request(request)
        self.assertEqual('5738951475903', product.bar_code)
        self.assertEqual('100', product.sales_price)
        self.assertEqual('50', product.cost_price)
        self.assertEqual('d', product.description)
        self.assertEqual('My test product', product.name)
        self.assertEqual('500', product.product_number)
        self.assertEqual('100', product.recommended_price)

from django.test import TestCase, RequestFactory

from economic_dybdahl_rest.dto.product import Product, ProductValidationError
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
            sales_price=100,
            barred=False
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
            'inventory': {
                'recommendedCostPrice': 50
            },
            'barred': False
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
            'barred': False
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

    def test_when_cost_price_is_not_float_Should_raise_error(self):
        product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': 'illegal',  # illegal price
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': '500',
            'recommendedPrice': '100',
            'salesPrice': 100,
            'barred': False,
        })
        with self.assertRaises(ProductValidationError):
            product.validate()

    def test_when_recommended_price_is_not_float_Should_raise_error(self):
        product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': '10',
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': '500',
            'recommendedPrice': 'illegal',  # illegal price
            'salesPrice': 100,
            'barred': False
        })
        with self.assertRaises(ProductValidationError):
            product.validate()

    def test_when_sales_price_is_not_float_Should_raise_error(self):
        product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': '10',
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': '500',
            'recommendedPrice': '100',
            'salesPrice': 'illegal',  # illegal price,
            'barred': False,
        })
        with self.assertRaises(ProductValidationError):
            product.validate()

    def test_can_convert_barred_to_boolean(self):
        product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': '10',
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': 1
            },
            'productNumber': '500',
            'recommendedPrice': '100',
            'salesPrice': 'illegal',  # illegal price,
            'barred': 'True',
        })
        self.assertTrue(product.barred)

    def test_when_valid_validation_Should_have_converted_fields_to_correct_types(self):
        product = Product.from_dict({
            'barCode': '5738951475903',
            'costPrice': '10',
            'description': 'd',
            'name': 'My test product',
            'productGroup': {
                'productGroupNumber': '1'
            },
            'productNumber': '500',
            'recommendedPrice': '100',
            'salesPrice': '2.2',
            'barred': False,
        })
        product.validate()
        self.assertEqual(10.00, product.cost_price)
        self.assertEqual(1, product.product_group.product_group_number)
        self.assertEqual(100.00, product.recommended_price)
        self.assertEqual(2.20, product.sales_price)
        self.assertFalse(product.barred)

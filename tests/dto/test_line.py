from unittest import TestCase

from economic_dybdahl_rest.dto.line import Line


class TestLine(TestCase):

    def test_to_dict(self):
        line = Line(
            unit_number=2,
            unit_name='Tim',
            product_number='50',
            quantity=1.00,
            unit_net_price=10.00,
            discount_percentage=0.00,
            unit_cost_price=46.93,
            total_net_amount=10.00,
            margin_in_base_currency=-46.93,
            margin_percentage=0.0
        )
        expected = {
            "unit": {
                "unitNumber": 2,
                "name": "Tim"
            },
            "product": {
                "productNumber": "50"
            },
            "quantity": 1.00,
            "unitNetPrice": 10.00,
            "discountPercentage": 0.00,
            "unitCostPrice": 46.93,
            "totalNetAmount": 10.00,
            "marginInBaseCurrency": -46.93,
            "marginPercentage": 0.0
        }
        self.assertDictEqual(expected, line.to_dict())

    def test_from_dict(self):
        line = Line.from_dict({
            "unit": {
                "unitNumber": 2,
                "name": "Tim"
            },
            "product": {
                "productNumber": "50"
            },
            "quantity": 1.00,
            "unitNetPrice": 10.00,
            "discountPercentage": 0.00,
            "unitCostPrice": 46.93,
            "totalNetAmount": 10.00,
            "marginInBaseCurrency": -46.93,
            "marginPercentage": 0.0
        })
        self.assertEqual(2, line.unit_number)
        self.assertEqual('Tim', line.unit_name)
        self.assertEqual('50', line.product_number)
        self.assertEqual(1.00, line.quantity)
        self.assertEqual(10.00, line.unit_net_price)
        self.assertEqual(0.00, line.discount_percentage)
        self.assertEqual(46.93, line.unit_cost_price)
        self.assertEqual(10.00, line.total_net_amount)
        self.assertEqual(-46.93, line.margin_in_base_currency)
        self.assertEqual(0.0, line.margin_percentage)

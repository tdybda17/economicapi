from unittest import TestCase

from economic_dybdahl_rest.api.post_draft_order import PostDraftOrder
from economic_dybdahl_rest.dto.line import Line
from tests.dto.test_order import default_order as dummy_order


class TestPostDraftOrder(TestCase):

    def setUp(self) -> None:
        self.default_order = dummy_order

    def test_(self):
        self.default_order.layout_number = 19
        self.default_order.lines = [
            Line(
                unit_number=2,
                unit_name='Tim',
                product_number='1',
                quantity=1.00,
                unit_net_price=10.00,
                discount_percentage=0.00,
                unit_cost_price=46.93,
                total_net_amount=10.00,
                margin_in_base_currency=-46.93,
                margin_percentage=0.0
            )
        ]
        response = PostDraftOrder().post(self.default_order)
        print(response.content)

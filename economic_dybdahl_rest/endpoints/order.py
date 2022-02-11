import json

from django.http import JsonResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.api.get_draft_order import GetDraftOrderApi
from economic_dybdahl_rest.api.post_draft_order import PostDraftOrder
from economic_dybdahl_rest.dto.order import Order
from economic_dybdahl_rest.usecases.get_draft_order.get_draft_order import GetDraftOrderUseCase
from economic_dybdahl_rest.usecases.get_draft_order.get_draft_order_listener import GetDraftOrderListener
from tests.dto.test_order import default_order


class OrderEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        order = default_order
        order.layout_number = 20
        order.lines[0].product_number = '3'
        response = PostDraftOrder().post(order)
        decoded = json.loads(response.content.decode('utf-8'))
        return None

    def get(self, request, id):
        api = GetDraftOrderApi()
        response = api.get(id)

        # Can save the pdf
        # with open('/Users/tobiasdybdahl/Desktop/test.pdf', 'wb') as f:
        #    f.write(response.content)
        return None

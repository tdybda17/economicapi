from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.block_product.block_product import BlockProductUseCase
from economic_dybdahl_rest.usecases.block_product.block_product_listener import BlockProductListener


class BlockProductEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, product_number):
        listener = BlockProductListener()
        BlockProductUseCase.block(product_number, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

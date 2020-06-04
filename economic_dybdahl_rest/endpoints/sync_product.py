from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.dto.product import Product
from economic_dybdahl_rest.usecases.sync_product.sync_product import SyncProductUseCase
from economic_dybdahl_rest.usecases.sync_product.sync_product_listener import SyncProductListener


class SyncProductEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        product = Product.from_request(request)
        listener = SyncProductListener()
        SyncProductUseCase.sync(product, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict())

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.dto.product import Product
from economic_dybdahl_rest.usecases.delete_product.delete_product import DeleteProductUseCase
from economic_dybdahl_rest.usecases.delete_product.delete_product_listener import DeleteProductListener
from economic_dybdahl_rest.usecases.get_product.get_product import GetProductUseCase
from economic_dybdahl_rest.usecases.get_product.get_product_listener import GetProductListener
from economic_dybdahl_rest.usecases.sync_product.sync_product import PutProductUseCase
from economic_dybdahl_rest.usecases.sync_product.sync_product_listener import SyncProductListener


class ProductEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        product = Product.from_request(request)
        listener = SyncProductListener()
        PutProductUseCase.put(product, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

    def delete(self, request, product_number):
        listener = DeleteProductListener()
        DeleteProductUseCase.delete(product_number, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

    def get(self, request, product_number):
        listener = GetProductListener()
        GetProductUseCase.get(product_number, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict(), status=response.status_code)

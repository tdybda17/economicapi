from django.http import JsonResponse, Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.dto.product import Product
from economic_dybdahl_rest.usecases.delete_product.delete_product import DeleteProductUseCase
from economic_dybdahl_rest.usecases.delete_product.delete_product_listener import DeleteProductListener
from economic_dybdahl_rest.usecases.get_product.get_product import GetProductUseCase
from economic_dybdahl_rest.usecases.get_product.get_product_listener import GetProductListener
from economic_dybdahl_rest.usecases.get_products_in.get_products_in import GetProductsInUseCase
from economic_dybdahl_rest.usecases.get_products_in.get_products_in_listener import GetProductsInListener
from economic_dybdahl_rest.usecases.get_products_in.product_numbers_string_splitter import split_product_number_string
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

    def get(self, request, product_number=None):
        if product_number:
            listener = GetProductListener()
            GetProductUseCase.get(product_number, listener)
            response = listener.get_response()
            return JsonResponse(data=response.to_dict(), status=response.status_code)
        else:
            product_numbers = request.GET.get('in', None)
            trimmed = split_product_number_string(product_numbers)
            if not trimmed:
                raise Http404()
            else:
                listener = GetProductsInListener()
                GetProductsInUseCase.get(trimmed, listener)
                response = listener.get_response()
                return JsonResponse(data=response.to_dict(), status=response.status_code)

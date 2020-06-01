from django.http import JsonResponse
from django.views import View

from economic_dybdahl_rest.dto.product import Product
from economic_dybdahl_rest.http.headers import Headers
from economic_dybdahl_rest.usecases.sync_product.sync_product import SyncProductUseCase
from economic_dybdahl_rest.usecases.sync_product.sync_product_listener import SyncProductListener


class SyncProductEndpoint(View):

    def post(self, request):
        product = Product.from_request(request)
        listener = SyncProductListener()
        headers = Headers.from_request(request)
        SyncProductUseCase.sync(product, headers, listener)
        response = listener.get_response()
        return JsonResponse(data=response.to_dict())

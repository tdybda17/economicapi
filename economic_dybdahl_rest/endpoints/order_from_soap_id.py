from django.http import JsonResponse, Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_order.get_order import GetOrderListener, GetOrderUseCase
from economic_dybdahl_rest.usecases.get_order.get_orders_in import GetOrdersInListener, GetOrdersInUseCase
from economic_dybdahl_rest.usecases.get_order.soap_ids_string_splitter import split_soap_id_string


class OrderFromSoapIDEndpoint(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id=None):
        if id:
            listener = GetOrderListener()
            GetOrderUseCase.get(id, listener)
            response = listener.get_response()
            return JsonResponse(
                data=response.to_dict(),
                status=response.status_code
            )
        else:
            soap_ids = request.GET.get('in', None)
            trimmed = split_soap_id_string(soap_ids)
            if not trimmed:
                raise Http404()
            listener = GetOrdersInListener()
            GetOrdersInUseCase.get(trimmed, listener)
            response = listener.get_response()
            return JsonResponse(
                data=response.to_dict(),
                status=response.status_code
            )



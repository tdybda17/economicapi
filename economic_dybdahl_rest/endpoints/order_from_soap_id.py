from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_order.get_order import GetOrderListener, GetOrderUseCase


class OrderFromSoapIDEndpoint(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        listener = GetOrderListener()
        GetOrderUseCase.get(id, listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )

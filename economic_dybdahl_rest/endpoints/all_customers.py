from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.sync_customer_data.get_all_customer import GetAllCustomerUseCase
from economic_dybdahl_rest.usecases.sync_customer_data.get_all_customer_listener import GetAllCustomerListener


class AllCustomersEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        listener = GetAllCustomerListener()
        GetAllCustomerUseCase.get(listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )

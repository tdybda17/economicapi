from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_customer.get_customer import GetCustomerUseCase
from economic_dybdahl_rest.usecases.get_customer.get_customer_listener import GetCustomerListener


class CustomersEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, customer_number):
        listener = GetCustomerListener()
        GetCustomerUseCase.get(customer_number, listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )

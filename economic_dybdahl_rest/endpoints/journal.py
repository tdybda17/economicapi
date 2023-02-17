from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.api.post_vouchers import PostVouchers
from economic_dybdahl_rest.usecases.get_customer.get_customer import GetCustomerUseCase
from economic_dybdahl_rest.usecases.get_customer.get_customer_listener import GetCustomerListener


class JournalEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, journal_id):
        response = PostVouchers().post(journal_id, request.data)
        return JsonResponse(
            data=response,
            status=response.status_code
        )

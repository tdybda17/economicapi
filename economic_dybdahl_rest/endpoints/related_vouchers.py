from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.usecases.get_related_vouchers.get_related_vouchers import GetRelatedVouchersListener, \
    GetRelatedVouchersRequest, GetRelatedVouchersUseCase


class RelatedVouchersEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, journal_number, accounting_year, voucher_number):
        listener = GetRelatedVouchersListener()
        request = GetRelatedVouchersRequest(journal_number, accounting_year, voucher_number)
        GetRelatedVouchersUseCase.get(request, listener)
        response = listener.get_response()
        return JsonResponse(
            data=response.to_dict(),
            status=response.status_code
        )

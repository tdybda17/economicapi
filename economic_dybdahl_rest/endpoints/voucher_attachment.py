from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from economic_dybdahl_rest.api.journal_voucher_attachment import JournalVoucherAttachmentAPI


class VoucherAttachmentEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, journal_number, accounting_year, voucher_number):
        try:
            accounting_year_voucher_number = str(accounting_year) + '-' + str(voucher_number)

            response = JournalVoucherAttachmentAPI().patch(journal_number, accounting_year_voucher_number, request.FILES)

            return JsonResponse(data={'msg': 'PDF attached'}, status=response.status_code)

        except Exception as e:
            return JsonResponse(data={'error': str(e)}, status=400)

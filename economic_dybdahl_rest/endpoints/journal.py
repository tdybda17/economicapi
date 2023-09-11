from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json
import base64

from economic_dybdahl_rest.api.get_attachments import Attachment, HasAttachment
from economic_dybdahl_rest.api.post_vouchers import Vouchers
from economic_dybdahl_rest.usecases.get_customer.get_customer import GetCustomerUseCase
from economic_dybdahl_rest.usecases.get_customer.get_customer_listener import GetCustomerListener


class JournalEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, journal_id):
        response = Vouchers().post(journal_id, request.data)

        if response.status_code == 201:
            data = 'Created'
        else:
            json_response = response.json()
            if json_response:
                data = json_response
            else: data = response.content

        return JsonResponse(
            data={'data': data},
            status=response.status_code
        )

    def get(self, request, journal_id):

        response = Vouchers().get(journal_id)

        data = json.loads(response.text)

        vouchers = {
            "collection": []
        }

        for voucher in data['collection']:
            voucher_name = list(voucher['entries'].keys())[0]

            temt_voucher = {}

            temt_voucher['voucher_number'] = voucher['voucherNumber']
            temt_voucher['date'] = voucher['entries'][voucher_name][0]['date']
            temt_voucher['voucher_amount'] = voucher['entries'][voucher_name][0]['amount']
            temt_voucher['accounting_year'] = voucher['accountingYear']['year']

            attc_response = HasAttachment().get(journal_id, voucher['accountingYear']['year'], voucher['voucherNumber'])
            if attc_response.status_code == 200:

                temt_voucher['attachment'] = True if attc_response.json()['pages'] > 0 else False

                #base64.b64encode(attc_response.content).decode('utf-8')

            vouchers["collection"].append(temt_voucher)

        return JsonResponse(data=vouchers, status=response.status_code)

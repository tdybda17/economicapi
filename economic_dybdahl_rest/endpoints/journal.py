from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json
import base64

from economic_dybdahl_rest.api.get_attachments import Attachment, HasAttachment
from economic_dybdahl_rest.api.post_vouchers import Vouchers


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
            else:
                data = response.content

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
            vat_data = None

            try:
                contra_vat_account = voucher['entries'][voucher_name][0]['contraVatAccount']
                vat_data = dict(
                    rate_percentage=contra_vat_account['ratePercentage'],
                    vat_code=contra_vat_account['vatCode'],
                )
            except KeyError:
                pass

            account_number = None
            try:
                account_number = voucher['entries'][voucher_name][0]['supplier']['supplierNumber']
            except KeyError:
                pass

            contra_account_number = None
            try:
                contra_account_number = voucher['entries'][voucher_name][0]['contraAccount']['accountNumber']
            except KeyError:
                pass

            temt_voucher['voucher_number'] = voucher['voucherNumber']
            temt_voucher['date'] = voucher['entries'][voucher_name][0]['date']
            temt_voucher['voucher_amount'] = voucher['entries'][voucher_name][0]['amount']
            temt_voucher['voucher_amount_default_currency'] = voucher['entries'][voucher_name][0][
                'amountDefaultCurrency']
            temt_voucher['accounting_year'] = voucher['accountingYear']['year']
            temt_voucher['account_number'] = account_number
            temt_voucher['contra_account_number'] = contra_account_number
            temt_voucher['contra_vat_account'] = vat_data
            temt_voucher['exchange_rate'] = voucher['entries'][voucher_name][0].get('exchangeRate', None)

            attc_response = HasAttachment().get(journal_id, voucher['accountingYear']['year'], voucher['voucherNumber'])
            if attc_response.status_code == 200:
                temt_voucher['attachment'] = True if attc_response.json()['pages'] > 0 else False

                #base64.b64encode(attc_response.content).decode('utf-8')

            vouchers["collection"].append(temt_voucher)

        return JsonResponse(data=vouchers, status=response.status_code)

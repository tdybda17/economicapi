from dataclasses import dataclass
from http import HTTPStatus

from economic_dybdahl_rest.api.get_journal_voucher import GetJournalVoucherAPI
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class GetRelatedVouchersListener(Listener):
    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'lines': data
            }
        )

    def on_unknown_error(self, error):
        self.response = Response(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            data={
                'detail': error
            }
        )


class GetRelatedVouchersRequest:

    def __init__(self, journal_number, accounting_year, voucher_number):
        self.journal_number = journal_number
        self.accounting_year = accounting_year
        self.voucher_number = voucher_number
        super().__init__()


class GetRelatedVouchersUseCase:

    @staticmethod
    def get(request: GetRelatedVouchersRequest ,listener=None):
        accounting_year_voucher_number = str(request.accounting_year) + '-' + str(request.voucher_number)

        response = GetJournalVoucherAPI().get(request.journal_number, accounting_year_voucher_number)

        if not response.ok:
            listener.on_unknown_error(response.content)
            return

        json_response = response.json()

        listener.on_success(json_response)
        return json_response

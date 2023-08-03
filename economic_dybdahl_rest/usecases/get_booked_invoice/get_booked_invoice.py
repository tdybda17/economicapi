import json
from http import HTTPStatus

from economic_dybdahl_rest.api.get_booked_invoice import GetBookedInvoiceAPI
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class GetBookedInvoiceListener(Listener):
    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'bookedInvoice': json.loads(data.decode("utf-8"))
            }
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class GetBookedInvoiceUseCase:

    @staticmethod
    def get(id, listener=None):
        try:
            economic_response = GetBookedInvoiceAPI().get(id)

            if not economic_response.ok:
                listener.on_unknown_error(content=json.loads(economic_response.content.decode("utf-8")),
                                          status_code=economic_response.status_code)
                return

            listener.on_success(data=economic_response.content)

        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return

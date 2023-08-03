import json
from http import HTTPStatus

from economic_dybdahl_rest.api.list_payment_terms import ListPaymentTermsAPI
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class ListPaymentTermsListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=HTTPStatus.OK,
            data={
                'paymentTerms': data
            }
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class ListPaymentTermsUseCase:

    @staticmethod
    def list(listener=None):
        try:
            payment_terms = []

            next_page = None
            while True:
                response = ListPaymentTermsAPI().get(next_page)

                if not response.ok:
                    listener.on_unknown_error(
                        content=json.loads(response.content.decode("utf-8")),
                        status_code=response.status_code
                    )
                    return

                json_response = response.json()
                for payment_term in json_response['collection']:
                    payment_terms.append(payment_term)

                try:
                    next_page = json_response['pagination']['nextPage']
                except KeyError:
                    break

            listener.on_success(data=payment_terms)
            return
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return

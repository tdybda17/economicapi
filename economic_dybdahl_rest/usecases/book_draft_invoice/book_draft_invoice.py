import json
from dataclasses import dataclass

from economic_dybdahl_rest.api.book_draft_invoice import BookDraftInvoiceAPI, BookDraftInvoiceRequest
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class BookDraftInvoiceListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=200,
            data={
                'bookedInvoice': json.loads(data.decode("utf-8"))
            }
        )

    def on_unknown_error(self, status_code, content):
        content_dict = json.loads(content.decode("utf-8"))
        content_dict['status_code'] = status_code
        self.response = Response(
            status_code=status_code,
            data=content_dict
        )


class BookDraftInvoiceUseCase:

    @staticmethod
    def book(request: BookDraftInvoiceRequest, listener=None):
        try:
            response = BookDraftInvoiceAPI().post(request)

            if not response.ok:
                listener.on_unknown_error(content=response.content, status_code=500)
                return

            listener.on_success(response.content)
            return
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return

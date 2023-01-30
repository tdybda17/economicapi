from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.usecases._listener import Listener


class InvoicesDraftsListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            status_code=200,
            data=data
        )

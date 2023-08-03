import json
import requests

from economic_dybdahl_rest.api.draft_invoices import PostInvoicesDraft
from economic_dybdahl_rest.api.get_all_customers import GetAllCustomersApi
from economic_dybdahl_rest.api.get_contacts import GetContactsApi
from economic_dybdahl_rest.api.get_customer import GetCustomerApi
from economic_dybdahl_rest.dto.customer import Customer
from economic_dybdahl_rest.dto.delivery_location import DeliveryLocation
from economic_dybdahl_rest.usecases.invoices_drafts.invoices_drafts_listerner import InvoicesDraftsListener


class PostInvoicesDraftsUseCase:

    @staticmethod
    def post(request, listener: InvoicesDraftsListener):

        invoice = request.data['invoice']

        api = PostInvoicesDraft()
        response = api.post(invoice)

        if response.status_code == 201:

            listener.on_success(response.content)
        else:
            listener.on_unknown_error(response.status_code, response.content)

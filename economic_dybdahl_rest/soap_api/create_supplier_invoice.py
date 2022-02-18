from economic_dybdahl_rest.api.get_products import GetProducts
from economic_dybdahl_rest.dto.supplier_invoice import SupplierInvoice
from economic_dybdahl_rest.http.response import Response
from economic_dybdahl_rest.soap_api._soap_api import EconomicSOAPApi
from economic_dybdahl_rest.usecases._listener import Listener


class CreateSupplierInvoiceAPIListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            data={'id': data},
            status_code=200
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )


class CreateSupplierInvoiceWithLinesAPIListener(Listener):

    def on_success(self, data=None):
        self.response = Response(
            data={'invoice': data},
            status_code=200
        )

    def on_unknown_error(self, status_code, content):
        self.response = Response(
            data={'message': content},
            status_code=status_code
        )

    def on_product_does_not_exist(self, product):
        self.response = Response(
            data={'message': 'Produkt ' + str(product) + ' Eksistere ikke i economic, eller er uden lagerstyring'},
            status_code=400
        )


class CreateSupplierInvoiceAPI(EconomicSOAPApi):

    def __init__(self) -> None:
        super().__init__()

    def create_supplier_invoice(self, creditor_nr, invoice_nr,
                                listener=CreateSupplierInvoiceAPIListener()):
        creditor_nr = creditor_nr
        invoice_nr = invoice_nr
        try:
            response = self.client.service.CurrentSupplierInvoice_CreateFromData(data={
                'Handle': {
                    'Id': 1
                },
                'Id': 1,
                'InvoiceNo': invoice_nr,
                'CreditorHandle': {
                    'Number': creditor_nr
                }
            })
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        listener.on_success(response)
        return response

    def create_supplier_invoice_with_lines(self, creditor_nr, invoice_nr, lines,
                                           listener=CreateSupplierInvoiceWithLinesAPIListener()):
        creditor_nr = creditor_nr
        invoice_nr = invoice_nr
        lines = lines

        try:
            products_numbers = get_product_numbers_in_economic_from_lines(lines)
        except UnknownErrorException as e:
            listener.on_unknown_error(500, str(e))
            return

        for line in lines:
            if str(line['product_nr']) not in products_numbers:
                listener.on_product_does_not_exist(line['product_nr'])
                return

        try:
            invoice_id = self.client.service.CurrentSupplierInvoice_CreateFromData(data={
                'Handle': {
                    'Id': 1
                },
                'Id': 1,
                'InvoiceNo': invoice_nr,
                'CreditorHandle': {
                    'Number': creditor_nr
                }
            })

            data_array = []

            for line in lines:
                temp = {
                    'Handle': {
                        'InvoiceId': invoice_id,
                        'Number': 1,
                    },
                    'InvoiceId': invoice_id,
                    'Number': 1,
                    'InvoiceHandle': {
                        'Id': invoice_id
                    },
                    'ProductHandle': {
                        'Number': line['product_nr']
                    },
                    'Quantity': line['amount'],
                    'UnitPrice': line['price']
                }

                data_array.append(temp)

            response = self.client.service.CurrentSupplierInvoiceLine_CreateFromDataArray(dataArray={
                'CurrentSupplierInvoiceLineData': data_array
            })
        except Exception as e:
            listener.on_unknown_error(content=str(e), status_code=500)
            return
        invoice = SupplierInvoice(
            supplier_nr=creditor_nr,
            comment=invoice_nr,
            lines=lines,
            invoice_id=invoice_id
        )
        listener.on_success(invoice.to_dict())
        return response


def get_product_numbers_in_economic_from_lines(lines):
    lines_product_numbers = []
    for line in lines:
        lines_product_numbers.append(str(line['product_nr']))

    products = []
    get_products_api = GetProducts()
    response = get_products_api.get(lines_product_numbers)
    if response.status_code > 300:
        raise UnknownErrorException(str(response.status_code) + ': ' + str(response.content))
    products.extend(response.json()['collection'])
    pagination = response.json()['pagination']

    while 'nextPage' in pagination:
        response = get_products_api.get_next_page(pagination['nextPage'])
        if response.status_code > 300:
            raise UnknownErrorException(str(response.status_code) + ': ' + str(response.content))
        products.extend(response.json()['collection'])
        pagination = response.json()['pagination']

    product_numbers = []
    for product in products:
        if 'inventoryEnabled' not in product['productGroup']:
            continue
        product_numbers.append(product['productNumber'])

    return product_numbers


class UnknownErrorException(RuntimeError):
    pass

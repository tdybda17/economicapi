from django.urls import path

from economic_dybdahl_rest.endpoints.all_customers import AllCustomersEndpoint
from economic_dybdahl_rest.endpoints.attachment import AttachmentEndpoint
from economic_dybdahl_rest.endpoints.block_product import BlockProductEndpoint
from economic_dybdahl_rest.endpoints.booked_invoice import BookedInvoiceEndpoint
from economic_dybdahl_rest.endpoints.customers import CustomersEndpoint
from economic_dybdahl_rest.endpoints.draft_orders_lines import DraftOrdersLinesEndpoint
from economic_dybdahl_rest.endpoints.invoices_drafts import InvoicesDraftEndpoint, BookDraftInvoiceEndpoint
from economic_dybdahl_rest.endpoints.journal import JournalEndpoint
from economic_dybdahl_rest.endpoints.journals import JournalsEndpoint
from economic_dybdahl_rest.endpoints.order_from_soap_id import OrderFromSoapIDEndpoint
from economic_dybdahl_rest.endpoints.payment_terms import PaymentTermsEndpoint
from economic_dybdahl_rest.endpoints.product import ProductEndpoint
from economic_dybdahl_rest.endpoints.supplier_invoice import SupplierInvoiceWithLinesEndpoint, \
    SupplierInvoiceAllEndpoint

# Product
urlpatterns = [
    path('v1/product/', ProductEndpoint.as_view(), name='sync product endpoint'),
    path('v1/product/<str:product_number>/', ProductEndpoint.as_view(), name='product endpoint'),
    path('v1/product/<str:product_number>/block/', BlockProductEndpoint.as_view(), name='block product endpoint'),
]

# Customers
urlpatterns += [
    path('v1/customers/', AllCustomersEndpoint.as_view(), name='get all customer numbers endpoint'),
    path('v1/customers/<str:customer_number>/', CustomersEndpoint.as_view(), name='get all customer numbers endpoint'),
]

# Journals
urlpatterns += [
    path('v1/journals/<int:journal_id>/', JournalEndpoint.as_view(), name='post journals endpoint'),
    path('v1/journals/<int:journal_id>/attachment/<int:accounting_year>/<int:attachment_id>/', AttachmentEndpoint.as_view(), name='post journals endpoint'),
    path('v1/journals/', JournalsEndpoint.as_view(), name='Journals')
]

# Draft invoices
urlpatterns += [
    path('v1/invoices_draft/', InvoicesDraftEndpoint.as_view(), name='post a invoice'),
    path('v1/invoices_draft/<int:draft_invoice_number>/book/', BookDraftInvoiceEndpoint.as_view(),
         name='book a draft invoice'),
]

# Booked invoices
urlpatterns += [
    path('v1/invoices_booked/<int:booked_id>/', BookedInvoiceEndpoint.as_view(), name='get booked invoice'),
]

# Orders
urlpatterns += [
    path('v1/orders/drafts/lines/', DraftOrdersLinesEndpoint.as_view(), name='get all draft orders lines'),
    path('v1/orders/<int:soap_id>/', OrderFromSoapIDEndpoint.as_view(),
         name='get order from a soap id or soap id list'),
    path('v1/orders/', OrderFromSoapIDEndpoint.as_view(), name='get order from a soap id or soap id list'),
]

# Payment terms
urlpatterns += [
    path('v1/payment-terms/', PaymentTermsEndpoint.as_view(), name='Payment terms'),
]

# Supplier invoice
urlpatterns += [
    path('v1/supplier/invoice/', SupplierInvoiceWithLinesEndpoint.as_view(), name='supplier invoice with lines'),
    path('v1/supplier/invoice/<int:id>/', SupplierInvoiceWithLinesEndpoint.as_view(),
         name='supplier invoice with lines'),
    path('v1/supplier/invoice/all/', SupplierInvoiceAllEndpoint.as_view(),
         name='supplier invoice with lines'),
]

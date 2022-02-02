from django.urls import path

from economic_dybdahl_rest.endpoints.block_product import BlockProductEndpoint
from economic_dybdahl_rest.endpoints.customers import CustomersEndpoint
from economic_dybdahl_rest.endpoints.draft_orders_lines import DraftOrdersLinesEndpoint
from economic_dybdahl_rest.endpoints.product import ProductEndpoint
from economic_dybdahl_rest.endpoints.supplier_invoice import SupplierInvoiceWithLinesEndpoint, \
    SupplierInvoiceAllEndpoint

urlpatterns = [
    path('v1/product/', ProductEndpoint.as_view(), name='sync product endpoint'),
    path('v1/product/<str:product_number>/', ProductEndpoint.as_view(), name='product endpoint'),
    path('v1/product/<str:product_number>/block/', BlockProductEndpoint.as_view(), name='block product endpoint'),
    path('v1/customers/<str:customer_number>/', CustomersEndpoint.as_view(), name='get customer endpoint'),
    path('v1/supplier/invoice/', SupplierInvoiceWithLinesEndpoint.as_view(), name='supplier invoice with lines'),
    path('v1/supplier/invoice/<int:id>/', SupplierInvoiceWithLinesEndpoint.as_view(),
         name='supplier invoice with lines'),
    path('v1/supplier/invoice/all/', SupplierInvoiceAllEndpoint.as_view(),
         name='supplier invoice with lines'),
    path('v1/customers/<str:customer_number>/', CustomersEndpoint.as_view(), name='get customer endpoint'),
    path('v1/orders/drafts/lines/', DraftOrdersLinesEndpoint.as_view(), name='get all draft orders lines')
]

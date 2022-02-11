from django.urls import path

from economic_dybdahl_rest.endpoints.block_product import BlockProductEndpoint
from economic_dybdahl_rest.endpoints.customers import CustomersEndpoint
from economic_dybdahl_rest.endpoints.order import OrderEndpoint
from economic_dybdahl_rest.endpoints.product import ProductEndpoint

urlpatterns = [
    path('v1/product/', ProductEndpoint.as_view(), name='sync product endpoint'),
    path('v1/product/<str:product_number>/', ProductEndpoint.as_view(), name='product endpoint'),
    path('v1/product/<str:product_number>/block/', BlockProductEndpoint.as_view(), name='block product endpoint'),
    path('v1/customers/<str:customer_number>/', CustomersEndpoint.as_view(), name='get customer endpoint'),
    path('v1/order/draft/<int:id>/', OrderEndpoint.as_view(), name='get/put draft order endpoint'),
    path('v1/order/draft/', OrderEndpoint.as_view(), name='post draft order endpoint'),
]

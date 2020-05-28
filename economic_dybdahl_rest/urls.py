from django.urls import path

# from economic_dybdahl_rest.endpoints.order import OrderEndpoint
from economic_dybdahl_rest.endpoints.sync_product import SyncProductEndpoint

urlpatterns = [
    # path('v1/order/', OrderEndpoint.as_view(), name='order endpoint'),
    path('v1/sync-product', SyncProductEndpoint.as_view(), name='sync product endpoint'),
]

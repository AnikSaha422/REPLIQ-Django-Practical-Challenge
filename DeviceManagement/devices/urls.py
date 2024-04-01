from django.urls import path
from .views.deviceView import DeviceListCreate, DeviceDetail
from .views.checkoutView import CheckoutListCreate, CheckoutDetail

urlpatterns = [
    path("devices/", DeviceListCreate.as_view(), name="device-list-create"),
    path(
        "devices/<int:pk>/",
        DeviceDetail.as_view(),
        name="device-detail",
    ),
    path("checkouts/", CheckoutListCreate.as_view(), name="checkout-list-create"),
    path("checkouts/<int:pk>/", CheckoutDetail.as_view(), name="checkout-detail"),
]

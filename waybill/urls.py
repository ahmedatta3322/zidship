from django.urls import path
from . import views

urlpatterns = [
    path("waybill/", views.WayBillListCreate.as_view()),
    path(
        "waybill/print/<int:id>/<str:printer_name>/", views.PrintWayBill.as_view()
    ),  # <int:id> is the primary key of the waybill
    path("waybill/sender/", views.SenderListCreate.as_view()),
    path("waybill/receiver/", views.ReceiverListCreate.as_view()),
    path("waybill/shipment/", views.ShipmentListCreate.as_view()),
    path("waybill/shipment/track/<int:id>/", views.TrackShipmentStatus.as_view()),
    path("waybill/shipment/map/<int:id>/", views.MapShipmentStatus.as_view()),
]


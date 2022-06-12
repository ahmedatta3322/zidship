from .models import WayBill, Sender, Receiver, Shipment
from .serializers import (
    WayBillSerializer,
    SenderSerializer,
    ReceiverSerializer,
    ShipmentSerializer,
)
from .services import WayBillServices
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics


class WayBillListCreate(generics.ListCreateAPIView):
    queryset = WayBill.objects.all()
    serializer_class = WayBillSerializer


class SenderListCreate(generics.ListCreateAPIView):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer


class ReceiverListCreate(generics.ListCreateAPIView):
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer


class ShipmentListCreate(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class PrintWayBill(generics.RetrieveAPIView):
    queryset = WayBill.objects.all()
    serializer_class = WayBillSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        waybill = self.get_object()
        WayBillServices.print_waybill(waybill, kwargs["printer_name"])
        return Response(
            {
                "message": "Waybill printed , you will find the PDF in your Directory folder"
            }
        )


class TrackShipmentStatus(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        shipment = self.get_object()
        return Response({"message": "Shipment status is " + shipment.shipment_status})


class MapShipmentStatus(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        shipment = self.get_object()
        WayBillServices.map_shipment_status(shipment)
        return Response({"message": "Shipment status is " + shipment.shipment_status})

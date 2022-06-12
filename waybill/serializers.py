from rest_framework.serializers import ModelSerializer
from .models import WayBill, Sender, Receiver, Shipment


class WayBillSerializer(ModelSerializer):
    class Meta:
        model = WayBill
        fields = "__all__"


class SenderSerializer(ModelSerializer):
    class Meta:
        model = Sender
        fields = "__all__"


class ReceiverSerializer(ModelSerializer):
    class Meta:
        model = Receiver
        fields = "__all__"


class ShipmentSerializer(ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"

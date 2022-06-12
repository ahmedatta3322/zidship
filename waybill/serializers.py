from rest_framework.serializers import ModelSerializer
from .models import WayBill


class WayBillSerializer(ModelSerializer):
    class Meta:
        model = WayBill
        fields = "__all__"

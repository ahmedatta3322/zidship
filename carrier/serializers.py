from rest_framework import serializers
from .models import Carrier, CarrierFunction


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = "__all__"


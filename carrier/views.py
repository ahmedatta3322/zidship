from django.shortcuts import render
from .models import Carrier, CarrierFunction
from .serializers import CarrierSerializer, CarrierFunctionSerializer

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response


class CarrierListCreate(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer


class CarrierFunctionListCreate(generics.ListCreateAPIView):
    queryset = CarrierFunction.objects.all()
    serializer_class = CarrierFunctionSerializer


class RemoveFunction(generics.RetrieveAPIView):
    queryset = CarrierFunction.objects.all()
    serializer_class = CarrierFunctionSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        carrier_function = self.get_object()
        carrier_function.delete()
        return Response({"message": "Carrier Function removed"})

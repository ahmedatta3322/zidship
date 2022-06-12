from django.shortcuts import render
from .models import Carrier, CarrierFunction
from .serializers import CarrierSerializer

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response


class CarrierListCreate(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer


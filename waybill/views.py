from .models import WayBill
from .serializers import WayBillSerializer
from .services import WayBillService
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics


class WayBillListCreate(generics.ListCreateAPIView):
    queryset = WayBill.objects.all()
    serializer_class = WayBillSerializer


class PrintWayBill(generics.RetrieveAPIView):
    queryset = WayBill.objects.all()
    serializer_class = WayBillSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        waybill = self.get_object()
        service = WayBillService(waybill)
        service.print_waybill()
        return Response({"message": "Waybill printed"})

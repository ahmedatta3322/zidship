from waybill.models import WayBill
from zidship.base import BaseModel
from django.db import models


class Carrier(BaseModel):
    """
    Carrier Sections
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    carrier_functions = models.ManyToManyField("CarrierFunction", blank=True)

    class Meta:
        verbose_name_plural = "Carriers"

    def __str__(self):
        return self.name

    def create_waybill(self, shipment, sender, receiver, packages):
        return WayBill.objects.create(
            carrier=self,
            shipment=shipment,
            sender=sender,
            receiver=receiver,
            packages=packages,
        )

    def get_waybills(self):
        return WayBill.objects.filter(carrier=self)

    def get_waybills_count(self):
        return WayBill.objects.filter(carrier=self).count()


class CarrierFunction(BaseModel):
    """
    Carrier Function Sections
    """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Carrier Functions"

    def __str__(self):
        return self.name

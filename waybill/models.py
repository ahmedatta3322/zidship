from django.dispatch import receiver
from zidship.base import BaseModel
from django.db import models
import uuid

# Create your BaseModel here.
class WayBill(BaseModel):

    """
    Way Bill Sections
    """

    # Way Bill Number
    way_bill_number = models.UUIDField(
        max_length=255, unique=True, default=uuid.uuid4, editable=False
    )

    # Way Bill Label
    way_bill_label = models.CharField(max_length=255)

    carrier = models.ForeignKey("carrier.Carrier", on_delete=models.CASCADE)
    # Shipper
    sender = models.ForeignKey("Sender", on_delete=models.CASCADE)

    # Receiver
    receiver = models.ForeignKey("Receiver", on_delete=models.CASCADE)

    # Shipment
    shipment = models.OneToOneField("Shipment", on_delete=models.CASCADE)

    def __str__(self):
        return self.way_bill_label


class Sender(BaseModel):
    """
    Sender Sections
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Senders"

    def __str__(self):
        return self.name


class Receiver(BaseModel):
    """
    Receiver Sections
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Receivers"

    def __str__(self):
        return self.name


class Package(BaseModel):

    """
    Package Sections
    """

    weight = models.FloatField()
    package_type = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    shipment = models.ForeignKey(
        "Shipment", on_delete=models.CASCADE, related_name="packages"
    )

    class Meta:
        verbose_name_plural = "Packages"

    def __str__(self):
        return self.package_type


class Shipment(BaseModel):

    """
    Shipment Sections
    """

    statuses = ("In Transit", "Delivered", "Cancelled", "Returned")

    # Shipment Number
    shipment_number = models.UUIDField(
        max_length=255, unique=True, default=uuid.uuid4, editable=False
    )
    # Fragile
    fragile = models.BooleanField(default=False)
    # Shipment Date
    shipment_date = models.DateField()
    # Shipment Type
    shipment_type = models.CharField(max_length=100)  # e.g. "Air", "Ground", "Sea"
    # Shipment Status
    shipment_status = models.CharField(
        max_length=100, choices=tuple([(status, status) for status in statuses])
    )  # e.g. "Pending", "In Transit", "Delivered"
    # Shipment Notes
    shipment_notes = models.CharField(max_length=300)

    def __str__(self):
        return str(self.shipment_number)

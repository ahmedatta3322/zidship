from zidship.base import BaseModel
from django.db import models

# Create your BaseModel here.
class WayBill(BaseModel):

    """
    Way Bill Sections
    """

    # Way Bill Number
    way_bill_number = models.CharField(max_length=255, unique=True)

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
        return self.way_bill_number


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
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Senders"


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
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Receivers"


class Package(BaseModel):

    """
    Package Sections
    """

    weight = models.FloatField()
    package_type = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Packages"


class Shipment(BaseModel):

    """
    Shipment Sections
    """

    # Shipment Number
    shipment_number = models.CharField(max_length=255, unique=True)
    # Fragile
    fragile = models.BooleanField(default=False)
    # Shipment Date
    shipment_date = models.DateField()
    # Shipment Type
    shipment_type = models.CharField(max_length=100)  # e.g. "Air", "Ground", "Sea"
    # Shipment Status
    shipment_status = models.CharField(
        max_length=100
    )  # e.g. "Pending", "In Transit", "Delivered"
    # Shipment Notes
    shipment_notes = models.CharField(max_length=300)
    # Shipment Package
    shipment_package = models.ForeignKey("Package", on_delete=models.CASCADE)

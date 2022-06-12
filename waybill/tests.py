from django.test import TestCase
from rest_framework.test import APIRequestFactory

from . import views

# Create your tests here.
class TestViews(TestCase):
    def test_waybill_list_create(self):
        factory = APIRequestFactory()
        request = factory.get("/waybill/")
        response = views.WayBillListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_sender_list_create(self):
        factory = APIRequestFactory()
        request = factory.get("/sender/")
        response = views.SenderListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_receiver_list_create(self):
        factory = APIRequestFactory()
        request = factory.get("/receiver/")
        response = views.ReceiverListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_shipment_list_create(self):
        factory = APIRequestFactory()
        request = factory.get("/shipment/")
        response = views.ShipmentListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)


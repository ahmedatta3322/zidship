from django.test import TestCase
from rest_framework.test import APIRequestFactory

from . import views

# Create your tests here.

# Test for the views.py file
class TestViews(TestCase):
    def test_carrier_list_create(self):
        factory = APIRequestFactory()
        request = factory.get("/courier/")
        response = views.CarrierListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_carrier_function_list_create(self):
        factory = APIRequestFactory()
        request = factory.get("/courier/function/")
        response = views.CarrierFunctionListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_remove_function(self):
        factory = APIRequestFactory()
        # add a carrier function first
        request = factory.post(
            "/courier/function/", {"name": "test", "description": "test"}
        )
        response = views.CarrierFunctionListCreate.as_view()(request)
        self.assertEqual(response.status_code, 201)
        # remove the carrier function
        request = factory.get("/courier/function/1/")
        response = views.RemoveFunction.as_view()(request, id=1)
        self.assertEqual(response.status_code, 200)


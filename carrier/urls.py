from django.urls import path
from . import views

urlpatterns = [
    path("courier/", views.CarrierListCreate.as_view()),
    path("courier/<int:id>/", views.CarrierListCreate.as_view()),
    path("courier/<int:id>/function/", views.CarrierFunctionListCreate.as_view()),
    path("courier/function/<int:id>/", views.RemoveFunction.as_view()),
]

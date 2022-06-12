from django.contrib import admin
from .models import Carrier, CarrierFunction

# Register your models here.


class CarrierAdmin(admin.ModelAdmin):
    pass


class CarrierFunctionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Carrier, CarrierAdmin)
admin.site.register(CarrierFunction, CarrierFunctionAdmin)

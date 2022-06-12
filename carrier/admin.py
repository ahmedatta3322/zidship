from django.contrib import admin
from .models import Carrier

# Register your models here.


class CarrierAdmin(admin.ModelAdmin):
    pass


admin.site.register(Carrier, CarrierAdmin)

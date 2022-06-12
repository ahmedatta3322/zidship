from django.contrib import admin
from .models import WayBill, Sender, Receiver, Shipment, Package

# Register your models here.


class WayBillAdmin(admin.ModelAdmin):
    pass


class SenderAdmin(admin.ModelAdmin):
    pass


class ReceiverAdmin(admin.ModelAdmin):
    pass


class ShipmentAdmin(admin.ModelAdmin):
    pass


class PackageAdmin(admin.ModelAdmin):
    pass


admin.site.register(WayBill, WayBillAdmin)
admin.site.register(Sender, SenderAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Package, PackageAdmin)

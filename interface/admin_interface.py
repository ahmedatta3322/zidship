from carrier.models import Carrier, CarrierFunction
class CouriersAdminInterface:
    def create_courier(self, courier):
        courier = Carrier(**courier).save()
        return courier

    def delete_courier(self, courier):
        courier = Carrier.objects.get(id=courier.id).delete()
        return courier

    def update_courier(self, courier):
        courier = Carrier.objects.get(id=courier.id).update(**courier)
        return courier

    def get_courier_functions(self, courier):
        functions = CarrierFunction.objects.filter(carrier=courier)
        return functions

    def set_courier_functions(self, courier, functions):
        functions = CarrierFunction.objects.filter(id__in=functions)
        courier.carrier_functions.set(functions)

from django.contrib import admin

# Register your models here.
from .models import ShippingProvider, DispenseCoolerBox, Delivery
# Register your models here.

admin.site.register(ShippingProvider)
admin.site.register(DispenseCoolerBox)
admin.site.register(Delivery)

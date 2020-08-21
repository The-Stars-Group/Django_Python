from django.contrib import admin

# Register your models here.
from .models import Customer, ShippingAddress
# Register your models here.

admin.site.register(Customer)
admin.site.register(ShippingAddress)

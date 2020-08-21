from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import Order
# Create your models here.
class ShippingProvider(models.Model):
    name = models.CharField(max_length=10)
    date_joined = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharF(max_length=25)


    def __str__(self):
        return self.name()


class DispenserCoolerBox(models.Model):      
    box_number = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=150)
    unlock_code = models.IntegerField()



    def __str__(self):
        return self.location()



class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    shipping_provider = models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    #cooler_box = models.ForeignKey(Cooler, on_delete=models.CASCADE)


    def __str__(self):
            return self.order()


        



     
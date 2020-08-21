from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ShippingProvider(models.Model):
    name = models.CharField(max_length=10)
    date_joined = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharF(max_length=25)


    def __str__(self):
        return self.shippingprovider()


class DispenserCoolerBox(models.Model):      
     box_number = models.IntegerField()
     location = models.CharField()
     unlock_code = models.IntegerField
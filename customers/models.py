
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.get_full_name()


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=8)
    notes = models.TextField(max_length=150)

    def __str__(self):
        return self.shippingaddress()
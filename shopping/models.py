from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateField()
    status = models.CharField(max_length=100)
    Basket = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    payment = models.ForeignKey('self', on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('self', on_delete=models.CASCADE)
    order_price = models.DecimalField(decimal_places=4)
    shipping_cost = models.DecimalField(decimal_places=3)
    total_cost = models.DecimalField(decimal_places=6)

    def __str__(self):
        return self.order()

class Payment(models.Model):
   custom= models.ForeignKey('self', on_delete=models.CASCADE)
   payment_method =models.CharField(max_length=50)
   orderer = models.ForeignKey('self', on_delete=models.CASCADE)
   amount = models.DecimalField(decimal_places=8)
   date_of_payment = models.DateTimeField()

   def __str__(self):
        return self.payment()


class Cart(models.Model):
    product = models.OneToOneField('self', on_delete=models.CASCADE)
    data_created = models.DateTimeField()
    total_price = models.DecimalField(decimal_places=5)
    status = models.CharField(max_length=80)

    def __str__(self):
        return self.cart()
 
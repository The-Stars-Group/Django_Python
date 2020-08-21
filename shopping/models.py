from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import Customer
# Create your models here.


class Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    data_created = models.DateTimeField()
    total_price = models.DecimalField(decimal_places=5)
    status = models.CharField(max_length=80)

    def __str__(self):
        return self.cart()


class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateField()
    status = models.CharField(max_length=100)
    basket = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='+')
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('ShippingProvider', on_delete=models.CASCADE)
    order_price = models.DecimalField(decimal_places=4, max_length=9)
    shipping_cost = models.DecimalField(decimal_places=3, max_digits=5)
    total_cost = models.DecimalField(decimal_places=4, max_digits=4)


    def __str__(self):
        return self.order()

class Payment(models.Model):
   custom= models.ForeignKey(Customer, on_delete=models.CASCADE)
   payment_method =models.CharField(max_length=60)
   order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
   amount = models.DecimalField(decimal_places=8, max_digits=7)
   date_of_payment = models.DateTimeField()

   def __str__(self):
        return self.customer.get_full_name()


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data_created = models.DateTimeField()
    total_price = models.DecimalField(decimal_places=5)
    status = models.CharField(max_length=80)

    def __str__(self):
        return self.cart()
 


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product
from customers.models import Customer
# Create your models here.


class Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    data_created = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=5)
    status = models.CharField(max_length=80)

    def __str__(self):
        return self.cart()
    
    

class Payment(models.Model):
   custom= models.ForeignKey(Customer, on_delete=models.CASCADE)
   payment_method =models.CharField(max_length=60)
#    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
   amount = models.DecimalField(decimal_places=8, max_digits=10)
   date_of_payment = models.DateTimeField()

   def __str__(self):
        return self.customer()

class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateField()
    status = models.CharField(max_length=100)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider', on_delete=models.CASCADE)
    order_price = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=9)
    shipping_cost = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=5)
    total_cost = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=4)


    def __str__(self):
        return self.order_number()





 
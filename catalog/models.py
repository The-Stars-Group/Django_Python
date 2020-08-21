# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# class ProductSuppliier(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email_address = models.EmailField()
#     phone_number = models.IntegerField()
#     date_added = models.DateField()
#     id_number = models.IntegerField()
#     profile_picture = models.ImageField()

    
#     class ProductCategory(models.Model):

#     name= models.CharField()
#     description = models.EmailField()
#     icon = models.ImageField()


# class Product(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     title = models.CharField()
#     category = models.ProductCategory()
#     description= models.TextField()
#     supplier_price = models.DecimalField()
#     selling_price = models.DecimalField()
#     supplier = models.ProductSupplier()
#     date_added = models.DateField()
#     id_number = models.IntegerField()
#     profile_picture = models.ImageField()
#     kiosk = models.Kiosk()
#     number_in_stock = models.IntegerField()
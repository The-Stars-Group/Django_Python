from django.urls import path
from . import views
from .views import upload_kiosk

urlpatterns = [
    # path('', products_list, name='products-list'),
    # path('products/<int:product_id>/',product_details, name='product-details'),
    # path('products/upload/', upload_product, name='upload-product'),
    path('kiosk/upload/', upload_kiosk, name='upload-kiosk'),
]

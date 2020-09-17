from django.shortcuts import render, redirect
from . models import Product 
from . forms import ProductForm

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})



def product_details(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'products': products})

def upload_product(request):
    if request.method == "POST":
         form = ProductForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('products_list')
    else:
       form = ProductForm()
       return render(request,'upload_product.html',{'form':form})
# Create your views here.

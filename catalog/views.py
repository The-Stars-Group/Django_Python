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
    form = ProductForm()
    if request.method == "POST":
         form = ProductForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            return redirect('product-details.')
    else:
       form = ProductForm()
       return render(request, 'upload_product.html', {'form':form})


       def add_to_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(
                book=book,
                cart=self,
                quantity=1
                )
            new_order.save()

            def __unicode__(self):
                return "%s" % (self.book_id)
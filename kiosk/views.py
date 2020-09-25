from django.shortcuts import render, redirect
from . models import Kiosk
from . forms import KioskForm


def upload_kiosk(request):
    form = KioskForm()
    if request.method == "POST":
         form = KioskForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('Upload product-list')
    else:
       form = KioskForm()
       return render(request,'upload_product.html',{'form':form})
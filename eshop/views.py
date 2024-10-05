from django.shortcuts import render 
from product.models import Product 


def home(request):
    products = Product.objects.all().filter(available=True)
    context = {
        'products':products,
    }
    return render(request, 'home.html',context)
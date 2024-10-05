from django.shortcuts import render, get_object_or_404
from django.http import Http404


from .models import Product 

def store(request, category_slug=None):

    if category_slug != None:
        products = Product.objects.filter(category__slug=category_slug).filter(available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request,'product/store.html',context)

def product_details(request,category_slug, slug):
    
    try:
        product = Product.objects.get(category__slug=category_slug, slug=slug)
    except Product.DoesNotExist:
        raise Http404
    
    context = {
        'product': product,
    }
    return render(request, 'product/product_details.html', context)
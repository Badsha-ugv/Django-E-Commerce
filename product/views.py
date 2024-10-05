from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .models import Product
from cart.models import Cart, CartItem
from cart.views import _cart_id


def store(request, category_slug=None):

    if category_slug != None:
        products = Product.objects.filter(category__slug=category_slug).filter(
            available=True
        )
        paginator = Paginator(products, 2)
        page = request.GET.get("page")
        products_ = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get("page")
        products_ = paginator.get_page(page)
        product_count = products.count()

    context = {
        "products": products_,
        "product_count": product_count,
    }
    return render(request, "product/store.html", context)


def product_details(request, category_slug, slug):

    try:
        product = Product.objects.get(category__slug=category_slug, slug=slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product
        ).exists()
    except Product.DoesNotExist:
        raise Http404

    context = {
        "product": product,
        "in_cart": in_cart,
    }
    return render(request, "product/product_details.html", context)


def search_products(request):
    query = request.GET.get("q")

    if query:
        products = Product.objects.filter(name__icontains=query, available=True)
        # paginator = Paginator(products, 1)
        # page = request.GET.get("page")
        # products_ = paginator.get_page(page)
        product_count = products.count()
        context = {
            "products": products,
            "product_count": product_count,
            "query": query,
        }
    else:
        return redirect("store")
    return render(request, "product/store.html", locals())  # lazy developer :)

from django.shortcuts import render, get_object_or_404, redirect

from product.models import Product 
from .models import Cart, CartItem
# Create your views here.
def cart(request, total=0, quantity=0, cart_item=None):

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except:
        pass 
    tax = (2*total)/100
    grand_total = (total+tax)
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
        
    }
    return render(request, 'cart/cart.html', context)


def _cart_id(request):
    cart = request.session.session_key
    print(cart)
    if not cart:
        cart = request.session.create()
    return cart 

def add_to_cart(request,product_id):

    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')
        print('color and size',color,size)

    product = get_object_or_404(Product, id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    print(cart_item.product)
    return redirect('cart')


def decrement_item_quantity(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')
    
def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

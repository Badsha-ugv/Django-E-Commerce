from .models import Cart , CartItem
from .views import _cart_id


def cart_count(request):
    cart_id = _cart_id(request)
    cart_count = 0
    if cart_id:
        cart = Cart.objects.get(cart_id=cart_id)
        cart_items = CartItem.objects.all().filter(cart=cart)
        cart_count = cart_items.count()
        return {'cart_count': cart_count}
    else:
        return {'cart_count': 0}
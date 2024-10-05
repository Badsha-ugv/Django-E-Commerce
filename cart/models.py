from django.db import models

from product.models import Product

class Cart(models.Model):
    cart_id = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart ID: {self.cart_id}'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'CartItem: {self.id}'
from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:product_id>',views.remove_cart,name='remove_cart'),
    path('decrement/<int:product_id>',views.decrement_item_quantity,name='decrement_item_quantity'),


]
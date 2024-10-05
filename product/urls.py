from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='product_by_category'),
    path('<slug:category_slug>/<slug:slug>/',views.product_details,name='product_details'),
    
]
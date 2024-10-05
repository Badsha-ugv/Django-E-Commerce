from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name','category', 'available']
admin.site.register(Product, ProductAdmin)

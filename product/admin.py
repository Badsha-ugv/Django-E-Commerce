from django.contrib import admin
from .models import Category, Product, Product_variant


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name','category', 'available']
admin.site.register(Product, ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'variant_type', 'variant_value','status']

admin.site.register(Product_variant, ProductVariantAdmin)
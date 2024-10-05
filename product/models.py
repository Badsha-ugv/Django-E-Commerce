from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/category/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, upload_to='images/product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_details', args=(self.category.slug, self.slug))
    
    def __str__(self):
        return f'{self.name} from {self.category.name}'


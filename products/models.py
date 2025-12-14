from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name} - {self.price}' 
from django.db import models
from categories.models import Category
from vendors.models import Vendor

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                 related_name='products')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField()
    stock = models.IntegerField(default=True)
    size = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    # material = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    size = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color}"
    
    

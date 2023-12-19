from django.db import models
from categories.models import Category
# from vendors.models import Vendor

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                 related_name='products')
    # vendor = models.ForeignKey(Vendor, 
    #                            on_delete=models.SET_NULL, 
    #                            null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image = models.ImageField(upload_to='uploads/products/')
    available = models.BooleanField()
    stock = models.IntegerField(default=True)
    size = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    # material = models.CharField(max_length=100, blank=True)


    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_category(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products();

    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Products, 
                                related_name='variants', 
                                on_delete=models.CASCADE)
    size = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color}"
    
    

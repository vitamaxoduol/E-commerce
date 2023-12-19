from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'stock', 'size', 'color')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description')

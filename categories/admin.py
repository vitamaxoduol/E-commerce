from typing import Any
from django.contrib import admin
from .models import Category
from mptt.admin import  MPTTModelAdmin

# @admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'is_parent', 'is_child')
    list_filter = ('parent',)
    search_fields = ('name',)


    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('children')
    
admin.site.register(Category, CategoryAdmin)
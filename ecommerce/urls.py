from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.index_title = "Categories"
admin.site.index_title = "Users"
admin.site.index_title = "Orders"
admin.site.index_title = "Products"
admin.site.site_header = 'E-commerce Admin'
admin.site.site_title = "Ecommerce"

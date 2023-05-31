from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'balance', 'price']
    list_display_links = ['name']
    list_filter = ['category']
    search_fields = ['name']
    fields = ['id', 'name', 'description', 'category', 'balance', 'price']

admin.site.register(Product, ProductAdmin)
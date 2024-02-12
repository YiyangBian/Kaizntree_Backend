from django.contrib import admin
from .models import Item, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'category', 'in_stock', 'stock_quantity', 'available_stock']
    list_filter = ['category', 'in_stock']
    search_fields = ['name', 'sku']

from django.contrib import admin

# Register your models here.
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('price', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name', 'price')
    ordering = ('price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
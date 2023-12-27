from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' ,'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug','price','instock', 'creatd','updated']
    list_filter = ['instock', 'is_active']
    list_editable = ['price', 'instock']
    prepopulated_fields = {'slug': ('title',)}

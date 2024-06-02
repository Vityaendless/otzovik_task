from django.contrib import admin
from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['title', 'created_at', 'category']
    search_fields = ['title', 'description', 'category']
    fields = ['title', 'category', 'description', 'img', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_at']
    list_display_links = ['id', 'text']
    list_filter = ['created_at', 'product', 'author', 'status', 'grade']
    search_fields = ['text', 'status', 'product', 'author', 'grade']
    fields = ['text', 'grade', 'status', 'product', 'author', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

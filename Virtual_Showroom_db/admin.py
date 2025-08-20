from django.contrib import admin

from .models.Products import ProductDetails, UserCart

@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'style_no', 'product_type', 'designer_head', 'category', 'season', 'fabric', 'sustainable', 'is_active')
    search_fields = ('product_code', 'style_no', 'product_type', 'designer_head', 'category')
    list_filter = ('is_active', 'sustainable')      
    ordering = ('-created_at',)

@admin.register(UserCart)       
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'is_active', 'created_at', 'updated_at')
    search_fields = ('product_id__product_code', 'product_id__style_no')
    list_filter = ('is_active',)
    ordering = ('-created_at',) 

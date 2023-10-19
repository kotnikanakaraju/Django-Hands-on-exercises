from django.contrib import admin
from .models import Product, Cart, CartItem
from shopping_mall_project.shopping import models

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('user_id', 'total_items', 'total_price')

    def total_items(self, obj):
        return obj.cartitem_set.aggregate(models.Sum('quantity'))['quantity__sum']

    def total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.cartitem_set.all())

    total_items.short_description = 'Total Items'
    total_price.short_description = 'Total Price'

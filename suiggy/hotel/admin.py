from django.contrib import admin
from . models import Order, User,Hotel,Menu

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display=('name','address')
    search_fields=('name','address')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('hotel','item_name','price')
    list_filter=('hotel')
    search_fields=('item_name','hotel_name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('user','total_price','items')
    list_filter=('user')
    search_fields=('user__username','total_price')

admin.site.site_header = 'Suiggy Admin'
admin.site.site_title='Suiggy Admin Portal'
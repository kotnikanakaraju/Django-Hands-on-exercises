from django.urls import path
from shopping.views import product_list, add_to_cart, view_cart

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
]
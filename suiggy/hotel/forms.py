from django import forms

from .models import Hotel,Menu,Order

class HotelForm(forms.ModelForm):
    class meta:
        model=Hotel
        fields=['name', 'address']

class MenuForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields=['hotel','item_name','price']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['items']
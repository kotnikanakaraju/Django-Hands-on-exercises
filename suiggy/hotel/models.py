from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()

class Menu(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu)
    total_price=(models.DecimalField(max_digits=10,decimal_places=2))


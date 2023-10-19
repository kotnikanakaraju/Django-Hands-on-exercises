from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    symbol = models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    
class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    balence=models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.user.username

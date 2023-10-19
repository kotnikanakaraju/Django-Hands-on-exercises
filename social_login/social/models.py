from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id=models.CharField(max_length=255, blank=True,null=True)
    google_id=models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return self.user.username

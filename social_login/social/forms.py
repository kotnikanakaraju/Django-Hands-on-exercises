from django import forms

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class metadata:
        model=UserProfile
        fields=('facebook_id', 'google_id')
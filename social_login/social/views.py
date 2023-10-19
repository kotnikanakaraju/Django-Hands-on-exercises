from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from social_login import social_login
from .forms import UserProfileForm

@login_required
def profile(request):
    user=request.user
    try:
        facebook_id=user.social_login.get(provider='facebook').uid
    except social_login.DoesNotExist:
        facebook_id=None

    try:
        google_id=user.social_login.get(provider='google').uid
    except social_login.DoesNotExist:
        google_id=None

    if request.method=='POST':
        form=UserProfileForm(request.POST,instance=user.userprofile)
        if form.is_valid():
            form.save()
        else:
            form=UserProfileForm(request.POST,instance=user.userprofile)
        return render(request,'social/profile.html') 
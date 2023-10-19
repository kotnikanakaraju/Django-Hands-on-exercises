from django.shortcuts import render

from .models import Stock,UserProfile


def stock_list(request):
    stocks=Stock.object.all()
    return render(request, 'stock/stock_list.html',{'stocks':stocks})

def user_Profile(request):
    profile=UserProfile.objects.all()
    return render(request,'stock/user_profile.html',{'profile':profile})

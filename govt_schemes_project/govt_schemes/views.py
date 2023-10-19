from django.shortcuts import render

from .models import Schema

def scheme_list(request):
    scheme=Schema.objects.all()
    return render(request, 'govt_schemes/scheme_list.html', {'scheme':scheme})

def scheme_details(request):
    scheme=Schema.objects.all()
    return render(request, 'govt_schemes/scheme_details.html', {'scheme':scheme})
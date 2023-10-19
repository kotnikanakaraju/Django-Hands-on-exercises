from django.shortcuts import render
from django.views.generic import ListView,DetailView

from crud.simple.models import Company


class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

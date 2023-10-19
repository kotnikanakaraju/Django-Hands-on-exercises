from os import path
from django import views

from django.contrib import admin






urlpatterns = [
    path('',views.scheme_list,name='scheme_list'),
    path('<int:pk>/',views.scheme_details,name='scheme_details'),
]

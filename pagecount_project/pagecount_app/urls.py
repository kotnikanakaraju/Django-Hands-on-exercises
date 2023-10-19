from django.urls import path
from . import views

app_name = 'pagecount_app'
urlpatterns = [
    path('<str:page_name>/', views.increment_page_view, name='increment_page_view'),
    path('view/<str:page_name>/', views.display_page_view, name='display_page_view'),
]
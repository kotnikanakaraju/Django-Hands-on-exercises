

from django.urls import path
from simple import views





urlpatterns = [
    path('Companylist/', views.CompanyListView.as_view(), name='CompanyList'),
    path('CompaniesDetils/<int:pk>/', views.CompanyDetailsView.as_view(), name='CompanyDetails'),

    
]
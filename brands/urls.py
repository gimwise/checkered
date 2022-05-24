from django.urls import path
from . import views

app_name = 'brands'

urlpatterns =[
    path('', views.BrandAdmitCreateView.as_view(), name='request'),
    path('update/<str:pk>/', views.BrandUpdateView.as_view(), name='info'),
    path('list/', views.BrandListView.as_view(), name='brand_list'),
]
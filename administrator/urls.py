from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns =[
    path('', views.brandListView.as_view(), name='request_admit'),
    path('accept/<str:pk>/', views.BrandAdmitAcceptView.as_view(), name='accept'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('delete/<str:pk>/', views.DeleteUserView.as_view(), name='delete'),
]
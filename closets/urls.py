from django.urls import path
from . import views

app_name = 'closets'

urlpatterns =[
    path('', views.closet_list, name='c_list'),
]
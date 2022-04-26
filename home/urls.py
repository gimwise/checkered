from django.urls import path
from . import views

app_name = 'home'

urlpatterns =[
    path('', views.main, name='main'),
    path('intro/', views.intro, name='intro'),

]
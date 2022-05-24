from django.urls import path
from . import views

app_name = 'home'

urlpatterns =[
    path('', views.intro, name='intro'),
    path('main/', views.IndexView.as_view(), name='main'),
    path('<int:closet_id>/', views.detail, name='detail'),
]


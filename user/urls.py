from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns =[
    path('', views.intro.as_view(), name='intro'),
    path('main/', views.IndexView.as_view(), name='main'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('following/<str:pk>', views.FollowView.follow, name='following'),
    path('follower/', views.FollowerListView.as_view(), name='follower'),
]
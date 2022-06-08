from django.urls import path
from . import views

app_name = 'closets'

urlpatterns =[
    path('ours/', views.userListView.as_view(), name='u_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.ClosetCreateView.as_view(), name='new'),
    path('update/<int:pk>/', views.closetUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.deleteClosetView.as_view(), name='delete'),
    path('<uuid:pk>/', views.OtherClosetListView.as_view(), name='other_closet'),
    path('category/', views.categoryListView.as_view(), name='category'),
    path('delCategory/<int:pk>/', views.deleteCategoryView.as_view(), name='del_category'),
    path('newCategory/', views.CategoryCreateView.as_view(), name='new_category'),
]

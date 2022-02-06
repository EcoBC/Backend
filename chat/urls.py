from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('<str:room_name>/', views.room, name='room'),
    path('login/', obtain_auth_token, name="login"),
    path('logout/', views.logout, name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.classify, name='classify'),
    path('points/', views.get_points, name='get_points'),
]
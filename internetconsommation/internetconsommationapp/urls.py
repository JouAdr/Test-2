from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user_details, name='user_details'),
]

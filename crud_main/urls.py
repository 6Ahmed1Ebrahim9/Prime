from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''), # .home is the function name in views.py 
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]


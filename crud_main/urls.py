from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='crud_main-home'), # .home is the function name in views.py
]
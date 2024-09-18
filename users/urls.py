from django.urls import  path
from . import views

urlpatterns = [
    path('', views.register, name='reg'),
    path('/login', views.logging, name='log')
]
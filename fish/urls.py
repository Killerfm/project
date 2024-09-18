from django.urls import path
from . import views

urlpatterns = [
    path('', views.fish_home, name='fish_home'),
    path('create', views.create, name='create'),
]

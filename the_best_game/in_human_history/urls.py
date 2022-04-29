from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game', views.game, name='game'),
     path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('blank', views.blank, name='blank'),
]
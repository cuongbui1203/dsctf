"""dsctf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('games/', views.games, name='games'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('notification', views.notification, name='notification'),
    path('scoreboard', views.scoreboard, name='scoreboard'),
    path('', views.home,name='home'),
]

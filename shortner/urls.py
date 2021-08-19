from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]
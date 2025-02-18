from django.contrib import admin
from django.urls import path
from .views import HomePage, GamePage

urlpatterns = [
    path("", HomePage, name="home"),
    path("game/", GamePage, name="gamepage"),
]

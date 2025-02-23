from django.contrib import admin
from django.urls import path, include
from .views import registerPage

urlpatterns = [
    path("register/", registerPage, name="registerpage"),
]

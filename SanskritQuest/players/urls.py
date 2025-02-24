from django.contrib import admin
from django.urls import path, include
from .views import registerPage, loginPage, logout


urlpatterns = [
    path("register/", registerPage, name="registerpage"),
    path("login/", loginPage, name="loginpage"),
    path("logout/", loginPage, name="logout"),
]

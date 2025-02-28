from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy("loginpage"))
def HomePage(request):
    return render(request, "game/index.html")


@login_required(login_url=reverse_lazy("loginpage"))
def GamePage(request):
    return render(request, "game/game.html")


# Create your views here.

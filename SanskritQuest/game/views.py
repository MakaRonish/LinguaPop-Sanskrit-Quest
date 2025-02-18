from django.shortcuts import render


def HomePage(request):
    return render(request, "game/index.html")


def GamePage(request):
    return render(request, "game/game.html")


# Create your views here.

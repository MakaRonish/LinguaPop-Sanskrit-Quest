from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
    else:
        form = CustomUserForm()
    context = {"form": form}
    return render(request, "players/register.html", context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or pass incorrect")

    return render(request, "players/login.html")


def logoff(request):
    logout(request)
    return redirect("loginpage")


# Create your views here.

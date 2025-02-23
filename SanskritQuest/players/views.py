from django.shortcuts import render
from .forms import CustomUserForm


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


# Create your views here.

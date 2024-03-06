from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books.models import *
from .forms import *

# Create your views here.


@login_required
def user(request):
    current_user = request.user
    data = {"current_user": current_user}
    return render(request, "profile/profile.html", data)


def add_form(request):
    add_form = AddDataForm()
    return render(request, "profile/profile.html", {"add_form": add_form})


def add_data(request):
    if request.method == "POST":
        form = AddDataForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect(reverse("current_user"))
    else:
        form = AddDataForm()
    return render(request, "profile/profile.html", {"add_form": form})

from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from books.models import *
from .forms import *
from django.shortcuts import render
from books.models import Orders
import json

from django.http import JsonResponse


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
            print(form)
            form.save()
            return redirect(reverse("current_user"))
        data = {"form": form}
        return render(request, "profile/profile.html", data)

    else:
        form = AddDataForm()

    return render(request, "profile/profile.html", {"add_form": form})

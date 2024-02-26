from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import *
from .forms import *

# Create your views here.


def reg_view(request):
    reg_form = RegForm()
    return render(request, "auth_reg/auth_reg.html", {"reg_form": reg_form})

from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from search import views


urlpatterns = [
    path("", views.extended_search, name="extended_search")
]

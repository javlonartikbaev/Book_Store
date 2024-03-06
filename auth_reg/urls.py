from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from auth_reg import views


urlpatterns = [
    path("current_user/", views.user, name="current_user"),
    path("current_user/add_data", views.add_form, name="add_data"),
]

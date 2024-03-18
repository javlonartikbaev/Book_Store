from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from auth_reg import views
from books import views as book_view

urlpatterns = [
    path("current_user/", views.user, name="current_user"),
    path("current_user/add_data", views.add_data, name="add_data"),
    path("current_user/ordered_books", book_view.ordered_books, name="ordered_books"),
    path("current_user/my_orders", book_view.my_orders, name="my_orders"),
]

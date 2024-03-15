from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path("", views.book_list, name="home"),
    path("found_books/", views.search_books, name="search_books"),
    path("book_info/<slug:book_slug>", views.book_info, name="book_info"),
    path("catalog/", views.catalog, name="catalog"),
    path(
        "catalog/<slug:catalog_slug>", views.selected_catalog, name="selected_catalog"
    ),
    path("customers/order_books", views.submit_order, name="submit_order"),
    path("customers/save_order", views.save_order, name='save_order'),
]

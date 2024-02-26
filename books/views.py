from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Books, Genre
import datetime
from django.core.paginator import Paginator
from .forms import SearchForm
from django.db.models import Q

def books(request):
    return render(request, "books/books.html")


def book_list(request):
    search_query = request.GET.get("search", "")
    if search_query:
        books = Books.objects.filter(bookname__icontains=search_query)
    else:
        books = Books.published.order_by("id")

    paginator = Paginator(books, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()
    current_year = datetime.date.today().year

    form_search = SearchForm()

    return render(
        request,
        "books/books.html",
        {
            "page_obj": page_obj,
            "genres": genres,
            "current_year": current_year,
            "form_search": form_search,
        },
    )


def book_info(request, book_slug):
    book = get_object_or_404(Books, slug=book_slug)
    genres = Genre.objects.all()
    book_img = book.book_img
    current_year = datetime.date.today().year
    form_search = SearchForm()
    data = {
        "book": book,
        "genres": genres,
        "book_info": book.book_info,
        "book_img": book_img,
        "book_slug": book_slug,
        "current_year": current_year,
        "form_search": form_search,
    }
    return render(request, "books/book_info.html", data)


def catalog(request):
    genres = Genre.objects.all()
    current_year = datetime.date.today().year
    form_search = SearchForm()
    data = {
        "genres": genres,
        "current_year": current_year,
        "form_search": form_search,
    }
    return render(request, "books/catalog.html", data)


def selected_catalog(request, catalog_slug):
    genres = get_object_or_404(Genre, slug=catalog_slug)
    genres_list = Genre.objects.all()
    books = Books.published.filter(genre_id=genres.pk)

    paginator = Paginator(books, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    form_search = SearchForm()
    current_year = datetime.date.today().year
    data = {
        "page_obj": page_obj,
        "current_year": current_year,
        "catalog_slug": catalog_slug,
        "genres_list": genres_list,
        "form_search": form_search,
    }
    return render(request, "books/selected_catalog.html", data)


def search_books(request):
    current_year = datetime.date.today().year
    search_form = SearchForm(request.GET)
    
    if search_form.is_valid():
        search_query = search_form.cleaned_data["book_name"]
        if search_query:
            found_books = Books.published.filter(book_name__icontains=search_query)
        else:
            found_books = Books.published.all()
    else:
        found_books = Books.published.all()

    data = {
        "found_books": found_books,
        "current_year": current_year,
        "search_form": search_form,
        "form_search": search_form,
    }

    return render(request, "books/found_books.html", data)
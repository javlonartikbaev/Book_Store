from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from books.models import *
import datetime
from django.core.paginator import Paginator
from search.forms import *
from django.db.models import Q
from books.models import *
from django.utils.dateparse import parse_date




def extended_search(request):
    extended_search_form = ExtendedSearchForm(request.GET)
    found_books = Books.published.all()

    if extended_search_form.is_valid():
        search_book_name = extended_search_form.cleaned_data.get("book_name")
        search_author_name = extended_search_form.cleaned_data.get("author_name")
        search_genres = extended_search_form.cleaned_data.get("genres")
        search_start_date = extended_search_form.cleaned_data.get("start_date")

        if search_book_name:
            found_books = found_books.filter(book_name__icontains=search_book_name)
        
        if search_author_name:
            found_books = found_books.filter(author_name__icontains=search_author_name)

        if search_genres:
            found_books = found_books.filter(genre__id=search_genres)
        
        if search_start_date:
            found_books = found_books.filter(published_data__gte=search_start_date)
        
    data = {
        "extended_search_form": extended_search_form,
        "found_books": found_books,
    }
    return render(request, "search/extended_search.html", data)
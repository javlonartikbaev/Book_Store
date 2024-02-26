from django import forms
from books.models import *


class ExtendedSearchForm(forms.Form):
    book_name = forms.CharField(
        max_length=100,
        label="Название книги",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Введите название книги", "class": "book_name", 'name': "search_book_name"}
        ),
    )

    author_name = forms.CharField(
        max_length=100,
        label="Автор книги",
        required=False,
        widget=forms.TextInput(
            {"placeholder": "Введите автор книги", "class": "author_name", 'name': "search_author_name"}
        ),
    )

    def get_genre_list(self):
        genre = list(Genre.objects.values_list('id', 'genre'))
        return genre

    genres = get_genre_list(Genre)

    genres = forms.ChoiceField(
        label="Жанры",
        required=False,
        choices=genres
    )


    start_date = forms.DateField(
        label="Дата Публикаций",
        widget=forms.DateInput(attrs={"type": "date", "class": "start_date", "name": "search_start_date"}),
        required=False,
    )


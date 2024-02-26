from django import forms


class SearchForm(forms.Form):
    book_name = forms.CharField(
        max_length=100,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Введите название книги", "name": "search"}
        ),
    )
    



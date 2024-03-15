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
    

class AddToCartForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    book_name = forms.CharField(widget=forms.HiddenInput())
    book_price = forms.CharField(widget=forms.HiddenInput())

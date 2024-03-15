from django import forms

from books.models import *


class RegForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Введите ваше имя", "class": "first_name"}
        ),
    )
    second_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Введите фамилию", "class": "second_name"}
        ),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Введите email", "class": "email"})
    )
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"placeholder": "Введите username", "class": "username"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введите пароль", "class": "password"}
        )
    )


class AddDataForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ["first_name", "second_name", "email", "phone_number"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

from django import forms


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


class AddDataForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Введите email", "class": "email"})
    )
    phone_number = forms.CharField(max_length=13)

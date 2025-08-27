from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Dogovornitsa.apps.iam.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    username = forms.CharField(label="Логин")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = f'Введите {field.label.lower()}'



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите логин или email"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Введите пароль"
        })
    )


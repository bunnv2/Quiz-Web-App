from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-4", "placeholder": "Enter Username"}
        ),
    )
    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-5",
                "placeholder": "Enter Email (optional)",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=30,
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-6", "placeholder": "Enter Password"}
        ),
    )
    password2 = forms.CharField(
        max_length=30,
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-7", "placeholder": "Enter Password"}
        ),
    )

    class Meta:
        model = Account
        fields = ("username", "email", "password1", "password2")


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-4", "placeholder": "Enter Username"}
        ),
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-5", "placeholder": "Enter Password"}
        ),
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid Login")

    class Meta:
        model = Account
        fields = ("username", "password")

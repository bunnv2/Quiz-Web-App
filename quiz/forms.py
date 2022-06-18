from django import forms
from .models import *


class QuizForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Enter Quiz Name",
            }
        ),
    )

    category = forms.CharField(
        max_length=50,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-5", "placeholder": "Enter Quiz Category"}
        ),
    )

    class Meta:
        model = Quiz
        fields = ["name", "category"]

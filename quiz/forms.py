from email.policy import default
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


class QuestionForm(forms.ModelForm):
    question = forms.CharField(
        max_length=200,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-4", "placeholder": "Enter Question"}
        ),
    )

    class Meta:
        model = Question
        fields = ["question"]


class AnswerForm(forms.Form):
    correct1 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mt-0"}),
    )
    answer1 = forms.CharField(
        max_length=50,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First answer"}
        ),
    )
    correct2 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mt-0"}),
    )
    answer2 = forms.CharField(
        max_length=50,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Second answer"}
        ),
    )
    correct3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mt-0"}),
    )
    answer3 = forms.CharField(
        max_length=50,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Third answer"}
        ),
    )
    correct4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mt-0"}),
    )
    answer4 = forms.CharField(
        max_length=50,
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Fourth answer"}
        ),
    )

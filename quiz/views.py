from django.shortcuts import redirect, render
from .forms import *
from account.models import Account


def create(request):
    context = {}
    form = QuizForm()
    context["form"] = form
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                print(form.cleaned_data)
                quiz = Quiz(
                    name=form.cleaned_data["name"],
                    category=form.cleaned_data["category"],
                    id_user=user,
                )
                quiz.save()
                return redirect("add")
    return render(request, "quiz/create.html", context)


def add(request):
    return render(request, "quiz/add.html")


def quizes(request):
    return render(request, "quiz/quizes.html")

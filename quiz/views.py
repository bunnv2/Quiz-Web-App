from django.shortcuts import redirect, render
from .forms import *
from account.models import Account


def create(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = QuizForm(request.POST)
            if form.is_valid():
                quiz = Quiz(
                    name=form.cleaned_data["name"],
                    category=form.cleaned_data["category"],
                    id_user=user,
                )
                quiz.save()
                return redirect("add")
    form = QuizForm()
    context["form"] = form
    return render(request, "quiz/create.html", context)


def add(request):
    return render(request, "quiz/add.html")


def quizes(request):
    return render(request, "quiz/quizes.html")

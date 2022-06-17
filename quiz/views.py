from django.shortcuts import redirect, render
from .forms import *
from account.models import Account


def create(request):
    context = {}
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            quiz = Quiz(
                name=form.cleaned_data["name"],
                category=form.cleaned_data["category"],
                # id_user=User.objects.get(login=request.POST["active"]),
            )
            quiz.save()
            return redirect("add")
    else:
        form = QuizForm()
        context["form"] = form
    return render(request, "quiz/create.html", context)


def add(request):
    return render(request, "quiz/add.html")


def quizes(request):
    return render(request, "quiz/quizes.html")

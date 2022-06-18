from multiprocessing import context
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
                return redirect("add", quiz_id=quiz.id)
    form = QuizForm()
    context["form"] = form
    return render(request, "quiz/create.html", context)


def add(request, quiz_id):
    context = {}
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            question_form = QuestionForm(request.POST)
            answers_form = AnswerForm(request.POST)
            if question_form.is_valid() and answers_form.is_valid():
                quiz = Quiz.objects.get(id=quiz_id)
                question = Question(
                    question=question_form.cleaned_data["question"],
                    id_quiz=quiz,
                )
                question.save()
                answer1 = Answer(
                    id_question=question,
                    answer=answers_form.cleaned_data["answer1"],
                    correct=answers_form.cleaned_data["correct1"],
                )
                answer2 = Answer(
                    id_question=question,
                    answer=answers_form.cleaned_data["answer2"],
                    correct=answers_form.cleaned_data["correct2"],
                )
                answer3 = Answer(
                    id_question=question,
                    answer=answers_form.cleaned_data["answer3"],
                    correct=answers_form.cleaned_data["correct3"],
                )
                answer4 = Answer(
                    id_question=question,
                    answer=answers_form.cleaned_data["answer4"],
                    correct=answers_form.cleaned_data["correct4"],
                )
                answer1.save()
                answer2.save()
                answer3.save()
                answer4.save()
                return redirect("add", quiz_id=quiz_id)
    question_form = QuestionForm()
    answers_form = AnswerForm()
    context["question_form"] = question_form
    context["answers_form"] = answers_form
    return render(request, "quiz/add.html", context)

    return render(request, "quiz/add.html")


def quizes(request):
    return render(request, "quiz/quizes.html")

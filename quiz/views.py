from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import *
from account.models import Account
from django.contrib import messages


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


def quizes(request):
    context = {}
    quizes = Quiz.objects.all()
    if len(quizes) != 0:
        questions_number = []
        for quiz in quizes:
            questions_number.append(len(Question.objects.filter(id_quiz=quiz)))
        context["quizes"] = zip(quizes, questions_number)
        return render(request, "quiz/quizes.html", context)
    context["quizes"] = None
    return render(request, "quiz/quizes.html", context)


def solving(request, quiz_id):
    context = {}
    user = request.user
    if user.is_authenticated:
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(id_quiz=quiz)
        if request.method == "POST":
            result_number = check_answers(request, quiz_id)
            result = Result(
                id_quiz=quiz,
                id_user=user,
                score=result_number,
            )
            # wyswitlenie modala
            messages.success(request, f"Your result: {result_number}%")
            result.save()
            context["result"] = result_number
        answers, zipped = [], []
        for id, question in enumerate(questions):
            answers.append(Answer.objects.filter(id_question=question))
            zipped.append([question, answers[id]])
        context["questions"] = zipped
        context["quiz"] = quiz
    return render(request, "quiz/solving.html", context)


def check_answers(request, quiz_id):
    # numerpytania:numerodpowiedzi
    form_data = request.POST.getlist("answer", None)
    if form_data:
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(id_quiz=quiz)
        answers = Answer.objects.filter(id_question__in=questions)
        selected_answers = []
        result = 0
        # odczytywanie wybranych odpowiedzi oraz przypisanie ich do list
        for item in form_data:
            sliced = item.split(":")
            question = questions[int(sliced[0])]
            answer = answers[4 * int(sliced[0]) + int(sliced[1])]
            selected_answers.append(answer)
        # sprawdzanie poprawnosci wybranych odpowiedzi
        for question in questions:
            correct_answers = Answer.objects.filter(id_question=question, correct=True)
            correct_answers = [answer for answer in correct_answers]
            selected_answers_in_question = [
                answer for answer in selected_answers if answer.id_question == question
            ]
            if selected_answers_in_question == correct_answers:
                result += 1
        return round((result / len(questions)) * 100, 2)
    return 0.0


def quiz_delete(request):
    data = request.POST.getlist("id_quiz", None)
    quiz = Quiz.objects.get(id=data[0])
    quiz.delete()
    return redirect("quizes")

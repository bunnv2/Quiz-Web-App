from django.shortcuts import render

def create(request):
    return render(request, "quiz/create.html")

def name(request):
    return render(request, "quiz/name.html")

def quizes(request):
    return render(request, "quiz/quizes.html")

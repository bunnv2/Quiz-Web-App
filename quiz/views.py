from django.shortcuts import render

def create(request):
    return render(request, "quiz/create.html")

def add(request):
    return render(request, "quiz/add.html")

def quizes(request):
    return render(request, "quiz/quizes.html")

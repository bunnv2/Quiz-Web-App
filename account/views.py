from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def sign(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return render(request, "account/sign.html", context)

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("sign")
    form = LoginForm()
    context["form"] = form
    return render(request, "account/sign.html", context)


def register(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            context["form"] = form
            return redirect("home")
    else:
        form = RegisterForm()
        context["form"] = form
    return render(request, "account/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")

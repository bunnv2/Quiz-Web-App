from django.shortcuts import render

def sign(request):
    return render(request, "account/sign.html")

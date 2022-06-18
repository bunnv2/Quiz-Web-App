from django.urls import path
from . import views

urlpatterns = [
    path("sign", views.sign, name="sign"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    # path("create", views.quizes, name="quizes"),
    path("quizes", views.quizes, name="quizes"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("create/<int:quiz_id>", views.add, name="add"),
    path("quizes", views.quizes, name="quizes"),
    path("quiz_delete", views.quiz_delete, name="quiz_delete"),
    path("quizes/<int:quiz_id>", views.solving, name="solving"),
]

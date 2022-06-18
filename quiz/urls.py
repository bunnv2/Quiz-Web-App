from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("create/add", views.add, name="add"),
    path("quizes", views.quizes, name="quizes"),
    path("quizes/solving", views.solving, name="solving"),    
]

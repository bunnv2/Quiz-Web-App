from django.contrib import admin
from .models import Quiz, Question, Answer, Result


class QuizAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "id_user")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "id_quiz")


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer", "id_question", "correct")


class ResultAdmin(admin.ModelAdmin):
    list_display = ("id_quiz", "id_user", "score", "date")


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)

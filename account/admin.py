from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("login", "password", "user_type", "blocked")


admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "is_admin")


admin.site.register(Account, AccountAdmin)

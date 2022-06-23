from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "is_admin")


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)

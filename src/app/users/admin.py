from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from app.users.models import User


@admin.register(User)
class User(UserAdmin):
    list_display = UserAdmin.list_display + ("chat_id",)
    fieldsets = UserAdmin.fieldsets + ((_("Telegram Bot"), {"fields": ("chat_id",)}),)

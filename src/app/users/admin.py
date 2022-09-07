from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.users.models import User


@admin.register(User)
class User(UserAdmin):
    pass

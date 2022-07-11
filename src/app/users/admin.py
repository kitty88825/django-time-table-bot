from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.jobs.models import Job

from .models import User


class JobInlineAdmin(admin.TabularInline):
    model = Job
    extra = 0


@admin.register(User)
class User(UserAdmin):
    inlines = (JobInlineAdmin,)
    list_display = UserAdmin.list_display + ('jobs',)

    def jobs(self, user):
        return user.company.count()

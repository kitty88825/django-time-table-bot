from django.contrib import admin

from app.jobs.models import Job, Wage, WorkDay


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
    list_filter = ("user",)


@admin.register(Wage)
class WageAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    pass

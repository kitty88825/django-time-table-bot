from django.contrib import admin

from app.jobs.models import Job, Wage, WorkDay


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Wage)
class WageAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    pass

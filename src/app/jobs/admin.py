from django.contrib import admin

from app.jobs.models import Company, Job, WorkDay


class WorkDayInlineAdmin(admin.TabularInline):
    model = WorkDay
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = (WorkDayInlineAdmin,)
    list_display = ("id", "user", "company", "hourly_rate")
    list_filter = ("company", "user")
    list_display_links = ("id", "user", "company", "hourly_rate")


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    list_display = ("id", "job", "start_datetime", "end_datetime", "hours")
    list_display_links = ("id", "job", "start_datetime", "end_datetime", "hours")
    list_filter = ("job",)

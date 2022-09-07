from django.db import models

from app.users.models import User


class Job(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Wage(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    hourly_rate = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.hourly_rate}"


class WorkDay(models.Model):
    wage = models.ForeignKey(Wage, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    hours = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.wage}: {self.hours}"

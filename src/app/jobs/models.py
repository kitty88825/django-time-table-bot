from django.db import models


class Company(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return self.name


class Job(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    hourly_rate = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.company.name}: {self.user.username}"


class WorkDay(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    hours = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.job}"

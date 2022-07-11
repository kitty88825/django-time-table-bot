from django.contrib.auth.models import AbstractUser
from django.db import models

from app.jobs.models import Company


class User(AbstractUser):
    company = models.ManyToManyField(Company, through="jobs.Job")

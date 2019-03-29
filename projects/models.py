from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete="CASCADE")
    data = JSONField()
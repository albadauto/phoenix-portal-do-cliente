from django.db import models
from django.contrib.auth.models import User
from datetime import date
class TCALL(models.Model):
    description = models.TextField(max_length=255)
    is_solved = models.BooleanField(default=False)
    title = models.TextField(max_length=64)
    is_answered = models.BooleanField(default=False)
    date_inserted = models.DateField(default=date.today())
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    hours_to_resolve = models.IntegerField()
    hours_resolved = models.IntegerField(default=0)

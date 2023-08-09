from django.db import models

class TCALL(models.Model):
    description = models.TextField(max_length=255)
    isSolved = models.BooleanField(default=False)


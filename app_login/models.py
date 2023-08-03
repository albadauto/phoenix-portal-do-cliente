from django.db import models


class TUSER(models.Model):
    name = models.TextField(max_length=255)
    password = models.TextField(max_length=255)

from django.db import models
from app_login import models as app_login_model
from datetime import date
class TCALL(models.Model):
    description = models.TextField(max_length=255)
    isSolved = models.BooleanField(default=False)
    title = models.TextField(max_length=64)
    date_inserted = models.DateField(default=date.today())
    login = models.ForeignKey(app_login_model.TUSER, on_delete=models.CASCADE)


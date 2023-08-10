# Generated by Django 4.2.3 on 2023-08-10 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_call', '0002_tcall_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcall',
            name='date_inserted',
            field=models.DateField(default=datetime.date(2023, 8, 9)),
        ),
        migrations.AddField(
            model_name='tcall',
            name='title',
            field=models.TextField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-10 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0002_rename_usuname_tuser_name_and_more'),
        ('app_call', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcall',
            name='login',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_login.tuser'),
            preserve_default=False,
        ),
    ]

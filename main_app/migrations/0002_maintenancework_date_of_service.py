# Generated by Django 5.1.3 on 2024-11-10 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancework',
            name='date_of_service',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
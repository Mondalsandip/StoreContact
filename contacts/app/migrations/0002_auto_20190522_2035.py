# Generated by Django 2.1.7 on 2019-05-22 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

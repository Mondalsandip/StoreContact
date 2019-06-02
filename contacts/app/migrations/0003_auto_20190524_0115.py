# Generated by Django 2.1.7 on 2019-05-23 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20190522_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='contact',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

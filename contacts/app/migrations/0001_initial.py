# Generated by Django 2.1.7 on 2019-05-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('info', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

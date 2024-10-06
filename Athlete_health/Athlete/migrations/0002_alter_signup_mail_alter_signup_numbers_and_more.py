# Generated by Django 5.0.7 on 2024-08-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Athlete', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='mail',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='numbers',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

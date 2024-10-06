# Generated by Django 5.0.7 on 2024-09-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Athlete', '0011_rename_athleteinput_healthinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthInputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heartrate', models.CharField(max_length=20)),
                ('blood_pressure', models.CharField(max_length=20)),
                ('Temperature', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='HealthInput',
        ),
    ]

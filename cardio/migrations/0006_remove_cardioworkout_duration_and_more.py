# Generated by Django 4.0 on 2022-01-12 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardio', '0005_sprint_rest_measure_sprint_rest_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardioworkout',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='cardioworkout',
            name='intensity_category',
        ),
        migrations.RemoveField(
            model_name='cardioworkout',
            name='unit_of_measure',
        ),
    ]

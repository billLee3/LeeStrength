# Generated by Django 4.0 on 2022-01-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_rename_exercise_name_exerciseset_associated_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='category',
            field=models.CharField(default='Assorted Exercise', max_length=200),
        ),
    ]
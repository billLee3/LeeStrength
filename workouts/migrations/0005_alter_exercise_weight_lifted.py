# Generated by Django 4.0 on 2022-01-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_exercise_repetitions_exercise_sets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='weight_lifted',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

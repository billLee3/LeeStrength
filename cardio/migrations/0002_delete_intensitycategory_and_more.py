# Generated by Django 4.0 on 2022-01-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IntensityCategory',
        ),
        migrations.AddField(
            model_name='cardioworkout',
            name='intensity_category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

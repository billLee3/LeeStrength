# Generated by Django 4.0 on 2022-01-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio', '0007_cardioworkout_owner_cardioworkout_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervaltraining',
            name='load_measure',
            field=models.CharField(default='seconds', max_length=100),
        ),
        migrations.AddField(
            model_name='intervaltraining',
            name='rest_measure',
            field=models.CharField(default='seconds', max_length=100),
        ),
    ]

# Generated by Django 4.0 on 2022-01-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio', '0009_alter_cardioworkout_cardio_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='sprint_type',
            field=models.CharField(choices=[('distance', 'distance run'), ('time', 'for time')], default='time', max_length=200),
        ),
    ]
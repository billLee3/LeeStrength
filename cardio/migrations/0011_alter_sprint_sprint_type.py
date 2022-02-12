# Generated by Django 4.0 on 2022-01-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio', '0010_sprint_sprint_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='sprint_type',
            field=models.CharField(choices=[('distance', 'Distance run'), ('time', 'For time')], default='time', max_length=200),
        ),
    ]

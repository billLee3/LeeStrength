# Generated by Django 4.0 on 2022-01-07 21:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardioWorkout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cardio_type', models.CharField(default='Run', max_length=200)),
                ('duration', models.FloatField()),
                ('unit_of_measure', models.CharField(default='seconds', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IntensityCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('intensity_category', models.CharField(default='distance', max_length=100)),
            ],
        ),
    ]

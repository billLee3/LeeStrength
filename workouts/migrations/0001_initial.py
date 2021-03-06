# Generated by Django 3.2.9 on 2022-01-01 03:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('exercise_name', models.CharField(default='Not Listed', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('repetitions', models.IntegerField(default=1)),
                ('weight_lifted', models.FloatField(blank=True, null=True)),
                ('exercise_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='associated_workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workout'),
        ),
    ]

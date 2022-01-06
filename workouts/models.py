from django.db import models
import uuid
from base.models import Profile
# Create your models here.

class Workout(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    #Relationships
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

class Exercise(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    exercise_name = models.CharField(max_length=200, unique=False, blank=False, null=False, default="Not Listed")
    #Relationships
    associated_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    
class ExerciseSet(models.Model):  
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    repetitions = models.IntegerField(unique=False, blank=False, null=False, default=1)
    weight_lifted = models.FloatField(blank=True, null=True)
    #Relationships
    associated_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
from django.db import models
import uuid
from base.models import Profile
# Create your models here.

class Workout(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, null=False, blank=False, default="Assorted Exercise")
    #Relationships
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.owner.username + "-" + str(self.timestamp))

class Exercise(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    exercise_name = models.CharField(max_length=200, unique=False, blank=False, null=False, default="Not Listed")
    repetitions = models.IntegerField(unique=False, blank=False, null=False, default=1)
    weight_lifted = models.FloatField(blank=True, null=True, default=0)
    sets = models.IntegerField(unique=False, blank=False, null=False, default=1)
    #Relationships
    associated_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.associated_workout.owner.username + "-" + self.exercise_name + "-" + str(self.associated_workout.timestamp)[0:10])


from django.db import models
import uuid

from django.db.models.fields import CharField
from base.models import Profile
# Create your models here.

class CardioWorkout(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cardio_type = models.CharField(max_length=200, null=False, blank=False, default="Run")
    timestamp = models.DateField(auto_now_add=True)
    #Relsationships
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.owner.username + "-" + self.cardio_type + "-" + str(self.timestamp))

class IntervalTraining(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    load_interval = models.FloatField(default=0) #assume seconds for measurement
    load_measure = CharField(max_length=100, null=False, blank=False, default="seconds")
    rest_interval = models.FloatField(default=0)
    rest_measure = CharField(max_length=100, null=False, blank=False, default="seconds")
    num_iterations = models.IntegerField(default=1)
    overall_distance = models.FloatField(default=0) #assume miles for measurement
    #Relationships
    associated_cardio_workout = models.ForeignKey(CardioWorkout, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.associated_cardio_workout.owner.username + '-' + str(self.associated_cardio_workout.timestamp))

class Distance(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    distance = models.FloatField() # assume miles for measurement
    time = models.FloatField() # assume seconds for measurement
    elevation_gained = models.FloatField() # assume feet for measurements.
    #Relationships
    associated_cardio_workout = models.ForeignKey(CardioWorkout, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.associated_cardio_workout.owner.username + '-' + str(self.associated_cardio_workout.timestamp) + '-' + str(self.distance) + "miles")

class Sprint(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    sprint_type = models.TextChoices('SprintType', 'DISTANCE TIME')
    sprint_distance = models.FloatField(null=True, blank=True)
    sprint_time = models.FloatField(null=True, blank=True)
    rest_period = models.FloatField(default=0)
    rest_measure = models.CharField(max_length=200, null=True, blank=True, default='seconds')
    num_sprints = models.IntegerField(null=False, blank=False, default=1)
    on_hill = models.BooleanField(null=True, blank=True)
    #Relationships
    associated_cardio_workout = models.ForeignKey(CardioWorkout, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.associated_cardio_workout.owner.username + '-' + str(self.associated_cardio_workout.timestamp))

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import CardioWorkout, IntervalTraining, Sprint, Distance, Profile
from django.dispatch import receiver

options = {
    "distance run": Distance, 
    "interval training": IntervalTraining,
    "sprint": Sprint
    }


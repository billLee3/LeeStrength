from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    height = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    #Relationships
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.username)

class Weight(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    weight = models.FloatField(null=True, blank=False)
    date = models.DateField(auto_now_add=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #Relationships
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Goal(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    priority = models.CharField(max_length=100, null=False, blank=False, default="primary")
    short_description = models.CharField(max_length=500, blank=False, null=True)
    long_description = models.CharField(max_length=500, blank=False, null=False, default="Get Better")
    #Relationships
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    
    
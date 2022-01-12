from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Nutrition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    #Relationships
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.owner.username)

class FoodItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=500, blank=False, null=False, default="Not listed")
    meal = models.CharField(max_length=100, blank=False, null=False, default="Snack")
    protein = models.FloatField()
    carbs = models.FloatField()
    calories = models.FloatField()
    fat = models.FloatField()
   
    #Relationships
    owner = models.ForeignKey(Nutrition, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner.owner.username + "-" + self.name)
    

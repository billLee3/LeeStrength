from django.contrib import admin
from . import models
from .models import Nutrition, FoodItem

# Register your models here.
admin.site.register(Nutrition)
admin.site.register(FoodItem)
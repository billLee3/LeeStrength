from django.contrib import admin
from .models import CardioWorkout, IntervalTraining, Distance, Sprint
# Register your models here.
admin.site.register(CardioWorkout)
admin.site.register(IntervalTraining)
admin.site.register(Distance)
admin.site.register(Sprint)
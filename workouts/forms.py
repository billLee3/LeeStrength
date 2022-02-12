from ast import Mod
from django.forms import ModelForm
from .models import Workout, Exercise

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
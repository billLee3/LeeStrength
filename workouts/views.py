from django.shortcuts import render
from django.http import HttpResponse
from .models import Workout, Exercise

# Create your views here.
def workouts(request):
    workouts = Workout.objects.all()
    context = {'workouts': workouts}
    return render(request, 'workouts/workouts.html', context)

def workout(request, pk):
    workout = Workout.objects.get(id=pk)
    exercises = Exercise.objects.filter(associated_workout=pk)
    context = {'workout': workout, 'exercises': exercises}
    return render(request, 'workouts/single-workout.html', context)


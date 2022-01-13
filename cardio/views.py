from django.http import HttpResponse
from django.shortcuts import render
from .models import CardioWorkout, IntervalTraining, Sprint, Distance

# Create your views here.

def cardioWorkouts(request):
    workouts = CardioWorkout.objects.all()
    context = {'workouts': workouts}
    return render(request, 'cardio/cardio_workouts.html', context)

def cardioWorkout(request, pk):
    workout = CardioWorkout.objects.get(id=pk)
    if workout.cardio_type == 'interval training':
        workout_data = IntervalTraining.objects.filter(associated_cardio_workout=pk)
    elif workout.cardio_type == 'distance run':
        workout_data = Distance.objects.filter(associated_cardio_workout=pk)
    elif workout.cardio_type == 'sprint':
        workout_data = Sprint.objects.filter(associated_cardio_workout=pk)
    else:
        print("404. ")
    context = {'workout': workout, 'workout_data': workout_data}
    return render(request, 'cardio/single_cardio_workout.html', context=context)

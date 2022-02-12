from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm

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

def createWorkout(request):
    form = WorkoutForm()
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('workouts')
    context = {'form': form}
    return render(request, 'workouts/workout-form.html', context=context)

def updateWorkout(request, pk):
    workout = Workout.objects.get(id=pk)
    form = WorkoutForm(instance=workout)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
        return redirect('workouts')
    context = {'form': form}
    return render(request, 'workouts/workout-form.html', context=context)

def deleteWorkout(request, pk):
    workout = Workout.objects.get(id=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts')
    context = {'object': workout}
    return render(request, 'workouts/delete-object.html', context=context)

def createExercise(request):
    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts')
    context = {'form': form}
    return render(request, 'workouts/exercise-form.html', context=context)

def updateExercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    form = ExerciseForm(instance=exercise)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        form.save()
        return redirect('workouts')
    context = {'form': form}
    return render(request, 'workouts/exercise-form.html', context=context)

def deleteExercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('workouts')
    context = {'object': exercise}
    return render(request, 'workouts/delete-object.html', context=context)


    

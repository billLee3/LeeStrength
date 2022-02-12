from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CardioWorkout, IntervalTraining, Sprint, Distance
from .forms import CardioForm, IntervalForm, DistanceForm, SprintForm

# Create your views here.

def cardioWorkouts(request):
    workouts = CardioWorkout.objects.all()
    context = {'workouts': workouts}
    return render(request, 'cardio/cardio_workouts.html', context)

def cardioWorkout(request, pk):
    workout = CardioWorkout.objects.get(id=pk)
    if IntervalTraining.objects.filter(associated_cardio_workout=pk):
        exercises = IntervalTraining.objects.filter(associated_cardio_workout=pk)
    if  Distance.objects.filter(associated_cardio_workout=pk):
        exercises = Distance.objects.filter(associated_cardio_workout=pk)
    if Sprint.objects.filter(associated_cardio_workout=pk):
        exercises = Sprint.objects.filter(associated_cardio_workout=pk)
    context = {'workout': workout, 'exercises': exercises}
    return render(request, 'cardio/single_cardio_workout.html', context=context)

def createCardioWorkout(request):
    form = CardioForm()
    if request.method == 'POST':
        form = CardioForm(request.POST)
        if form.is_valid():
            cardioworkout = form.save()
        return redirect(reverse('createcardioexercise', kwargs={'pk': cardioworkout.id}))
    context = {'form': form}
    return render(request, 'cardio/cardio_form.html', context=context)

def updateCardioWorkout(request, pk):
    cardio_workout = CardioWorkout.objects.get(id=pk)
    form = CardioForm(instance=cardio_workout)
    if request.method == 'POST':
        form = CardioForm(request.POST, instance=cardio_workout)
        if form.is_valid():
            form.save()
        return redirect('cardioworkouts')
    context = {'form': form}
    return render(request, "cardio/cardio_form.html", context=context)

def deleteCardioWorkout(request, pk):
    cardio_workout = CardioWorkout.objects.get(id=pk)
    if request.method == 'POST':
        cardio_workout.delete()
        return redirect('cardioworkouts')
    context = {'object': cardio_workout}
    return render(request, 'cardio/delete-object.html', context=context)

def createCardioExercise(request, pk):
    cardio_workout = CardioWorkout.objects.get(id=pk)
    if cardio_workout.cardio_type == "distance run":
        form = DistanceForm()
        if request.method == 'POST':
            form = DistanceForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("cardioworkouts")
    elif cardio_workout.cardio_type == "sprint":
        form = SprintForm()
        if request.method == 'POST':
            form = SprintForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("cardioworkouts")
    elif cardio_workout.cardio_type == "interval training":
        form = IntervalForm()
        if request.method == 'POST':
            form = IntervalForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("cardioworkouts")
    context = {'form':form}
    return render(request, 'cardio/cardio_form.html', context=context)



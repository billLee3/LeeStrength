from django.shortcuts import render

# Create your views here.

def cardioWorkouts(request):
    context = {}
    return render(request, 'cardio/cardio_workouts.html', context)
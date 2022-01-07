from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def workouts(request):
    context = {}
    return render(request, 'workouts/workouts.html', context)
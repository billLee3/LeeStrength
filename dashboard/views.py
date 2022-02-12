from django.shortcuts import render
from base.models import Profile
from workouts.models import Workout, Exercise
from cardio.models import CardioWorkout, IntervalTraining, Sprint, Distance
# Create your views here.

def userDashboard(request):
    context = {}
    return render(request, 'dashboard/user-dashboard.html', context)
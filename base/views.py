from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.

def landing(request):
    context = {}
    return render(request, 'base/landing.html', context)

def login(request):
    context = {}
    return render(request, 'base/login.html', context)

def signup(request):
    context = {}
    return render(request, 'base/signup.html', context)
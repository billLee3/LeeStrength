from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardioWorkouts, name='cardioworkouts'),
    path('<str:pk>/', views.cardioWorkout, name='cardioworkout')
]
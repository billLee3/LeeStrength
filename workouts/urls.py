from django.urls import path
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('workout/<str:pk>/', views.workout, name='workout'),
    path('create-workout/', views.createWorkout, name='create-workout'),
    path('update-workout/<str:pk>', views.updateWorkout, name='update-workout'),
    path('delete-workout/<str:pk>/', views.deleteWorkout, name='delete-workout'),
    path('create-exercise/', views.createExercise, name='create-exercise'),
    path('update-exercise/<str:pk>/', views.updateExercise, name='update-exercise'),
    path('delete-exercise/<str:pk>/', views.deleteExercise, name='delete-exercise'),
]
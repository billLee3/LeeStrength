from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardioWorkouts, name='cardioworkouts'),
    path('cardio/<str:pk>/', views.cardioWorkout, name='cardioworkout'),
    path('createcardioworkout/', views.createCardioWorkout, name='createcardioworkout'),
    path('updatecardioworkout/<str:pk>/', views.updateCardioWorkout, name='updatecardioworkout'),
    path('deletecardioworkout/<str:pk>/', views.deleteCardioWorkout, name='deletecardioworkout'),
    path('createcardioexercise/<str:pk>/', views.createCardioExercise, name="createcardioexercise")
]
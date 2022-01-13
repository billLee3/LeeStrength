from django.urls import path
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('<str:pk>/', views.workout, name='workout')
]
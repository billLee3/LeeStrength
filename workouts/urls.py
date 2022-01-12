from django.urls import path
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('workouts/<str:pk>/', views.workout, name='workout')
]
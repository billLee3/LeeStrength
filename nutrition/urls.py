from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutritionDashboard, name="nutrition-dashboard"), 
]
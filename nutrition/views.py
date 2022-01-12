from django.shortcuts import render

# Create your views here.
def nutritionDashboard(request):
    context = {}
    return render(request, 'nutrition/nutrition_dashboard.html', context)
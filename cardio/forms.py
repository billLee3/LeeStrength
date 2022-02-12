from django.forms import ModelForm
from .models import CardioWorkout, IntervalTraining, Distance, Sprint

class CardioForm(ModelForm):
    class Meta:
        model = CardioWorkout
        fields = '__all__'

class IntervalForm(ModelForm):
    class Meta:
        model = IntervalTraining
        fields = ['load_interval', 
        'load_measure', 
        'rest_interval', 
        'rest_measure', 
        'num_iterations', 
        'overall_distance']

class DistanceForm(ModelForm):
    class Meta: 
        model = Distance
        fields = '__all__'

class SprintForm(ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'

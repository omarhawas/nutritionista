from django.forms import ModelForm
from .models import Meals

class MealsForm(ModelForm):
    class Meta:
        model = Meals
        fields = ['meal', 'food', 'portion', 'calories', 'day']




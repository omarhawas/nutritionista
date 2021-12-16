from django.shortcuts import render, redirect
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Day, Food
from .forms import MealsForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def days_index(request):
    days = Day.objects.all()
    return render(request, 'days/index.html', {'days': days }) 

def days_detail(request, day_id):
    day = Day.objects.get(id=day_id)
    meals_form = MealsForm()
    return render(request, 'days/detail.html', {
        'day': day, 'meals_form': meals_form
        })

class DayCreate(CreateView):
    model = Day
    fields = ['date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DayUpdate(UpdateView):
    model = Day
    fields = '__all__'

class DayDelete(DeleteView):
    model = Day
    success_url = '/days/'

def signup(request):
    error_message = ''
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')
            else:
                error_message = 'Invalid sign up - try again'
    except Exception as err:
        print(err)
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class FoodList(ListView):
  model = Food

class FoodDetail(DetailView):
  model = Food

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'  

class FoodUpdate(UpdateView):
  model = Food
  fields = ['name', 'calories', 'portion']

class FoodDelete(DeleteView):
  model = Food
  success_url = '/foods/'

def add_meals(request, day_id):
    form = MealsForm(request.POST)
    if form.is_valid():
        new_meal = form.save(commit=False)
        new_meal.day_id = day_id
        new_meal.save()
    return redirect('detail', day_id=day_id)
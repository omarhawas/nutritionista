from django.shortcuts import render, redirect
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Day, Food




# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def days_index(request):
    days = Day.objects.all()
    return render(request, 'days/index.html', {'days': days }) 

def days_detail(request, day_id):
    day = Day.objects.get(id=day_id)
    return render(request, 'days/detail.html', {'day': day})

class DayCreate(CreateView):
    model = Day
    fields = '__all__'
    success_url = '/days/'

class DayUpdate(UpdateView):
    model = Day
    fields = '__all__'

class DayDelete(DeleteView):
    model = Day
    success_url = '/days/'



#Add day form
# def add_day(request, user_id):
# 	# create the ModelForm using the data in request.POST
#   form = DayForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the user_id assigned
#     new_day = form.save(commit=False)
#     new_day.user_id = user_id
#     new_day.save()
#   return redirect('detail', user_id=user_id)
def signup(request):
    error_message = ''
    try:
        if request.method == 'POST':
            # This is how to create a 'user' form object
            # that includes the data from the browser
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # This will add the user to the database
                user = form.save()
                # This is how we log a user in via code
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
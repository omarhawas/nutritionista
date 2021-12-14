from django.shortcuts import render
from .models import Day
# from .forms import DayForm







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
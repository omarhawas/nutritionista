from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm




# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def days_index(request):
    return render(request, 'days/index.html') #{'days': days })

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
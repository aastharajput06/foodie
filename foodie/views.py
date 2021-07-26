from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')    



def register(request):
    if request.method == "POST":
         form = CreateUserForm(request.POST)
    if form.is_valid():
          form.save()
          return redirect('login')
    else:
          form = CreateUserForm()
    return render (request, 'register.html', {'form': form})  
          

def login(request):
   
     return render(request, 'accounts/templates/login.html', context)  

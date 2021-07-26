from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
 


from .forms import CreateUserForm
from .models import *
from django.contrib import messages


def register(request):
   form = CreateUserForm()
    
    
   if request.method == "POST": 
          form = CreateUserForm(request.POST) 
          if form.is_valid():
              form.save()
              return redirect('login')
   
   context = {'form':form}
   return render(request, 'register.html', context)  
          

def loginPage(request):
       
     if request.method == "POST":
           username = request.POST.get('username')
           password =  request.POST.get('password')

           user = authenticate(request, username=username, password=password)

           if user is not None:
                 login(request, user) 
                 return redirect('register')

           else:
              messages.info(request, 'Username OR Password is incorrect')      

     context = {}
     return render(request, 'login.html', context)

# def logoutUser(request):
#     return redirect('login')        


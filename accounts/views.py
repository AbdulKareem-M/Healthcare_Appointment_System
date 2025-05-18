from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import RegisterForm, LoginForm
from django.views.generic import View

class RegisterView(View):
  def get(self, request):
    form = RegisterForm()
    return render(request,'register.html',{'form':form})
  
  def post(self, request):
    form = RegisterForm(request.POST)
    if form.is_valid():
      User.objects.create_user(**form.cleaned_data)
      
      return redirect('login')
    else:
      form = RegisterForm()
      return render(request,'register.html',{'form':form})


class LoginView(View):
  def get(self, request):
    form = LoginForm()
    return render(request,'login.html',{'form':form})
  
  def post(self, request):
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        return redirect('appointment-list')
      else:
        form = LoginForm()
        return render(request, 'login.html',{'form':form})
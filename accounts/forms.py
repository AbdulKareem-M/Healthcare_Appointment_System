from django import forms
from .models import User

class RegisterForm(forms.Form):
  
  username = forms.CharField(max_length=50)
  first_name = forms.CharField(max_length=50)
  last_name = forms.CharField(max_length=50)
  password = forms.CharField(widget=forms.PasswordInput())
  email = forms.EmailField()

class LoginForm(forms.Form):
  username = forms.CharField(max_length=50)
  password = forms.CharField(widget=forms.PasswordInput())
  
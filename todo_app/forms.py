from django.contrib.auth.models import User
from django import forms 
from todo_app.models import *
from .models import User


class register(forms.ModelForm):
    class Meta:
      model=User
      fields=('username','email','password')


      widgets = {
                  "username": forms.TextInput(attrs={"class":"form-control"}),
                  "email": forms.EmailInput(attrs={"class":"form-control"}),
                  "password": forms.PasswordInput(attrs={"class":"form-control"}),
        
      }
      
      
class loginform(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))   


class task_add(forms.ModelForm):
   class Meta:
      model=task
      fields = ['name']

      widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Add your task"})
      }
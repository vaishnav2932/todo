from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from todo_app.models import task


class register(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()   

class taskform(forms.ModelForm):
    class Meta:
        model=task 
        fields=['name',]


            
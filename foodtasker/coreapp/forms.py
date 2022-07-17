import logging
from django import forms
from django.contrib.auth.models import User
from coreapp.models import Restorant
from django.db import models
from django.contrib.auth import authenticate ,login 

class UserForm(forms.ModelForm):
    email=forms.CharField(max_length=100 ,required=True)
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=("username","password","first_name","last_name","email")
class RestorantForm(forms.ModelForm):
    class Meta:
        model=Restorant
        fields=("name","phone","adress","logo")

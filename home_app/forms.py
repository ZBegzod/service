from django import forms
from django.forms import Form, ModelForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterModelform(forms.ModelForm):
    confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password', 'confirm'] 
        widgets = {'password':forms.PasswordInput()}

class UserLoginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    class Meta:
        widgets = {'password':forms.PasswordInput()}

class ResursSearchForm(forms.Form):
    title = forms.CharField()
    product_quantity = forms.IntegerField()
    price = forms.FloatField()

class ResursModelform(forms.ModelForm):
    class Meta:
        model = Resurs
        fields = '__all__' 


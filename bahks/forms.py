from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

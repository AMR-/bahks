from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import models
from django.contrib.auth.models import User
import forms

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            login(request, user)
            return redirect('/storage')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = forms.UserForm()
        return render(request, 'signup.html', {'form': form})

@login_required(login_url='/login')
def boxes(request):
    return render(request, 'boxes.html')

def loginView(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/storage')
        else:
            return render(request, 'login.html')
    else:
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})

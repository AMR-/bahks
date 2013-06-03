from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import models
from django.contrib.auth.models import User
import models
import forms
import ups
from PIL import Image

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('/storage')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = forms.UserForm()
        return render(request, 'signup.html', {'form': form})

def boxes(request):
    boxes = models.Box.objects.filter(username=request.user)
    return render(request, 'boxes.html', {'boxes' : boxes})

#def addresses(request):
#    addresses = models.Address.objects.filter(username=request.user)
#    return render(request, '', {'addresses' : addresses})

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

def send(request):
    if request.method == 'POST':
        box = models.Box()
        box.username = request.user
        box.status = 'Labeled'
        box.save()
        shipment = ups.set_up_shipment("Austin Robinson", "1250 Ocean Avenue", "Brooklyn", "NY", "US", "11230",
                    "9198891172", "Bill Mandy", "399 Smith Street", "Brooklyn", "NY", "US", "11231", "9198891172",
                    ".1", ".1", ".1", ".1")
        ups.save_label(shipment)
        return redirect('/image')
    else:
        return render(request, 'send.html')

@login_required(login_url='/login')
def account(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            up = form.save()
            up.user = request.user
            up.save()
            return redirect('/storage')
    else:
        form = forms.UserForm(instance=request.user)
        return render(request, 'account.html', {'form': form})

def retrieve(request, boxId):
    models.Box.objects.filter(orderID=boxId).delete()
    return redirect('/storage')

def serveImage(request):
    im = Image.open("/tmp/label.gif")
    response = HttpResponse(mimetype="image/gif")
    im.save(response, "GIF")
    return response

def pricing(request):
    return render(request, 'pricing.html')

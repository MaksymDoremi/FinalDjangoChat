from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

# Create your views here.
def frontpage(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    #return render(request, 'registration.html')
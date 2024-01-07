from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout

# Create your views here.
def frontpage(request):
    return render(request, 'frontpage.html')

def signin(request):
    return render(request, 'login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("frontpage")
    return render(request, "logout.html")

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            user = form.save()

            login(request, user)

            success_message = "User created"
            return render(request, 'registration.html', {'success_message': success_message})
    #return render(request, 'registration.html')
    else:
        form = RegistrationForm()

    
    error_message = ""
    for field in form:
            for error in field.errors:
                error_message+=error

    return render(request, 'registration.html', {'error_message': error_message})
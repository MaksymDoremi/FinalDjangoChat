from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout

# Create your views here.
def frontpage(request):
     """
     Renders blank html page
     """
     return render(request, "frontpage.html")

def logout_view(request):
    """
    Renders logout view and performs logout
    """
    if request.method == "POST":
        logout(request)
        return redirect("frontpage")
    return render(request, "logout.html")

def registration(request):
    """
    Renders registration form and performs registration using built-in models.user
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            user = form.save()

            # logging into system
            login(request, user)

            success_message = "User created"
            # rendering success message
            return render(request, 'registration.html', {'success_message': success_message})
    #return render(request, 'registration.html')
    else:
        form = RegistrationForm()

    # in case of errors show them
    error_message = ""
    for field in form:
            for error in field.errors:
                error_message+=error

    return render(request, 'registration.html', {'error_message': error_message})
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
# Create your views here.

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')

def service(request):
    return render(request, 'service.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')
def event(request):
    return render(request, 'event.html')
def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='login')
def makeDonation(request):
    return render(request, 'make_donation.html')

def myDonation(request):
    """
    Render the 'my_donation.html' template.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered 'my_donation.html' page.
    """
    return render(request, 'my_donation.html')


def user_registration(request):  # sourcery skip: extract-method
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('/')
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method != 'POST':
        return render (request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user= CustomUser.objects.get(username=username)
        # user.set_password(password)
    except CustomUser.DoesNotExist:
        messages.error(request, 'username does not exist!')
        return render (request, 'login.html')
    user = authenticate(request, username=username, password=password)

    if user is None:
        messages.error(request, 'Incorrect password')
        return render (request, 'login.html')

    elif user.is_active:
        login(request, user)
        messages.success(request, 'Logged in succesfully')
    else:
        messages.error(request, 'Please activate your account')
        return render (request, 'login.html')
    return redirect('/')
    
def logout_user(request):
    logout(request)
    return redirect('/')
# Create your views here.
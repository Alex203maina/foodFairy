from django.shortcuts import render

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

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
def event(request):
    return render(request, 'event.html')
def blog(request):
    return render(request, 'blog.html')
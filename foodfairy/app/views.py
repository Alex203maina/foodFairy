from django.shortcuts import render, redirect,get_object_or_404
from .models import CustomUser, BlogPost, Event, Event, Contact, Volunteer
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from app.utils import send_registration_email

# Create your views here.
def login_required_redirect(request):
    messages.warning(request, "Please log in or create an account to access this page.")
    return redirect(f'/login/?next={request.path}')
def home(request):
    events = Event.objects.all().order_by('-date')[:2]
    blogs = BlogPost.objects.all().order_by('-date')[:3]
    return render(request, 'index.html',{'blogs':blogs, 'events':events})
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'profile.html')
def team(request):
    return render(request, 'team.html')

def service(request):
    return render(request, 'service.html')

def donate(request):
    return render(request, 'donate.html')

def volunteer(request):
    return render(request, 'volunteer.html')
def contact(request):
    return render(request, 'contact.html')
def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
def blog(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})
def blog_detail(request, id):
    # Use get_object_or_404 to fetch the blog post by ID
    blog = get_object_or_404(BlogPost, id=id)

    # Pass the blog object to the template context
    return render(request, 'blog_detail.html', {'blog': blog})
@login_required(login_url='/login')
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

try:
    def user_registration(request):  
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # send the registration email to user
                send_registration_email(user)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'You have signed up successfully.')
                login(request, user)
                return redirect('/')
            else:
                print(form.errors)  # Debug: Print form errors in case of invalid form
                messages.error(request, 'Please correct the errors below.')
        return render(request, 'register.html', {'form': form})
except Exception as e:
    print(f"Error during registration: {e}")
    messages.error(request, 'An error occurred during registration. Please try again.')
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
        messages.success(request, 'Logged in successfully')
    else:
        messages.error(request, 'Please activate your account')
        return render (request, 'login.html')
    return redirect('/')
    
def logout_user(request):
    logout(request)
    return redirect('/')
# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        phone = request.POST.get('phone_number')
        
        contact = Contact(name=name, email=email, subject=subject, message=message, created_at=Contact.created_at)
        
        contact.save()
        
        messages.success(request, 'Your message has been sent successfully.')
        
        return redirect('/contact')
    return render(request, 'contact.html')

def volunteer_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        volunteer = Volunteer(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, message=message)
        
        volunteer.save()
        
        messages.success(request, 'Your information has been submitted successfully.')
        
        return redirect('/volunteer')
    return render(request, 'volunteer.html')
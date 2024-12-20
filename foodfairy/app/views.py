from django.shortcuts import render, redirect,get_object_or_404
import requests
from .models import CustomUser, BlogPost, Event, Event, Contact, Volunteer, Donate,SocialHandler,TeamMember,EventRegistration,EventImage
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, DonationForm,ProfileUpdateForm, ProfileImage, EventRegistrationForm
from app.utils import send_registration_email

# Create your views here.
def login_required_redirect(request):
    messages.warning(request, "Please log in or create an account to access this page.")
    return redirect(f'/login/?next={request.path}')
def home(request):
    events = Event.objects.all().order_by('-date')[:2]
    blogs = BlogPost.objects.all().order_by('-date')[:3]
    socials = SocialHandler.objects.first()
    team_members = TeamMember.objects.all().order_by('-created_at')[:4]

    return render(request, 'index.html',{'blogs':blogs, 'events':events, 'socials':socials, 'team_members':team_members})
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'profile.html')
def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html',{'team_members':team_members})

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
    donations = Donate.objects.filter(donor=request.user)
    

    return render(request, 'my_donation.html', {'donations': donations})


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
def login_user(request):
    if request.method != 'POST':
        return render (request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user= CustomUser.objects.get(username=username)
        print(user)
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

def create_donation(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            # Set the donor to the currently logged-in user
            donation = form.save(commit=False)  # Don't save yet, we need to add donor
            donation.donor = request.user  # Associate the logged-in user as the donor
            donation.save()  # Now save the donation to the database

            # Add a success message (optional)
            messages.success(request, 'Thank you for your donation!')

            # Redirect to the 'mydonations' page
            return redirect('/make_donation/') 
        else:
            return render(request, 'make_donation.html', {'form': form})  # Show form with errors
    else:
        form = DonationForm()  # Initialize the form
        return render(request, 'make_donation.html', {'form': form})
    
@login_required(login_url='/login')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Handle optional password update
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if password or confirm_password:  # Only check if either field is provided
                if password == confirm_password:
                    if len(password) > 3:  # Basic length validation
                        user.set_password(password)
                        messages.success(request, "Password updated successfully!")
                    else:
                        messages.error(request, "Password must be longer than 3 characters.")
                        return redirect('/profile')
                else:
                    messages.error(request, "Passwords do not match.")
                    return redirect('/profile')
            
            user.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('/profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})

@login_required(login_url='/login')

@login_required
def update_image(request):
    if request.method == 'POST':
        # Handle the file upload
        form = ProfileImage(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile image has been updated successfully!')
            return redirect('/profile')  # Redirect to the updated profile page
    else:
        form = ProfileImage(instance=request.user)  # Pre-fill the form with the user's current profile

    return render(request, 'update_profile.html', {'form': form})
@login_required
def delete_account(request):
    if request.method == 'POST':  
        user = request.user
        user.delete() 
        logout(request)
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('app:home') 

    return render(request, 'settings.html') 
@login_required
def profile_settings(request):
    if request.method == "POST":
        user = request.user
        # Save the dark mode preference
        user.dark_mode = request.POST.get('dark_mode') == 'on'
        user.save()

    return render(request, 'settings.html', {'user': request.user})


def event_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch the specific event
    if request.method == 'POST':
        print(request.POST)
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event  # Associate the event with the registration
            registration.save()
            messages.success(request, 'You have successfully registered for the event!')
            return redirect('app:home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EventRegistrationForm()
    return render(request, 'event_registration.html', {'form': form, 'event': event})

def gallery(request):
    images = EventImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

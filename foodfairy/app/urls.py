from django.urls import path

from . import views

app_name = 'app'  # This is needed for reverse function in templates.  # Reverse('app:home') will return '/app/'

urlpatterns = [
    path('',views.home, name= 'home'),
    path('about/', views.about, name = 'about'),
    path('services/', views.service, name = 'service'),
    path('team/',views.team, name = 'team' ),
    path('donate/', views.donate, name = 'donate'),
    path('contact/', views.contact, name = 'contact'  ),
    path('login/', views.login_user, name = 'login'),
    path('signup/', views.user_registration, name ='register'),
    path('logout/', views.logout_user, name= 'logout'),
    path('event/', views.event, name = 'event'),
    path('blog/', views.blog, name = 'blog'),
    path('make_donation/', views.makeDonation, name = 'makeDonation'),
    path('my_donation/', views.myDonation, name = 'myDonation'),
    path('make_donation/', views.login_required_redirect, name='make_donation'),
    path('login-required/', views.login_required_redirect, name='login-required'),
    path('profile/', views.profile, name='profile'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),

]
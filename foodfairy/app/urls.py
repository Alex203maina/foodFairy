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
    path('login/', views.login, name = 'login'),
    path('signup/', views.register, name ='register'),
    path('event/', views.event, name = 'event'),
    path('blog/', views.blog, name = 'blog'),
    path('make_donation/', views.makeDonation, name = 'makeDonation'),
    path('my_donation/', views.myDonation, name = 'myDonation'),
]
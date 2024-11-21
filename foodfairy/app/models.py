from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users/', default='users/profile.png')
    organisation = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

# blog post
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    blog_image = models.ImageField(upload_to='blogs')
    
    def __str__(self):
        return self.title
    
class Beneficiary(models.Model):   
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    family_size = models.PositiveIntegerField(blank=True, null=True)
    institution_size = models.PositiveIntegerField(blank=True, null=True)
    beneficiary_type = models.CharField(max_length=100, choices=[
        ('individual', 'Individual'),
        ('family', 'Family'),
        ('institution', 'Institution'),
        ('community', 'Community'),
    ])    
    registration_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ], default='active')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'
        ordering = ['full_name']
        
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    date = models.DateField()
    location = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_image = models.ImageField(upload_to='events/')
    
    def __str__(self):
        return self.location
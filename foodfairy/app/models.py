from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users/', default='profile.png')
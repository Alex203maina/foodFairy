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
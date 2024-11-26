from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

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
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Query From : %s' % self.name

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Donate(models.Model):
    DONATION_TYPE_CHOICES = [
        ('food', 'Food'),
        ('money', 'Money'),
        ('clothing', 'Clothing'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('distributed', 'Distributed'),
    ]
    donor = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="donations")
    donation_type = models.CharField(max_length=50, choices=DONATION_TYPE_CHOICES, default='food')
    description = models.TextField(blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_distributed = models.BooleanField(default=False)
    is_perishable = models.BooleanField(default=False)
    shelf_life = models.IntegerField()
    beneficiary = models.ForeignKey(
        'Beneficiary',
        on_delete=models.SET_NULL,
        null = True,
        blank=True,
        related_name="received_donations",
    )
    distribution_center = models.ForeignKey(
        'DistributionCenter',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="donations_received",
        )
    date_donated = models.DateTimeField(default=now)
    

    class Meta:
        ordering = ['-date_donated']
        
    def __str__(self):
        return f"{self.donor} -- {self.donation_type} --{self.status} --{self.date_donated.strftime('%Y-%m-%d')}"
    
        
class DistributionCenter(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    current_stock = models.PositiveIntegerField()
    operation_hour = models.CharField(max_length=255,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Distribution Center"
        verbose_name_plural = "Distribution Center"
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name}-{self.location}"
    
    def is_full(self):
        """check if the center has reached its maximum capacity"""
        return self.current_stock >= self.capacity
    
    def add_stock(self,quantity):
        """add stock to the current Inventory"""
        if self.current_stock + quantity > self.capacity:
            raise ValueError("Cannot add stock. Center capacity exceeded")
        self.current_stock += quantity
        self.save()
        
    def remove_stock(self,quantity):
        """remove stock from the current Inventory"""
        if quantity > self.current_stock:
            raise ValueError("Cannot remove stock.Not enough Inventory quantity")
        self.current_stock -= quantity
        self.save()
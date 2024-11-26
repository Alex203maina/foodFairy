# from django.contrib.auth.models import User
from .models import CustomUser as User, Donate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
    
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['donation_type', 'description', 'quantity', 'is_perishable', 'shelf_life']
        def clean(self):
                cleaned_data = super().clean()
                status = cleaned_data.get('status')
                is_distributed = cleaned_data.get('is_distributed')

                # Check that the donation cannot be marked as 'distributed' if the status is 'pending'
                if status == 'pending' and is_distributed:
                    raise ValidationError("Cannot mark as distributed while status is 'pending approval'.")

                return cleaned_data
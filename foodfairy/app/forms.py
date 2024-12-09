# from django.contrib.auth.models import User
from .models import CustomUser as User, Donate,EventRegistration
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserChangeForm




class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'phone']
        
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['donation_type', 'description', 'quantity', 'is_perishable', 'shelf_life','unit']
class ProfileUpdateForm(forms.ModelForm):
    dark_mode = forms.BooleanField(required=False, initial=False)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'organisation', 'phone_number', 'id_number', 'nationality','dark_mode']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure password field has no initial value (blank or None)
        self.fields['password'].initial = None

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password or confirm_password:  # If either password field is filled
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.dark_mode = self.cleaned_data.get('dark_mode')

        password = self.cleaned_data.get('password')

        if password:  # Only set the password if it's not empty
            user.set_password(password)  # Use set_password to hash the password
        if commit:
            user.save()
        return user
class ProfileImage(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic'] 
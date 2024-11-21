from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BlogPost, Beneficiary, Event, Contact,Volunteer

# Customizing the display of CustomUser in the admin panel
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_active', 'date_joined')  
    list_filter = ('is_superuser', 'is_active', 'date_joined')  
    search_fields = ('username', 'email')  
    ordering = ('date_joined',) 

    # Custom fieldsets for the user form in the admin
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_superuser', 'is_staff'),
        }),
    )

# Registering the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Registering the other models
admin.site.register(BlogPost)
admin.site.register(Beneficiary)
admin.site.register(Event)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at') 
    list_filter = ('created_at',)  

# Register the Contact model with the custom ContactAdmin
admin.site.register(Contact, ContactAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'created_at')
    list_filter = ('created_at',)
    
    search_fields = ('first_name', 'email')
    
    # Register the Volunteer model with the custom VolunteerAdmin
admin.site.register(Volunteer, VolunteerAdmin)
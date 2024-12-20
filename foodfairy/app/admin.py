from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from .models import CustomUser, BlogPost, Beneficiary, Event, Contact,Volunteer,Donate,DistributionCenter,SocialHandler,TeamMember,EventRegistration,EventImage

admin.site.register(SocialHandler)
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
admin.site.register(Event)


class EventRegistrationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'email', 'phone', 'event', 'created_at', 'updated_at')
    
    # Adding search functionality for name, email, and event title
    search_fields = ('name', 'email', 'event__title')  # 'event__title' will allow searching by event title
    
    # Adding filters for event and registration date
    list_filter = ('event', 'created_at')

    # Adding a custom filter for counting registrations per event
    def count_registrations(self, obj):
        return EventRegistration.objects.filter(event=obj.event).count()

    # Adding the custom count field in the admin interface
    count_registrations.short_description = 'Number of Registrations'
    
    # Adding the count_registrations method in list_display
    list_display = ('name', 'email', 'phone', 'event', 'count_registrations', 'created_at', 'updated_at')

# Register the custom admin interface
admin.site.register(EventRegistration, EventRegistrationAdmin)

class DistributionCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location','capacity','contact_phone')
    
    list_filter = ('date_added',)
    
admin.site.register(DistributionCenter, DistributionCenterAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date')
    list_filter = ('date',)
admin.site.register(BlogPost, BlogPostAdmin)


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'location','beneficiary_type')
    list_filter = ('created_at',)
    
admin.site.register(Beneficiary, BeneficiaryAdmin)
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

class DonateAdmin(admin.ModelAdmin):
    list_display = ('donor', 'donation_type', 'status', 'is_distributed', 'beneficiary', 'date_donated')
    list_filter = ('date_donated', 'is_distributed')
    
    # Update search_fields to use related fields
    search_fields = ('donor__username', 'donation_type', 'status', 'beneficiary__name')  # Assuming 'name' is a field in the Beneficiary model

    def save_model(self, request, obj, form, change):
        # Check if status is 'pending' and is_distributed is True
        if obj.status == 'pending' and obj.is_distributed:
            messages.warning(request, "Cannot mark as distributed while status is 'pending approval'.")
        else:
            # Save the model if validation passes
            super().save_model(request, obj, form, change)

admin.site.register(Donate, DonateAdmin)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'created_at')
    list_filter = ('created_at',)
    
    search_fields = ('name', 'email')
    
admin.site.register(TeamMember, TeamMemberAdmin)

class EventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'caption', 'uploaded_at')
    list_filter = ('event', 'uploaded_at')
    search_fields = ('event__title', 'caption')
admin.site.register(EventImage, EventImageAdmin)
    
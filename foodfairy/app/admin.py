from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  CustomUser, BlogPost, Beneficiary, Event,Contact



# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BlogPost)
admin.site.register(Beneficiary)
admin.site.register(Event)
admin.site.register(Contact)

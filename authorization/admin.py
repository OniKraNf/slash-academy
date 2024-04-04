from django.contrib import admin
from .models import User, Profile
# from .models import User, Course

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email'] # That's displayed in admin panel
    
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def get_username(self, obj):
        return obj.user.username
    
    list_display = ["get_username", 'verified']
    

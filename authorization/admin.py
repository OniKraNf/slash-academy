from django.contrib import admin
from .models import User
# from .models import User, Course

# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'email'] # That's displayed in admin panel
    
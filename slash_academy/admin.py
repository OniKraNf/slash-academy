from django.contrib import admin

from slash_academy.models import Enroll

# Register your models here.
@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']
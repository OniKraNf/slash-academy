from django.contrib import admin
from .models import Webinar, WebinarLesson, Category
# Register your models here.


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    fields = ('name', 'author', 'category', 'description', 'language', 'includes', 'image', 'is_active', 'created_at', 'updated_at')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    
@admin.register(WebinarLesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_webinar_name']
    
    def get_webinar_name(self, obj):
        return obj.webinar.author.username
    
    get_webinar_name.short_description = 'Webinar author'
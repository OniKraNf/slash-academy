from django.contrib import admin
from .models import Course, Lesson, Category

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    fields = ('name', 'author', 'category', 'description', 'advantages', 'language', 'includes', 'image', 'price', 'is_active', 'created_at', 'updated_at')
    
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_course_name']
    
    def get_course_name(self, obj):
        return obj.course.author.username
    
    get_course_name.short_description = 'Course author'
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
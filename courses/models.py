import os
import shutil
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_delete
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from authorization.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


def course_image_path(instance, filename):
    return f'courses_images/{instance.name}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'  
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    advantages = models.CharField(max_length=500)
    language = models.CharField(max_length=200)
    includes = models.CharField(max_length=2000)
    placeholder = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=100, unique=True, primary_key=True, auto_created=False)
    image = models.ImageField(upload_to=course_image_path, unique=True, default='trashhold.png', )
    price = models.DecimalField(decimal_places=2, max_digits=5)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
    
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=100)
    duration = models.FloatField(validators=[MinValueValidator(0.30), MaxValueValidator(30.00)])
    video_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name
    

class LessonContent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessons_content')
    name = models.CharField(max_length=100)
    text_content = models.CharField(max_length=2000, blank=True)
    video_url = models.CharField(max_length=200, blank=True)
    duration = models.FloatField(validators=[MinValueValidator(0.30), MaxValueValidator(30.00)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    
@receiver(post_delete, sender=Course)
def auto_delete_file_course(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path) # For remove image
            folder_path = os.path.dirname(instance.image.path)
            shutil.rmtree(folder_path) # For remove directory 
        
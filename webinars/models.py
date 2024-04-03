import os
import shutil
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_delete
from django.utils.text import slugify
from authorization.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


def webinar_image_path(instance, filename):
    return f'webinars_images/{instance.name}/{filename}'


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
        
class Webinar(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=580, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=200)
    includes = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=100, unique=True, primary_key=True, auto_created=False)
    image = models.ImageField(upload_to=webinar_image_path, unique=True, default='trashhold.png', )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Webinar, self).save(*args, **kwargs)
    
    
@receiver(post_delete, sender=Webinar)
def auto_delete_file_webinars(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path) # For remove image
            folder_path = os.path.dirname(instance.image.path)
            shutil.rmtree(folder_path) # For remove directory 
        
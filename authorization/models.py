import os
import shutil

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.utils.text import slugify


# Create your models here.

class User(AbstractUser):
    email = models.CharField(unique=True)
    username = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.username
    
    def save(self, *args, **kwargs):
        if self.is_staff:
            self.is_active = True
        super().save(*args, **kwargs)
        
    
def user_directory_path(instance, file_name):
    return f'profiles_images/{instance.user.username}/{file_name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    information = models.CharField(max_length=2000)
    image = models.ImageField(default='default.png', upload_to=user_directory_path)
    verified = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    
    def __str__(self) -> str:
        return f'username: {self.user.username} verified: {self.verified}'
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_delete, sender=Profile)
def delete_image_path(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            folder_path = os.path.dirname(instance.image.path)
            shutil.rmtree(folder_path)
    
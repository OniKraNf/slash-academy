# Generated by Django 5.0.3 on 2024-04-02 19:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_category_course_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='course',
            name='courses_access',
            field=models.ManyToManyField(null=True, related_name='courses_access', to=settings.AUTH_USER_MODEL),
        ),
    ]

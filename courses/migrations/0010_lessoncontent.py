# Generated by Django 5.0.3 on 2024-04-09 15:25

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_merge_20240404_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text_content', models.CharField(blank=True, max_length=2000)),
                ('video_url', models.CharField(max_length=200)),
                ('duration', models.FloatField(validators=[django.core.validators.MinValueValidator(0.3), django.core.validators.MaxValueValidator(30.0)])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons_content', to='courses.lesson')),
            ],
        ),
    ]
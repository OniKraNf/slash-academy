<<<<<<< HEAD
# Generated by Django 5.0.3 on 2024-04-09 15:25
=======
# Generated by Django 5.0.3 on 2024-04-04 23:35
>>>>>>> ffe9a1cee150a51fff8de4f6ef3d167036060708

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0008_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

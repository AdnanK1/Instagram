# Generated by Django 4.0.5 on 2022-06-10 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_rename_profile_image_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='profile',
        ),
    ]

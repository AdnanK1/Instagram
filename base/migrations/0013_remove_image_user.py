# Generated by Django 4.0.5 on 2022-06-10 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_username_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]

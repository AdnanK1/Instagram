# Generated by Django 4.0.5 on 2022-06-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_image_hashtag_image_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='hashtag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

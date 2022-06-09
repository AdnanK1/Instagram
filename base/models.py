from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    photo = CloudinaryField('photo')
    Bio = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True)
    
    def __str__(self):
        return self.Bio

    def save_profile(self):
        self.save()

class Image(models.Model):
    image = CloudinaryField('image')
    hashtag = models.CharField(max_length = 30,null=True,blank=True)
    caption = models.TextField(null=True,blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)
    comments = models.TextField(null=True,blank=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name
    
    def number_of_likes(self):
        return self.likes.count()

    def save_image(self):
        self.save()


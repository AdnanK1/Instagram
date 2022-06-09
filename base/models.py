from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    liked = models.ManyToManyField(User,blank=True,default=None, related_name='blog_posts')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()


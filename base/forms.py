from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Image,Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PostForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','hashtag','caption']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'Bio']
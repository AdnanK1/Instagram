import imp
from django.test import TestCase
from .models import Profile,Image

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.caption = Image(caption= '')

    def test_instance (self):
        self.assertTrue(isinstance(self.caption, Image))

    def test_save_method(self):
        self.caption.save_post()
        posts = Image.objects.all()
        self.assertTrue(len(posts)>0)

class ProfileTestClass(TestCase):
     #setup method for this class
    def setUp(self):
        self.bio = Profile(bio = '')
    #testing whether we are being instanciated in the right way
    def test_instance(self):
        self.assertTrue(isinstance(self.bio, Profile))
    #testing the save method for this class
    def test_save_method(self):
        self.bio.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
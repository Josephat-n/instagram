from django.test import TestCase
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
   # Setup Method
   def setUp(self):
      self.profile=Profile(id = 1)
      self.image_one=Image(image_name='moana',image_caption='By the seashore',image_comments= 'Quality image')
      
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.image_one,Image))    
      
   # Testing Save Method
   def test_save_method(self):
      self.image_one.save_image()
      imgs = Image.objects.all()
      self.assertTrue(len(imgs) > 0)    
   
   # Teardown Method
   def tearDown(self):
      Image.objects.all().delete()    
   
   #Delete Method   
   def test_delete(self):
      self.image_one.save_image()    
      self.image_one.delete_image()
      imgs=Image.objects.all()
      self.assertTrue(len(imgs)<1)    
      
   #Update Method
   def test_update(self):
      self.image_one.save_image()
      self.image_one.image_caption.update()

class ProfileTestClass(TestCase):
   # Setup Method
   def setUp(self):
      # self.name=User(id = 1)
      self.profile_one=Profile(bio= 'A cool dude', name_id=1)
      
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.profile_one,Profile))    
      
   # Testing Save Method
   def test_save_method(self):
      self.profile_one.save_profile()
      prof = Profile.objects.all()
      self.assertTrue(len(prof) > 0)    
   
   # Teardown Method
   def tearDown(self):
      Profile.objects.all().delete()           
   
   #Delete Method   
   def test_delete(self):
      self.profile_one.save_profile()    
      self.profile_one.delete_profile()
      prof = Profile.objects.all()
      self.assertTrue(len(prof)<1)      
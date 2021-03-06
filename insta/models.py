from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   name = models.ForeignKey(User,on_delete=models.CASCADE)
   profile_photo = ImageField(blank=True, manual_crop="") 
   bio = models.TextField()
   
   def __str__(self):
      return self.name
   
   @classmethod
   def get_all(cls):
      """
      This function allows for the fetching of all the profile objects from the database
      """
      prof = Profile.objects.all()
      return prof
   
   def save_profile(self):
      """
      Save a profile to the database    
      """
      self.save()   
   
   def delete_profile(self):
      """
      function to delete a profile from the db
      """
      self.delete()      
   
class Image(models.Model):
   image_name = models.CharField(max_length =30)
   image_image = ImageField(blank=True, manual_crop="")
   image_caption = models.TextField()
   image_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default = 1)
   image_likes = models.IntegerField(default = 0)
   image_comments = models.TextField(blank = True)   
   
   def __str__(self):
      return self.image_name
   
   @classmethod
   def get_all(cls):
      """
      This function allows for the fetching of all the image objects from the database
      """
      imgs = Image.objects.all()
      return imgs  
   
   def save_image(self):
      """
      Save a new image to the database    
      """
      self.save()
      
   def delete_image(self):
      """
      function to delete an image from the db
      """
      self.delete()  
   
   def update_image(self):
      """
      function to update the caption of an image
      """
      self.image_caption.update()        
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField


# Create your models here.


class Profile(models.Model):

   user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
   bio = models.TextField()

   profile_image = models.ImageField(null=True,blank=True,upload_to="images/profile/")
   website_link = models.CharField(max_length=255,null=True,blank=True)
   facebook_link = models.CharField(max_length=255,null=True,blank=True)
   twitter_link = models.CharField(max_length=255,null=True,blank=True)
   instagram_link = models.CharField(max_length=255,null=True,blank=True)
   pinterest_link = models.CharField(max_length=255,null=True,blank=True)
   linkedin_link = models.CharField(max_length=255,null=True,blank=True)




   def __str__(self):
      return str(self.user) # this is an object need to convert it on string

class Category(models.Model):
   name = models.CharField(max_length=255)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('home_link')



class Post(models.Model):
   title = models.CharField(max_length=255)

   headr_images = models.ImageField(null=True,blank=True,upload_to="images/")

   title_page =models.CharField(max_length=255)
   author =models.ForeignKey(User, on_delete=models.CASCADE)
   #body =models.TextField()
   body = RichTextField(blank=True,null=True)

   post_date =models.DateField(auto_now_add=True)
   category = models.CharField(max_length=255,default="uncatpegorized")
   snippet = models.CharField(max_length=255, default="")
   likes = models.ManyToManyField(User,related_name='blog_posts') #


   #function for counting likes
   def likes_count(self):
      return self.likes.count()


   def __str__(self):
      return self.title + ' | ' + str(self.author)

   # take action and redirect to  "post_link" where we view the post after submitting
   def get_absolute_url(self): #after submittng the button and go fo page!
      return reverse('post_link',args=(str(self.id))) #args=(str(self.id)) this argument helps to viewing the current post

   #here after submitting we want to redicret to direct home page insted of viewing the current post
   def get_absolute_url(self):
      return reverse('home_link') #redirect to home including with the other post

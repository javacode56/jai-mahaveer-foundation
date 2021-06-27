from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



# Create your models here.

class UserProfileInfo(models.Model):
#create relationship (don't inherit from user!)
    user=models.OneToOneField(User)

    #Add any additional attributes we want
    address=models.CharField(max_length=500)
    amount=models.PositiveIntegerField()
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    slug=models.SlugField(max_length=200,db_index=True)


    def get_absolute_url(self):
        return reverse('newapp:update',kwargs={'pk':self.pk})
    def __str__(self):

        #Built-in attribute of django.contrib.auth.models.User (we used user name after on form like welcome user name)
        return self.user.username





class DonorProfileInfo(models.Model):
#create relationship (don't inherit from user!)
    username=models.CharField(max_length=500)
    email=models.EmailField(max_length=100)
    #Add any additional attributes we want
    address=models.CharField(max_length=500)
    amount=models.PositiveIntegerField()
    mobile=models.PositiveIntegerField()
    slug=models.SlugField(max_length=200,db_index=True)





    def __str__(self):

        #Built-in attribute of django.contrib.auth.models.User (we used user name after on form like welcome user name)
        return self.username

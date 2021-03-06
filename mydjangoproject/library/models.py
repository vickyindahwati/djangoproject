from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pengarang(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    sinopsis = models.TextField(null=True,blank=True)
    pengarang=models.ForeignKey(Pengarang,null=True,blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

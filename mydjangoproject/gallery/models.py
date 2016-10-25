from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=40)
    picture = models.ImageField()
   
    def __str__(self):
        return self.name
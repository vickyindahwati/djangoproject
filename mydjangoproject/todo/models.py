from django.db import models
from django.utils import timezone

# Create your models here.
class Schedule(models.Model):
    to_do = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.to_do

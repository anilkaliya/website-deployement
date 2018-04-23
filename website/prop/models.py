from django.db import models
from django.urls import reverse
class proper(models.Model):
    location=models.CharField(max_length=256)
    price=models.CharField(max_length=20)
    area=models.CharField(max_length=20)
    sector=models.CharField(max_length=3)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('home')

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Watch(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    brand=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')
    material=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    colour=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
# Create your models here.

class Userlog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'


from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    excerpt = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

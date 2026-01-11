from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .fields import EncryptedField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = EncryptedField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    excerpt = EncryptedField()

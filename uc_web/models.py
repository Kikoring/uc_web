from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Memo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_date =models.DateTimeField(auto_now_add=True)
    
    

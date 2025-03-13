from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=20)

class Memo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True
    )

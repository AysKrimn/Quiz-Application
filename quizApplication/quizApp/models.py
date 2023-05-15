from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.FileField(upload_to='quizApp/static/profilePicture', null=True)

class Category(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    def __str__(self):
        return self.title
    
class Quizes(models.Model):
    title = models.CharField(max_length=35)
    detail = models.TextField()
    date_joined = models.DateTimeField(default=timezone.now)
    banner = models.FileField(upload_to='quizApp/static/quizBanner', null=True)
    timer = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
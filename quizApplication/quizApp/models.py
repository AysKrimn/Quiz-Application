from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    def __str__(self):
        return self.title
    
class Quizes(models.Model):
    title = models.CharField(max_length=35)
    detail = models.TextField()
    date_joined = models.DateTimeField(default=timezone.now)
    banner = models.FileField(upload_to='static/img', null=True)
    timer = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    roll=IntegerField()
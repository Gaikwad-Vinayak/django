from django.db import models
from .manager import custom_manager 
# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=20)
    marks=models.IntegerField()
    pass_date=models.DateField()

    students=custom_manager()


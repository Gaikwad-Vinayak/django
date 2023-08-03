from django.db import models

# Create your models here.
class student(models.Model):
    title=models.CharField(max_length=20)
    data=models.CharField(max_length=200)
    date=models.DateField()
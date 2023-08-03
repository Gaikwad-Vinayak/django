from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=20)
    marks=models.IntegerField()
    pass_date=models.DateField()


class teacher(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

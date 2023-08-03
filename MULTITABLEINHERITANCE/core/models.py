from django.db import models

# Create your models here.
class common(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)

class student(common):
    std=models.CharField(max_length=20)

class teacher(common):
    salary=models.CharField(max_length=20)
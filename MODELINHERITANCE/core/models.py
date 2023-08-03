from msilib.schema import Class
from pydoc import classname
from django.db import models

# Create your models here.
class commen(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    class Meta:
        abstract=True

class student(commen):
    city=models.CharField(max_length=20)

class teacher(commen):
    salary=models.IntegerField()
    
from weakref import proxy
from django.db import models

# Create your models here.
class common(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

class student(common):

    class Meta:
        proxy=True
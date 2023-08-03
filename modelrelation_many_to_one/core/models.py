from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=30)
    post_data=models.CharField(max_length=44)

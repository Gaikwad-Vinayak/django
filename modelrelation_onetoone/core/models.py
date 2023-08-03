from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class page(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    #user=models.OneToOneField(User,on_delete=models.CASCADE) 
    page=models.CharField(max_length=22)

# CASCADE IS USED TO USER DELETE IT CAN DELETE RELETED DATA
# PROTECT IT CAN FIRSTLY DELETE DATA RELETED USER THEN DELETE USER, DO NOT DELETE DIRECTLY USER
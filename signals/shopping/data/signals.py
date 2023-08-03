from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import post_save,post_delete,pre_migrate,post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.signals import request_started,request_finished

from .models import Customer

@receiver(user_logged_in,sender=User)
def loginsuc(sender,request,user,**kwargs):
    print(sender)
    print(request)
    print(user)

@receiver(user_logged_out,sender=User)
def loginsuc(sender,request,user,**kwargs):
    print(sender)
    print(request)
    print(user)

@receiver(user_login_failed,sender=User)
def loginsuc(request,**kwargs):
    print(request)

@receiver(post_save,sender=Customer)
def loginsuc(sender,instance,created,using,**kwargs):
    print('-----------------post save ----------------')
    print(sender)
    print(instance)
    print(created)
    print(using)


@receiver(post_delete,sender=Customer)
def loginsuc(sender,instance,using,**kwargs):
    print('-----------------post delete ----------------')
    print(sender)
    print(instance)
    print(using)


@receiver(pre_migrate)
def req(sender,**kwargs):
    print(sender)

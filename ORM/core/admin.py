from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import student
# Register your models here.
#admin.register(student)
class modeladmin(admin.ModelAdmin):
    list_display=['id','name','city','roll']
admin.site.register(student,modeladmin)
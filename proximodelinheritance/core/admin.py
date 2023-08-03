from django.contrib import admin
from .models import common,student
# Register your models here.

@admin.register(common)
class aadmin(admin.ModelAdmin):
    list_display=['id','city','name']

@admin.register(student)
class aadmisn(admin.ModelAdmin):
    list_display=['id','city','name']
from django.contrib import admin
from .models import common,student,teacher
# Register your models here.

@admin.register(common)
class cadmin(admin.ModelAdmin):
    list_display=['id','name','age']

@admin.register(student)
class cadmin(admin.ModelAdmin):
    list_display=['id','name','std']

@admin.register(teacher)
class cadmin(admin.ModelAdmin):
    list_display=['id','name','salary']
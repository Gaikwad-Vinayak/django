from django.contrib import admin
from .models import student,teacher
# Register your models here.
@admin.register(student)
class adminform(admin.ModelAdmin):
    list_display=['id','name','age','city']

@admin.register(teacher)
class adminform(admin.ModelAdmin):
    list_display=['id','name','age','salary']
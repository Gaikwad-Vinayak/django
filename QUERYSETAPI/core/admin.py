from django.contrib import admin
from .models import student,teacher
# Register your models here.

@admin.register(student)
class adminmodelclass(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date']

@admin.register(teacher)
class adminmodelclass(admin.ModelAdmin):
    list_display=['name','city']
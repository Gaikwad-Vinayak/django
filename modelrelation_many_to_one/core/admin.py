from django.contrib import admin
from .models import post
# Register your models here.
@admin.register(post)
class aadmin(admin.ModelAdmin):
    list_display=['id','post_title','post_data']
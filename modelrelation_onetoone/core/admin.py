from django.contrib import admin
from .models import page
# Register your models here.
@admin.register(page)
class aadmin(admin.ModelAdmin):
    list_display=['id','user','page']
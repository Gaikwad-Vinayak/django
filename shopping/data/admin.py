from django.contrib import admin
from .models import Customer,Product,Cart,Orderplace
# Register your models here.
@admin.register(Customer)
class registercustmer(admin.ModelAdmin):
    list_display=['user','name','address','address_2','city','state','pin_code']


@admin.register(Product)
class registerproduc(admin.ModelAdmin):
    list_display=['title','selling_price','discounted_price','discripition','brand','category','product_img']


@admin.register(Cart)
class registercart(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(Orderplace)
class registerorderplace(admin.ModelAdmin):
    list_display=['user','customer','Product','quantity','order_date','status']





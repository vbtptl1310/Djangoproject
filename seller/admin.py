from django.contrib import admin

from seller.models import *

# Register your models here.
@admin.register(Seller)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','password','pic']

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display= ['name','des','price','quantity','discount','pic','seller','discountedprice']

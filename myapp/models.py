
from unicodedata import name
from django.db import models

from seller.models import *

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def _str_(Self):
        return Self.product.name   

class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_status=models.CharField(max_length=50)

    def _str_(Self):
        return Self.user.name

class OrderDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    order=models.ForeignKey(order,on_delete=models.CASCADE)

    def _str_(Self):
        return Self.product.name

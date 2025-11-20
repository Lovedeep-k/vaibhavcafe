from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
    NAME=models.CharField(max_length=30)
    EMAIL=models.EmailField(max_length=50)
    PHONE=models.CharField(max_length=30)
    SUBJECT=models.CharField(max_length=30)


class products(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=5)


class CartItem(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class billing(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=50)
    Addres=models.CharField(max_length=80)
    Phone=models.CharField(max_length=30)

class shopp(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=5)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=50)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,null=False)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
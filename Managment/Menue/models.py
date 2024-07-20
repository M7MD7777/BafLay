from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    role=models.CharField(max_length=100,default='user')


    def __str__(self):
        return self.user.username


class Branche(models.Model):
    name = models.CharField(max_length=100)  
    country = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    image = models.ImageField(upload_to='branche_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class ParentCategory(models.Model):
    branche=models.ForeignKey(Branche,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='parent_category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    parent_category = models.ForeignKey(ParentCategory,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)  
    description = models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)


    def __str__(self):
        return self.name








   


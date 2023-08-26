from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length = 30)
    desc = models.CharField(max_length=50, default="add details")
    image = models.ImageField(upload_to = "images" , default=50)
    
    
    def __str__(self):
        return self.categoryname

    class Meta:
        db_table = "Category"

class Product(models.Model):
    pname = models.CharField(max_length= 50)
    price = models.FloatField(default = 200)
    desc = models.CharField(max_length= 200)
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        db_table = "Product"

class User(models.Model):
    fullname = models.CharField(max_length=40)
    usernm = models.CharField(max_length=40 , default="abc@123")
    email = models.EmailField(max_length=50, primary_key=True)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "User"

class MyCart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    prodct = models.ForeignKey(Product , on_delete= models.CASCADE)
    qty = models.IntegerField(default = 1)

    class Meta:
        db_table = "MyCart"

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    prodct = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    class Meta:
        db_table = "WishList"

class Address(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    contact= models.CharField(max_length=10)
    add = models.CharField(max_length=200)
    town = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = "Address"

class Payment(models.Model):
    card_no = models.CharField(max_length = 4)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default = 10000)

    class Meta:
        db_table = "Payment"

class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_order = models.DateField(default = datetime.now)
    amount = models.FloatField(default=1000)
    details = models.CharField(max_length=200)

    class Meta:
        db_table = "Orders"
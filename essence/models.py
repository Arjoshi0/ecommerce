from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  price = models.FloatField()
  stock = models.IntegerField()

class Customer(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  phone_no = models.IntegerField(unique=True)
  address = models.CharField(max_length=200)
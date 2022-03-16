from django.db import models
from myapp.models import Clothing

# Create your models here.
class Order(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postalcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

class Item(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

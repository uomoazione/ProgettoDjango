from django.db import models
from django.contrib.auth.models import User

#admin username: manuel -- email: manuelcampi20@gmail.com
#password: abc123
# Create your models here.
#min 17:30
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                # Cascade elimina tutto il customer, attributi compresi
                                blank=True)  # lega lo User col customer 1-1
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name  # valore di ritorno quando Customer chiamato


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)

    # digital è bool, così sappiamo se è fisico o meno il prodotto

    def __str__(self):
        return self.name


class Order(models.Model):  # il nostro carrello
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)  # oneToMany
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)  # return PK di Order


class OrderItem(models.Model):  # oggetto dentro carrello
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

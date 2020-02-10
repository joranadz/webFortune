from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    img = models.CharField(max_length=2083)
    info = models.CharField(max_length=2083)


class Discount(models.Model):
    code = models.CharField(max_length=55)
    info = models.CharField(max_length=255)
    discount = models.FloatField()

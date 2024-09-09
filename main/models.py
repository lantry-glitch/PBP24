from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField()
    quantity = models.PositiveIntegerField()

# Create your models here.


from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='images/') 
    quantity = models.PositiveIntegerField()

# Create your models here.


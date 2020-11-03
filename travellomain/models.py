from django.db import models

# Create your models here.


class Destination(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
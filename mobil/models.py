from django.db import models

# Create your models here.
class Avto(models.Model):
    marka = models.CharField(max_length=20)
    zavod = models.CharField(max_length=20)
    yaer = models.IntegerField()
    nomer = models.CharField(max_length=9)

from django.db import models
from django.conf import settings

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    size = models.FloatField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
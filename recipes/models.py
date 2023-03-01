from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    cuisine = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=500)
    directions = models.CharField(max_length=5000)
    time = models.PositiveBigIntegerField()

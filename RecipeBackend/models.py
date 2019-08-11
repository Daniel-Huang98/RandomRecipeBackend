from django.db import models
from django.conf import settings


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    imageURL = models.TextField()




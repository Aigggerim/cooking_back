from django.db import models

class Cook(models.Model):
    name = models.TextField()

class Recipe(models.Model):
    mainImage = models.TextField()
    title = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(Cook, on_delete=models.CASCADE, blank=True, null=True)
    ingredients = models.TextField()
    steps = models.TextField()

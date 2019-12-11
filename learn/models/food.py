from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    colors = models.CharField(max_length=20, default='')
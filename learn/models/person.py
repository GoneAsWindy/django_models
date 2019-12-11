from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField(max_length=30,verbose_name='名')
    last_name = models.CharField(max_length=30,verbose_name='姓')
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='L')


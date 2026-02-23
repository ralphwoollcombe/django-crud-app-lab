from django.db import models
from django.contrib.postgres.fields import ArrayField

class Person(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    interests = ArrayField(
        models.CharField(max_length=100),  
        default=list)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'


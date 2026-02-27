from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Interest(models.Model):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE,
    #     )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('interest-detail', kwargs={'pk': self.id})

class Category(models.Model):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True
    # )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Person(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    interests = models.ManyToManyField(Interest)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.id})

    
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

class Encounter(models.Model):
    date = models.DateField('Date')
    location = models.CharField(max_length=250)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Encounter with {self.person} at {self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']
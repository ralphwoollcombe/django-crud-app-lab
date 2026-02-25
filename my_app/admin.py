from django.contrib import admin

# Register your models here.
from .models import Person, Category, Interest, Encounter

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Interest)
admin.site.register(Encounter)
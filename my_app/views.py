from django.shortcuts import render
from .models import Person
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def person_index(request):
    person = Person.objects.all()
    return render(request, 'person/index.html', {'person': person})

def person_detail(request, person_id):
    Person.objects.get(id=person_id)
    return render(request, 'person/detail.html', {'person': person})
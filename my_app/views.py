from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class People:
    def __init__(self, name, location, category, subcategory, interests, description):
        self.name = name
        self.location = location
        self.category = category
        self.subcategory = subcategory
        self.interests = interests
        self.description = description

people = [
    People('Monty', 'London, UK', 'friend', 'BFF', [], 'My crazy queer party pal - a lovely link with many pals'),
    People('Ella', 'Bristol, UK', 'friend', 'London crew', [], 'My stunning soulmate sister'),
    People('Frances', 'London, UK', 'coding', 'peer', [], 'Main pal on my coding bootcamp'),
    People('Noa', 'London, UK', 'coding', 'instructor', [], 'My coding instructor' ),
    People('Blythe', 'London, UK', 'friend', 'London crew', [], 'new pal, absolute legend'),
    People('Alice K', 'Bristol, UK', 'documentary', 'wildlife', [], 'My main pal from my wildlife film era'),
]

def people_index(request):
    return render(request, 'people/index.html', {'people': people})
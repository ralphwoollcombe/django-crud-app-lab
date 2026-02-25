from django.shortcuts import render, redirect
from .models import Person
from .forms import EncounterForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class PersonList(ListView):
    model = Person

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['interest_form'] = InterestForm()
    #     return context

    
class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['encounter_form'] = EncounterForm()
        return context

class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person-index')

def add_encounter(request, pk):
    form = EncounterForm(request.POST)
    if form.is_valid():
        new = form.save(commit=False)
        new.person_id = pk
        new.save()
    return redirect('person-detail', pk=pk)
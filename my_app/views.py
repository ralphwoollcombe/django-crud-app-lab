from django.shortcuts import render, redirect
from .models import Person, Interest
from .forms import EncounterForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

class PersonList(LoginRequiredMixin, ListView):
    model = Person

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['name', 'location', 'category', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['interest_form'] = InterestForm()
    #     return context

    
class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interests_doesnt_have = Interest.objects.exclude(id__in = self.object.interests.all().values_list('id'))
        context['encounter_form'] = EncounterForm()
        context['interests'] = interests_doesnt_have
        return context

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['name', 'location', 'category', 'description']

class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person-index')

@login_required
def add_encounter(request, pk):
    form = EncounterForm(request.POST)
    if form.is_valid():
        new = form.save(commit=False)
        new.person_id = pk
        new.save()
    return redirect('person-detail', pk=pk)

class InterestList(LoginRequiredMixin, ListView):
    model = Interest

class InterestCreate(LoginRequiredMixin, CreateView):
    model = Interest
    fields = ['name']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class InterestDetail(LoginRequiredMixin, DetailView):
    model = Interest

class InterestUpdate(LoginRequiredMixin, UpdateView):
    model = Interest
    fields = ['name']

class InterestDelete(LoginRequiredMixin, DeleteView):
    model = Interest
    success_url = reverse_lazy('interest-index')

@login_required
def associate_interest(request, person_id, interest_id):
    # Note that you can pass a toy's id instead of the whole object
    Person.objects.get(id=person_id).interests.add(interest_id)
    return redirect('person-detail', pk=person_id)

@login_required
def remove_interest(request, person_id, interest_id):
    Person.objects.get(id=person_id).interests.remove(interest_id)
    return redirect('person-detail', pk=person_id)

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('person-index')
        else:
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
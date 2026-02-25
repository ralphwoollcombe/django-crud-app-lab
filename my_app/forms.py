from django import forms
from .models import Person, Interest, Encounter
from django.contrib.auth.models import User


# class PersonForm(forms.ModelForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Interest.objects.none(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    # class Meta:
    #     model = Person
    #     fields = '__all__'


#     def __init__(self, *args, user=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         if user:
#             self.fields['interests'].queryset = Interest.objects.filter(user=user)

# class InterestForm(forms.ModelForm):
#     class Meta:
#         model = Interest
#         fields = ['name']


class EncounterForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['date', 'location']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }),
        }
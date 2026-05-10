from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    name = forms.CharField(label="Name",
                             widget=forms.TextInput(attrs={"placeholder": "Enter your name",
                                                           "class": "validate"}))
    surname = forms.CharField(label="Surname",
                             widget=forms.TextInput(attrs={"placeholder": "Enter your surname",
                                                           "class": "validate"}))
    email = forms.EmailField(initial="john@example.com", label="Email")
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "(111) 11-11-111"}), label="Your phone number")
    additional = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your additional"}), label="Enter your additional")

    class Meta:
        model = Person
        fields = ['name', 'surname', 'email', 'phone', 'additional']
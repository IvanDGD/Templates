from django import forms
from django.forms import widgets

choices =[
    (1, "English"),
    (2, "Spanish"),
    (3, "French"),
    (4, "Ukrainian")
]

class UserForm(forms.Form):
    field_order = ["password", "surname", "name", "set_lang", "about"]

    #BooleanField = input:checkbox
    #EmailField = input:email
    #CharField = input:text
    #ChoiceField = select
    #DecimalField = input:number

    f_name = forms.CharField(initial="John", label="name",
                             widget=forms.TextInput(attrs={"placeholder": "Enter your name",
                                                           "class": "validate"}))
    surname = forms.CharField(initial="Smith", label="surname")
    age_field = forms.IntegerField(initial=18, min_value=18, max_value=100, label="age")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter password")
    about = forms.CharField(widget=forms.Textarea, required=True)
    set_lang = forms.ChoiceField(choices=choices, required=False)
    langs = forms.MultipleChoiceField(choices=choices, required=False)

    avatar = forms.ImageField(label="Upload your avatar", required=False)

    error_css_class = "error-text"
    required_css_class = "validate-required"

    def clean_f_name(self):
        data = self.cleaned_data["f_name"]

        if "joe" in str(data).lower():
            self.add_error("f_name", "Name cannot contain 'joe'")

        return data

    def clean(self):
        return super().clean()
    

monthCountChoices =[
    (1, "1 Month"),
    (2, "3 Months"),
    (3, "6 Months"),
    (4, "12 Months")
]

bottleVolumeChoices =[
    (1, "5 liters"),
    (2, "10 liters"),
    (3, "15 liters")
]
class WaterOrderForm(forms.Form):
    name = forms.CharField(label="Name",
                             widget=forms.TextInput(attrs={"placeholder": "Enter your name",
                                                           "class": "validate"}))
    surname = forms.CharField(initial="Smith", label="Surname",
                             widget=forms.TextInput(attrs={"placeholder": "Enter your surname",
                                                           "class": "validate"}))
    email = forms.EmailField(initial="john@example.com", label="Email")
    number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "(111) 11-11-111"}), label="Your phone number")
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your address"}), label="Enter your address")

    monthCount = forms.ChoiceField(choices=monthCountChoices, label="Month Count")
    bottleVolume = forms.ChoiceField(choices=bottleVolumeChoices, label="Bottle Volume")


    error_css_class = "error-text"
    required_css_class = "validate-required"

    def clean(self):
        return super().clean()
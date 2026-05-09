from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.
import random
class Person:
    def __init__(self, name, age, surname):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname} is {self.age} years old"
    

def index(request):
    context = {}
    context["welcom_text"] = "Welcome to the world of Django Templates"
    context["html_tag"] = '<h3 style="color: red;">HTML tag</h3>'
    context['value_int'] = 100
    context['value_float'] = 3.14
    context["value_bool"] = False

    context["list"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    context["dict"] = {"name": "Alex", "surname": "Smith", "age": 30}
    context["person"] = Person("Alex", 30, "Smith")
    context["random_value"] = random.randint(-100, 100)
    return render(request, "index.html", context = context)

def text_format(request):
    
    return TemplateResponse(request, "text_format.html", {"list" : [i for i in range(0, 10)]})

def contacts(request):
    persons = [
        Person("Alex", 30, "Smith"),
        Person("John", 25, "Doe"),
        Person("Jane", 28, "Doe")
    ]
    return TemplateResponse(request, "contacts.html", {"persons": persons})

def style(request):
    return TemplateResponse(request, "main_page.html")


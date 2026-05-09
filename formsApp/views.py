from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotAllowed, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from . import forms
from .forms import monthCountChoices, bottleVolumeChoices
from datetime import datetime
import os

userform = forms.UserForm()

def current_time():
    return str(int(datetime.timestamp(datetime.now())))

def index(request: HttpResponse):
    return render(request, "django_forms.html", {"form": forms.UserForm()})
"""
def postuser(request: HttpResponse):
    print("POST request received", request.POST)
    name = request.POST.get("name", "")
    surname = request.POST.get("surname", "")
    languages = request.POST.getlist("languages", [])
    password = request.POST.get("password", "")

    if (len(name) < 3 or len(surname) < 3):
        return HttpResponse("Name and surname must be at least 3 characters long")

    if password:
        print("Password", password)
    return render(request, "user_page.html", { "name": name, "surname": surname, "languages": languages})
"""

def postuser(request: HttpRequest):
    if request.method == "POST":
        userform = forms.UserForm(request.POST, request.FILES)
        if userform.is_valid():
            name = userform.cleaned_data["f_name"]
            surname = userform.cleaned_data["surname"]
            avatar = userform.cleaned_data.get("avatar")
            image_url = None
            if avatar:
                fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                file_type = avatar.name.split(".")[1]
                file_name = fs.save(f"{current_time()}.{file_type}", avatar)

                image_url = fs.url(file_name)
            return render(request, "user_page.html", {
                "name": name,
                "surname": surname,
                "imageUrl": image_url
            })
        return render(request, "django_forms.html", {"form": userform})
    return HttpResponseNotAllowed(["POST"])

orderform = forms.WaterOrderForm()

def orderform(request: HttpResponse):
    return render(request, "order_form.html", {"form": forms.WaterOrderForm()})

def postorder(request: HttpRequest):
    if request.method == "POST":
        orderform = forms.WaterOrderForm(request.POST)
        if orderform.is_valid():
            name = orderform.cleaned_data["name"]
            surname = orderform.cleaned_data["surname"]
            email = orderform.cleaned_data["email"]
            number = orderform.cleaned_data["number"]
            address = orderform.cleaned_data["address"]
            months_dict = dict(forms.monthCountChoices)
            volumes_dict = dict(forms.bottleVolumeChoices)
            month_label = months_dict.get(int(orderform.cleaned_data["monthCount"]))
            volume_label = volumes_dict.get(int(orderform.cleaned_data["bottleVolume"]))

            return render(request, "ordered_page.html", {
                "name": name,
                "surname": surname,
                "email": email,
                "number": number,
                "address": address,
                "monthCount": month_label,
                "bottleVolume": volume_label,
            })
        return render(request, "order_form.html", {"form": orderform})
    return HttpResponseNotAllowed(["POST"])
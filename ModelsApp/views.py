from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponse, JsonResponse
from .forms import PersonForm
from .models import Person, Product

#region Example
def seed(request):
    Product.objects.create(
        name="Product template",
        description="Description for Product 1",
        price=10.99
    ).save()
    return HttpResponse("Products seeded successfully.")

def get_all_products(request):
    products = Product.objects.all().values('id', 'name', 'description', 'price')
    return render(request, "products.html", {"products": products})

def add_product(request):
    seed(request)
    products = Product.objects.all().values('id', 'name', 'description', 'price')
    return render(request, "products.html", {"products": products})


def update_product(request, id):
    Product.objects.filter(id=id).update(
        price=90.00,
        name="Samsung"
    )
    products = Product.objects.all().values('id', 'name', 'description', 'price')
    return render(request, "products.html", {"products": products})

def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product.html", {"product": product})

def del_product(request, id):
    product = Product.objects.get(id=id).delete()
    products = Product.objects.all().values('id', 'name', 'description', 'price')
    return render(request, "products.html", {"products": products})

# products  = Product.objects.all().order_by("name")
# products  = Product.objects.all().order_by("-price")
#
# filter_products = Product.objects.filter(price=20)
# filter_products = Product.objects.filter(price__gt=20)
# filter_products = Product.objects.filter(price__lte=20)
# filter_products = Product.objects.filter(price__in=[10, 300])
# filter_products = Product.objects.filter(price__range=(10, 300))
# filter_products = Product.objects.filter(name__exact="Product 1")
# filter_products = Product.objects.filter(name__contains="proDuct 1")
# filter_products = Product.objects.filter(name__isstartwith="Pro")
# filter_products = Product.objects.filter(name__iendswith="ct 1")
# filter_products = Product.objects.filter(name__isstartwith="Pro") & Product.objects.filter(price__gt=20.00)
# filter_products = Product.objects.exclude(price=20.00)
#
# try:
#     product = Product.objects.get(id="24879a6752d24892958c94b36ee9faea")
#     print_product(product)
# except ObjectDoesNotExist:
#     print("Product with id 24879a6752d24892958c94b36ee9faea does not exist.")
#
# products = Product.objects.get_or_create(name="Product 5", description="Description for Product 5", price=50.99)
#
# try:
#     product = Product.objects.get(id="24879a6752d24892958c94b36ee9faea").delete()
# except:
#     pass
#
#
# Product.objects.filter(id="24879a6752d24892958c94b36ee9faea").update(name = "Samsung", price=F("price") + 10)

#endregion

def personform(request):
    persons = Person.objects.all()
    return render(request, "person_form.html", {
        "form": PersonForm(),
        "persons": persons
    })


def postperson(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_form')

        persons = Person.objects.all()
        return render(request, "person_form.html", {"form": form, "persons": persons})

    return HttpResponseNotAllowed(["POST"])

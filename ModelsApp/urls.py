from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path("", views.seed, name="seed"),
    # path('print/', views.get_all_products, name="print"),
    path("postperson/", views.postperson, name="person_post"),
    path("personform/", views.personform, name="person_form"),
    path("products/", views.get_all_products, name="products"),
    path("product/<str:id>", views.get_product, name="product"),
    path("delproduct/<str:id>", views.del_product, name="del_product"),
    path("updateproduct/<str:id>", views.update_product, name="update_product"),
    path("add_product/", views.add_product, name="add_product"),
]
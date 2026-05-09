from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="form_page"),
    path("postuser/", views.postuser, name="simple_form"),
    path("postorder/", views.postorder, name="order_form"),
    path("orderform/", views.orderform, name="order_page")
]
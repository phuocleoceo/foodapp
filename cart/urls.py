from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add_to_cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("plus_cart/<int:product_id>", views.plus_cart, name="plus_cart"),
    path("minus_cart/<int:product_id>", views.minus_cart, name="minus_cart"),
    path("remove_cart/<int:product_id>", views.remove_cart, name="remove_cart"),

    path("checkout", views.checkout, name="checkout")
]

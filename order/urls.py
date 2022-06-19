from django.urls import path
from . import views

urlpatterns = [
    path("place_order/", views.place_order, name="place_order"),
    path("history/", views.order_history, name="order_history")
]

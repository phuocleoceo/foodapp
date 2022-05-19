from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),
    path("category", views.CategoryManage, name="CategoryManage"),
    path("product", views.ProductManage, name="ProductManage"),
]

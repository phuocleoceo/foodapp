from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),

    path("category", views.ReadCategory, name="ReadCategory"),
    path("category/create", views.CreateCategory, name="CreateCategory"),
    path("category/<int:id>/update", views.UpdateCategory, name="UpdateCategory"),
    path("category/<int:id>/delete", views.DeleteCategory, name="DeleteCategory"),

    path("product", views.ReadProduct, name="ReadProduct"),
    path("product/create", views.CreateProduct, name="CreateProduct"),
    path("product/<int:id>/update", views.UpdateProduct, name="UpdateProduct"),
    path("product/<int:id>/delete", views.DeleteProduct, name="DeleteProduct"),
]

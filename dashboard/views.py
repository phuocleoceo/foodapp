from category.models import Category
from django.shortcuts import render
from product.models import Product


def HomePage(request):
    return render(request=request, template_name="dashboard/home.html")


def CategoryManage(request):
    # Các danh mục sản phẩm để hiển thị
    categories = Category.objects.all()
    return render(request=request, template_name="dashboard/category.html",
                  context={"categories": categories})


def ProductManage(request):
    # Các sản phẩm để hiển thị, kể cả không available
    products = Product.objects.all().filter()
    return render(request=request, template_name="dashboard/product.html",
                  context={"products": products})

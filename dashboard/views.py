from .forms import CategoryForm, ProductForm
from category.models import Category
from django.shortcuts import render
from product.models import Product


def HomePage(request):
    return render(request=request, template_name="dashboard/home.html")


def ReadCategory(request):
    # Các danh mục sản phẩm để hiển thị
    categories = Category.objects.all()
    return render(request=request, template_name="dashboard/category/read.html",
                  context={"categories": categories})


def CreateCategory(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CategoryForm()
    return render(request, "dashboard/category/create.html", context={"form": form})


def UpdateCategory(request, id):
    pass


def DeleteCategory(request, id):
    pass

####################################################################################


def ReadProduct(request):
    # Các sản phẩm để hiển thị, kể cả không available
    products = Product.objects.all().filter()
    return render(request=request, template_name="dashboard/product/read.html",
                  context={"products": products})


def CreateProduct(request):
    pass


def UpdateProduct(request, id):
    pass


def DeleteProduct(request, id):
    pass

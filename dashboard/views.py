from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, ProductForm
from category.models import Category
from django.shortcuts import render
from product.models import Product


def DashboardPage(request):
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
    return render(request, "dashboard/category/create-update.html", context={"form": form})


def UpdateCategory(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/dashboard/category")
    return render(request, "dashboard/category/create-update.html", context={"form": form})


def DeleteCategory(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        return redirect("/dashboard/category")
    return render(request, "dashboard/category/delete.html", context={"category": category})

#############################################################################################


def ReadProduct(request):
    # Các sản phẩm để hiển thị, kể cả không available
    products = Product.objects.all().filter()
    return render(request=request, template_name="dashboard/product/read.html",
                  context={"products": products})


def CreateProduct(request):
    form = ProductForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/dashboard/product")
    return render(request, "dashboard/product/create-update.html", context={"form": form})


def UpdateProduct(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(data=request.POST or None, files=request.FILES or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/dashboard/product")
    return render(request, "dashboard/product/create-update.html", context={"form": form})


def DeleteProduct(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect("/dashboard/product")
    return render(request, "dashboard/product/delete.html", context={"product": product})

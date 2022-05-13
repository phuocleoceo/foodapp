from django.shortcuts import render
from product.models import Product


def HomePage(request):
    products = Product.objects.all().filter(is_available=True)
    return render(request=request, template_name="home.html", context={"products": products})

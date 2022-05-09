from category.models import Category
from django.shortcuts import render
from .models import Product


# Create your views here.
def product(request):
    products = Product.objects.all().filter(is_available=True)
    quantity = products.count()
    categories = Category.objects.all()
    return render(request=request, template_name="product/product.html",
                  context={"products": products, "quantity": quantity, "categories": categories})

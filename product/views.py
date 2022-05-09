from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product


# Create your views here.
def product(request, category_slug=None):
    if category_slug != None:
        # Lấy ra category cần filter từ category_slug
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True)
    else:
        # Không dùng category để filter
        products = Product.objects.all().filter(is_available=True)

    # Đếm số lượng sản phẩm thu được
    quantity = products.count()
    # Các danh mục sản phẩm để hiển thị
    categories = Category.objects.all()
    return render(request=request, template_name="product/product.html",
                  context={"products": products, "quantity": quantity, "categories": categories})


def detail(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e
    return render(request=request, template_name="product/detail.html",
                  context={"product": product})

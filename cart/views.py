from django.shortcuts import redirect, render
from cart.models import Cart, CartItem
from product.models import Product


# Create your views here.
def cart_id_from_session(request):
    # Lấy ra cart id từ Session
    cart_id = request.session.session_key
    # Nếu không có thì tạo mới Session để lưu cart id
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def add_to_cart(request, product_id):
    """
    Hàm thêm 1 sản phẩm vào giỏ hàng
    """
    # Lấy ra sản phẩm bằng id
    product = Product.objects.get(id=product_id)
    try:
        # Lấy ra cart với id lấy từ Session
        cart = Cart.objects.get(cart_id=cart_id_from_session(request))
    except Cart.DoesNotExist:
        # Nếu cart chưa tồn tại thì ta tạo mới
        cart = Cart.objects.create(cart_id=cart_id_from_session(request))
    # Lưu cart
    cart.save()

    try:
        # Lấy ra cart_item, nếu đã tồn tại thì tăng số lượng thêm 1
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
    except:
        # Nếu chưa có thì tạo mới với số lượng là 1
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
    # Lưu cart_item
    cart_item.save()

    # Redirect về trang Cart (thật ra là reload trang)
    return redirect("cart")


def cart(request):
    return render(request=request, template_name="cart/cart.html")

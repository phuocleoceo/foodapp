from django.core.exceptions import ObjectDoesNotExist
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

    # Redirect đến trang Cart
    return redirect("cart")


def cart(request):
    total = 0
    quantity = 0
    cart_items = None
    try:
        # Dùng cart_id trong Session để lấy ra Cart
        cart = Cart.objects.get(cart_id=cart_id_from_session(request))
        # Lấy ra các Card_Item chưa thanh tóan từ cart
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        # Duyệt qua từng cart_item
        for ct in cart_items:
            # Tổng tiền = Đơn giá * số lượng
            total += ct.product.price * ct.quantity
            quantity += 1
    except ObjectDoesNotExist:
        pass
    return render(request=request, template_name="cart/cart.html",
                  context={"total": total, "quantity": quantity, "cart_items": cart_items})

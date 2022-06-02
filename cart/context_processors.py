from .views import cart_id_from_session
from .models import Cart, CartItem


def cart_count(request):
    """
    Context lưu số lượng sản phẩm trong giỏ hàng
    """
    cart_count_badge = 0
    if "admin" in request.path:
        return {}
    else:
        try:
            # Lấy cart hiện tại lưu trong session
            cart = Cart.objects.filter(cart_id=cart_id_from_session(request))
            # Lấy danh sách các cart_item của nó
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            # Đếm số lượng
            cart_count_badge = cart_items.count()
        except Cart.DoesNotExist:
            cart_count_badge = 0

    return dict(cart_count_badge=cart_count_badge)

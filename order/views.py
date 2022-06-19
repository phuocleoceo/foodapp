from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from order.models import Order, OrderDetail
from cart.models import CartItem
from .forms import OrderForm


# Create your views here.
@login_required(login_url="login")
def order_history(request):
    orders = Order.objects.order_by('-created_at').filter(user=request.user)
    # Mảng tuple chứa Order đi kèm theo các OrderDetail tương ứng
    orders_vm = []
    for order in orders:
        # Lấy order detail tương ứng
        order_detail = OrderDetail.objects.filter(user=request.user, order=order)
        orders_vm.append((order, order_detail))
    return render(request=request, template_name="order/history.html",
                  context={"orders_vm": orders_vm})


@login_required(login_url="login")
def set_order_done(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_done = True
    order.save()
    return redirect("order_history")


@login_required(login_url="login")
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect("product")

    total = 0
    # Duyệt qua từng cart_item
    for ci in cart_items:
        # Tổng tiền = Đơn giá * số lượng
        total += ci.cart_total()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = Order()
            new_order.user = request.user
            new_order.first_name = form.cleaned_data["first_name"]
            new_order.last_name = form.cleaned_data["last_name"]
            new_order.email = form.cleaned_data["email"]
            new_order.phone_number = form.cleaned_data["phone_number"]
            new_order.address = form.cleaned_data["address"]
            new_order.order_note = form.cleaned_data["order_note"]
            new_order.order_total = total
            # Save
            new_order.save()

            # Chuyển CartItem sang OrderDetail
            for ci in cart_items:
                new_order_detail = OrderDetail()
                new_order_detail.order = new_order
                new_order_detail.user = request.user
                new_order_detail.product = ci.product
                new_order_detail.quantity = ci.quantity
                new_order_detail.product_price = ci.product.price
                new_order_detail.save()
            # Xóa Cart vừa mua
            CartItem.objects.filter(user=request.user).delete()

            return redirect("order_history")
    return redirect("checkout")

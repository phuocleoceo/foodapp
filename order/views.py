from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from cart.models import CartItem
from order.models import Order
from .forms import OrderForm


# Create your views here.
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
        print(form)
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
            return redirect("checkout")
    return redirect("checkout")

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from cart.views import cart_id_from_session
from .forms import RegisterForm, LoginForm
from cart.models import Cart, CartItem
from django.contrib import auth
from .models import User


# Create your views here.
def login(request):
    # Login form submit
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                try:
                    cart = Cart.objects.get(cart_id=cart_id_from_session(request))
                    cart_items_exists = CartItem.objects.filter(cart=cart).exists()
                    if cart_items_exists:
                        cart_items = CartItem.objects.filter(cart=cart)
                        for ci in cart_items:
                            ci.user = user
                            ci.save()
                except:
                    pass

                auth.login(request, user)
                return redirect("/")
        return redirect("login")
    # Login page
    form = LoginForm()
    return render(request=request, template_name="user/login.html",
                  context={"form": form})


def register(request):
    # Register form submit
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]

            user = User.objects.create_user(email=email, first_name=first_name,
                                            last_name=last_name, username=username,
                                            password=password)
            user.phone_number = phone_number
            user.save()
            return render(request=request, template_name="user/login.html")
    # Register page
    form = RegisterForm()
    return render(request=request, template_name="user/register.html",
                  context={"form": form})


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("/")

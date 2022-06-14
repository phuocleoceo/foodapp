from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import auth
from .models import User


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return redirect("login")
    return render(request=request, template_name="user/login.html")


def register(request):
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

    form = RegisterForm()
    return render(request=request, template_name="user/register.html",
                  context={"form": form})


def logout(request):
    pass

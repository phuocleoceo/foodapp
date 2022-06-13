from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.
def login(request):
    form = RegisterForm()
    return render(request=request, template_name="user/login.html",
                  context={"form": form})


def register(request):
    return render(request=request, template_name="user/register.html")


def logout(request):
    pass

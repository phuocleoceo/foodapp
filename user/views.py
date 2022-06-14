from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.
def login(request):
    return render(request=request, template_name="user/login.html")


def register(request):
    form = RegisterForm()
    return render(request=request, template_name="user/register.html",
                  context={"form": form})


def logout(request):
    pass

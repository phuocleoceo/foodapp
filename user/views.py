from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request=request, template_name="user/login.html")


def register(request):
    return render(request=request, template_name="user/register.html")


def logout(request):
    pass

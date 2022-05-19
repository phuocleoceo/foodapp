from django.shortcuts import render


def HomePage(request):
    return render(request=request, template_name="dashboard/home.html")

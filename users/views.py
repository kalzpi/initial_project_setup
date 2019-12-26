from django.views import View
from django.shortcuts import render

# Create your views here.


def LogInView(request):
    return render(request, "users/login.html")

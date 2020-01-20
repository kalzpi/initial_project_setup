from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.shortcuts import render, reverse, redirect


def LogInView(request):

    return render(request, "users/login.html")


def switch_language(request):
    user_language = translation.get_language()
    response = redirect(reverse("core:dashboard"))
    if user_language == "ko":
        translation.activate("en")
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, "en")
    elif user_language == "en":
        translation.activate("ko")
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, "ko")
    return response

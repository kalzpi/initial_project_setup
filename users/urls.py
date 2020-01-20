from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LogInView, name="login"),
    path("switch-lang/", views.switch_language, name="switch-lang"),
]

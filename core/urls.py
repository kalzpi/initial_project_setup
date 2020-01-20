from django.urls import path
from . import views


app_name = "core"

urlpatterns = [path("", views.DashBoardView.as_view(), name="dashboard")]

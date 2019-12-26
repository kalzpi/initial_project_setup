from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "username",
        "first_name",
        "last_name",
    ]


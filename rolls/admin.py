from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Roll)
class RollAdmin(admin.ModelAdmin):
    list_display = [
        "project",
        "roll_type",
        "body",
        "steam_shaft",
        "gear_shaft",
    ]

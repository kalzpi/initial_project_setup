from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Purchasing)
class PurchasingAdmin(admin.ModelAdmin):
    pass

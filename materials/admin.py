from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Substrate)
class SubstrateAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["serial", "material_type"]


@admin.register(models.RollMaterial)
class RollMaterialAdmin(admin.ModelAdmin):
    list_display = [
        "substrate",
        "base_design",
        "status",
        "outer_dia",
        "inner_dia",
        "ic_depth",
        "ic_hardness_min",
        "ic_hardness_max",
        "qt_hardness_min",
        "qt_hardness_max",
    ]
